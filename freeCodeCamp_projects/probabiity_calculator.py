import copy
import random

# Consider using the modules imported above.


class Hat():

  def __init__(self, **kwargs):
    self.contents = []
    for k, v in kwargs.items():
      self.contents.extend([k for _ in range(v)])

  def draw(self, number):
    if number >= len(self.contents):
      balls_retrieved = copy.copy(self.contents)
      self.contents.clear()

    else:

      balls_retrieved = []
      for _ in range(number):
        d = random.choice(self.contents)
        balls_retrieved.append(d)
        self.contents.remove(d)
    return balls_retrieved


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  contentsave = copy.copy(hat.contents)
  f = 0
  d = set(list(expected_balls.keys()))
  for _ in range(num_experiments):
    hat.contents = copy.copy(contentsave)
    if (hat.contents) != []:
      draws = hat.draw(num_balls_drawn)

      counts = {}
      for dd in draws:
        counts[dd] = counts.get(dd, 0)+1

      s = set(list(counts.keys()))

      m = 0
      if d.issubset(s):
        for k in expected_balls.keys():
          if counts[k] >= expected_balls[k]:
            m += 1
      if m == len(d):
          f += 1
  return f/num_experiments


hat = Hat(blue=3, red=2, green=6)
probability = experiment(hat=hat, expected_balls={
                         "blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)
print(probability)
