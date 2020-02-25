
from typing import Tuple, List

from picamera import PiCamera
from picamera.array import PiRGBArray
from math import sqrt
import cv2, numpy as np
from cv2 import aruco

from vision.model import CupModel, RobotModel
from vision.detectors import ArucoDetector, CupDetector

Resolution = Tuple[int, int]

class VisionCamera(PiCamera):
    def __init__(self, resolution: Resolution, framerate: int):
        super().__init__(resolution=resolution, framerate=framerate)
        self.aruco_detector = ArucoDetector()
        self.cup_detector = CupDetector()
        self.unwarp = None

    def detectUnwarp(self):
        with PiRGBArray(self, size=self.resolution) as frame:
            self.capture(frame, format='bgr')
            img = frame.array

        board_marker = self.aruco_detector.findBoardMarker(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
        if board_marker:
            print('(camera) - board marker detected')
            br, bl, tl, tr = board_marker[0].tolist()
            side = br[0] - bl[0]
            # side = math.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))

            # NOTE: NEED REAL-WORLD MARKER DIMENSIONS FOR PROPER BOARD POSITION CALC
            dst = np.array([
                [*tl],
                [tl[0] + side, tl[1]],
                [tl[0] + side, tl[1] + side],
                [tl[0], tl[1] + side]
            ], dtype = "float32")

            unwarp = cv2.getPerspectiveTransform(board_marker, dst)
            self.unwarp = unwarp
            print('(camera) - unwarp calculated and set')
        else:
            print('(camera) - *board marker not found')


    def cupsInFrame(self, frame: PiRGBArray) -> List[CupModel]:
        cups = []
        img = frame.array

        # find cups in the frame

        return cups

    def robotsInFrame(self, frame: PiRGBArray) -> List[RobotModel]:
        robots = []
        img = frame.array

        # find robots in the frame

        return robots

    def videoStreamObjects(self):
        stream = PiRGBArray(self, size=self.resolution)
        for frame in self.capture_continuous(stream, format='bgr', use_video_port=True):
            yield (frame, self.cupsInFrame(frame), self.robotsInFrame(frame))
            stream.truncate(0)

    def videoStream(self):
        for frame, cups, robots in self.videoStreamObjects():
            img = frame.array
            # draw stuff on img
            yield img
