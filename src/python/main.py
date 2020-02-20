
import vision.model

from vision.main import beginImageProcessing
from vision.camera import VisionCamera

camera = VisionCamera((640, 480), 32)
vision = vision.model.VisionModel(side = vision.model.CupColour(int(input("Side? (0=GREEN / 1=RED) "))))
beginImageProcessing(None, camera, vision)

print("Hello world!")
