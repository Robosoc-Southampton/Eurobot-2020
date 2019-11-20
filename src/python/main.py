
import vision.model

from vision.main import beginImageProcessing
from pfp.Planner import Planner

planner = Planner()

beginImageProcessing(planner.visionModelUpdated)

planner.run()
