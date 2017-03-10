def find_missing(list1,list2):
  missing = []

  for i in list1:

    if i not in list2:  #if elements in list1 are not in list2 plce them in list missing with those elements in it
      missing.append(i)

  for i in list2:

    if i not in list1: #if elements in list2 are not in list1 place them in missing
      missing.append(i)

  if len(missing) > 0:
    if len(missing) == 1: #if there is only one element in missing array after tests return that value
      return missing[0]
    else:
      return missing  #otherwise return list with missing elements
  else:
    return 0