
from typing import Tuple, Dict
from model import CupColour, CupModel, RobotModel
from worldmodel.position import BoardPosition
import cv2, numpy as np

CupSpecification = Tuple(Tuple(int, int, int), Tuple(int, int, int))

class ArucoDetector:
    BOARD_MARKER_ID = 42

    def __init__(self):
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
        self.parameters =  aruco.DetectorParameters_create()

    def findRects(self, imgbw):
        aruco_rects = {}
        corners, ids, rejected = aruco.detectMarkers(imgbw, self.aruco_dict, parameters=self.parameters)
        for i in range(len(ids)):
            if ids[i][0] in aruco_rects:
                aruco_rects[ids[i][0]].append(corners[i])
            else:
                aruco_rects[ids[i][0]] = [corners[i]]

        return aruco_rects

    def findRectListById(self, imgbw, aruco_id):
        aruco_rects = self.findRects(imgbw)
        return aruco_rects[aruco_id] if aruco_id in aruco_rects else None

    def findBoardMarker(self, imgbw):
        board_marker = self.findRectListById(imgbw, self.BOARD_MARKER_ID)
        return board_marker[0] if board_marker else None

class CupDetector:
    DEFAULT_COLOUR_RANGES = { ((67, 50, 0), (87, 255, 255)): CupColour(0),
                              ((170, 50, 50), (180, 255, 255)): CupColour(1) }
    CUP_DIAMETER = 72

    def __init__(self, colour_ranges: Dict[CupSpecification, CupColour] = DEFAULT_COLOUR_RANGES):
        self.colour_ranges = colour_ranges

    def green_mask_fix(green_mask):
        kernel = np.ones((9,9), np.uint8)
        return cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel)

    def red_mask_fix(red_mask):
        kernel = np.ones((3,3), np.uint8)
        red_mask_t = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
        kernel = np.ones((9,9), np.uint8)
        return cv2.morphologyEx(red_mask_t, cv2.MORPH_CLOSE, kernel)

    def positions(self, img, unwarp, correction=self.CUP_DIAMETER//2):
        cups = []
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        for colour_range, colour in self.colour_ranges:
            mask = cv2.inRange(hsv, *colour_range)

            if colour == CupColour.GREEN:
                mask = green_mask_fix(mask)
            elif colour == CupColour.RED:
                mask = red_mask_fix(mask)

            for c in cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE):
                if 1000 < cv2.contourArea(c):
                    rect = cv2.boundingRect(c)
                    # must be unwarped and adjusted
                    # cups.append(CupModel(colour, BoardPosition(rect[0]+rect[2]/2, rect[1]+rect[3])))

        return cups
