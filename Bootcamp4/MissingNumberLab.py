def find_missing(list1,list2):
  missing = []
  if list1 == list2 or (list1 == [] and list2 == []):
    return 0
  else:
    for i in list1:
      if i not in list2:
        missing.append(i)
    for i in list2:
      if i not in list1:
        missing.append(i)
  return missing