
from vision.model import VisionModel

class Planner:
	def __init__(self):
		pass

	def visionModelUpdated(self, model: VisionModel):
		print(f"Planner vision model updated: {model}")

	def run(self):
		print("Running planner")
