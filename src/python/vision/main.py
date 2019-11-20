
from time import sleep
from threading import Thread
from .model import VisionModel, CupColour


class ImageProcessor(Thread):
	def __init__(self, callback):
		Thread.__init__(self)
		self.__callback = callback

	def run(self): # TODO
		while True:
			sleep(1)
			self.__callback(VisionModel([], [], CupColour.GREEN))


# start necessary background threads that process images
def beginImageProcessing(callback):
	ip = ImageProcessor(callback)
	ip.start()
