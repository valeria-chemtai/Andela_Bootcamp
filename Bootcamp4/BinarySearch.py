class BinarySearch(list):
  length = 0
  def __init__(self, a, b):
    
    self.length = a
    self.step=b
    super(BinarySearch, self).__init__()
    value = b
    while value <= (a * b):
      self.append(value)
      value += b

  def search(self, value):
    count = 0
    i = self
    while len(i) > 1:
      count += 1
      half = len(i) / 2
      if value == i[half]:
        i = []
        
      elif value > i[half - 1]:
        i = i[half:len(i) - 1]
        
      else:
        i = i[0:half]
        
      try:
        index = self.index(value)
        
      except:
        index = - 1
        
      return {'count': count, 'index': index}

