
from picamera import PiCamera
from picamera.array import PiRGBArray
from typing import Tuple
from model import CupModel, RobotModel

Resolution = Tuple[int, int]

class VisionCamera(PiCamera):
    def __init__(self, resolution: Resolution, framerate: int):
        super().__init__(resolution=resolution, framerate=framerate)

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
            yield (cupsInFrame(frame), robotsInFrame(frame))
            stream.truncate(0)
