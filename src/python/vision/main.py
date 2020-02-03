
from time import sleep
from threading import Thread
<<<<<<< HEAD
from .model import VisionModel, CupColour
=======
>>>>>>> 793a2ae... Misc project layout stuff


class ImageProcessor(Thread):
	def __init__(self, callback):
		Thread.__init__(self)
		self.__callback = callback

<<<<<<< HEAD
	def run(self): # TODO
		while True:
			sleep(1)
			self.__callback(VisionModel([], [], CupColour.GREEN))
=======
	def run(self):
		sleep(1)
		print("I am running in a thread, yeet!")
>>>>>>> 793a2ae... Misc project layout stuff


# start necessary background threads that process images
def beginImageProcessing(callback):
	ip = ImageProcessor(callback)
	ip.start()
