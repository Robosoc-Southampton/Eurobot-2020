
from time import sleep
from threading import Thread
from vision.camera import VisionCamera
from vision.model import VisionModel


class ImageProcessor(Thread):
    def __init__(self, callback, camera: VisionCamera, vision: VisionModel):
        Thread.__init__(self)
        self.__callback = callback
        self.camera = camera

    def run(self):
        # get object positions for robots, cups, etc. from the video stream
        for objectUpdate in self.camera.videoStreamObjects():
            # do stuff with the data (altering self.vision ?)
            # self.vision is passed by src/python/main.py and can be accessed easily from there
            # positions will be used for path finding etc.
            # objectUpdate: Tuple[List[CupModel], List[RobotModel]]
            pass

# start necessary background threads that process images
def beginImageProcessing(callback, camera: VisionCamera, vision: VisionModel):
    ip = ImageProcessor(callback, camera, vision)
    ip.start()
