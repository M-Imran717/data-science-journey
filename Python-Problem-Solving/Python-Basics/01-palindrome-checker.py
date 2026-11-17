#Program to check the pallindromic word 

def CheckPallindrome(word):
  start = 0
  end = len(word)-1
  IsPallindrome = True
  while(start <= end):
    if word[start] != word[end]:
      IsPallindrome = False
      break
    else:
      start = start + 1
      end = end - 1
  if IsPallindrome == True:
    return True
  else:
    return False

while True:
  print("1 : Check Word : ")
  print("2 : Exit  : " )
  UserChoice = int(input("Enter Your Choice : "))
  if UserChoice == 2:
    print("Exit : ")
    break
  else:
    UserInput = input("Enter Your Word : ")
    if CheckPallindrome(UserInput):
      print(f"Yes the word : {UserInput} is Pallindromic : ")
    else:
      print(f"No the word : {UserInput} is not Pallindromic : ")
 
  
  
  