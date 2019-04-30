def findUnique(char):

  if (len(char)) == 1:
    return True
  myList = []
  for i in char:
    # print(i)
    if i not in myList:
      myList.append(i)
  if len(char) == len(myList):
    return True
  else:
    return False
  # for i in range(1,len(char)+1):
  #   if char[i] != char[n-i]:
  #     return True
  #   else:
  #     return False

answer = findUnique('avengrs')
print(answer)
