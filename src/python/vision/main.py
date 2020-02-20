
from time import sleep
from threading import Thread
from camera import VisionCamera


class ImageProcessor(Thread):
	def __init__(self, callback, camera: VisionCamera):
		Thread.__init__(self)
		self.__callback = callback
		self.camera = camera

	def run(self):
		# get object positions for robots, cups, etc. from the video stream
		while objects := self.camera.videoStreamObjects():
			# do stuff with the data
			pass

# start necessary background threads that process images
def beginImageProcessing(callback, camera: VisionCamera):
	ip = ImageProcessor(callback, camera)
	ip.start()
