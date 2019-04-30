def findUnique(char):
  l = sorted(char)
  flag = False
  print(l)
  for i in range(1,len(l)+1):
    print('ith',l[i])
    print('i-1th',l[i-1])
    if l[i] != l[i-1]:
      flag = True
    else:
      flag= False
      break

  if (flag == True):
    return True
  else:
    return False

answer = findUnique('defhgtyphy')
print(answer)
