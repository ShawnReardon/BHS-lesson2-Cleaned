
# PART 4--Explore Activity 
def howOldIsLucy(lucyAge, yourAge):
  #Computes the difference in age between Lucy and user and stores it in a variable
  ageDifference = int(lucyAge) - int(yourAge)
  
  print("Lucy is", ageDifference, "year(s) from your age")
  # Stores the user response in a variable
  response = input("How old is Lucy? ")
  # Compares the user response as an integer to the age of Lucy and executes the branch if the response is equal ( == ) to the age of Lucy
  if int(response) == int(lucyAge):
    print("Nice work! Lucy is", lucyAge)
  else:
    print("Hmmmmm...try again")
    # This function will call itself if the user inputs an incorrect value for the age of Lucy, allowing the user another chance to answer
    howOldIsLucy(lucyAge, yourAge)

def howOldIsLucyWhile(lucyAge, yourAge):
  #Computes the difference in age between Lucy and user and stores it in a variable
  ageDifference = int(lucyAge) - int(yourAge)
  
  print("Lucy is", ageDifference, "year(s) from your age")
  # Stores the user response in a variable
  response = -100
  # Controls the message printed to the user inside the while loop below
  firstRun = True

  # Compares the user response as an integer to the age of Lucy and the program remains inside the while loop until the condition is made false. In other words, until the user responds with the correct age
  while int(response) != int(lucyAge):
    if firstRun:
      response = input("How old is Lucy? ")
      firstRun = False
    else:
      print("Hmmmmm...try again")
      response = input("How old is Lucy? ")

  print("Nice work! Lucy is", lucyAge)

