
from picamera import PiCamera
from picamera.array import PiRGBArray
from typing import Tuple

Resolution = Tuple[int, int]

class VisionCamera(PiCamera):
    def __init__(self, resolution: Resolution, framerate: int):
        super().__init__(resolution=resolution, framerate=framerate)

    def cupsInFrame(self, frame: PiRGBArray) -> List[CupModel]:
        cups = []
        img = frame.array

        # find cups in the frame

        return cups

    def videoStreamObjects(self):
        pass
