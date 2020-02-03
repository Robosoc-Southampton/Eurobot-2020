
from time import sleep
from threading import Thread


class ImageProcessor(Thread):
	def __init__(self, callback):
		Thread.__init__(self)
		self.__callback = callback

	def run(self):
		sleep(1)
		print("I am running in a thread, yeet!")


# start necessary background threads that process images
def beginImageProcessing(callback):
	ip = ImageProcessor(callback)
	ip.start()
