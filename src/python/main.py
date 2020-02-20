
import vision.model

from vision.main import beginImageProcessing
from vision.camera import VisionCamera

camera = VisionCamera((640, 480), 32)
beginImageProcessing(None, camera)

print("Hello world!")
