class GoalCounter:
  def __init__(self):
    self.counter = 0

  def notify(self, event):
    self.counter += 1

