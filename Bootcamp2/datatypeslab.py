"""python function for taking an argument, compare and return results"""
def data_type(n):
  if type(n)==type(""): #checking if argument is a string
    return len(n)
  elif type(n)==type(None): # check if there's no argument
    return "no value"
  elif type(n)==type(True): #check if type of argument is boolean
    return n
  elif type(n)==type(1): #elif block with if-else conditions to check if integer is less or more than 100
    if(n<100):
      return "less than 100"
    else:
      return "more than 100"
  elif type(n)==type([]): #condition checks if type list and return element in index 2
    if len(n)>=3:
      return n[2]
    else:
      return None
      