import random 
print("Do you want MOMOs? You can check in here below 🤷. Fill up the form.")
print("Note: Category implies Children, Students, Pregnant Women, Elderlies, Men, Women")
salary = float(input("Enter your salary:"))
savings = float(input("Enter your savings:"))

if (salary < 30000 or savings < 4000):
  print("Hmm, let's check if you're qualified for special treatment or not. Answer the following,")
  
  specialcheck1 = input("Where are you originally from?")
  if specialcheck1 == "Dharan" or specialcheck1 == "DHARAN" or specialcheck1 == "dharan":
    print("Congratulations!!! You're getting free momos for lifetime! Also a 🙌 from Tutors!")
    
  else:
      specialcheck2 = input("How many times have you watched the movie 3 idiots?")
      
      if specialcheck2 == "More than ten":
        print("You get 10 plate of free momos!!!")
        
      else:
          specialcheck3 = input("Are you a magician?")
          numberofmomo = random.randint(1,10)
          if specialcheck3 == "Yes" or specialcheck3 == "yes":
               print("You are getting " + str(numberofmomo) + " plates of free momos" )
               
          else:
              category = str(input("Enter your category"))
              if category == ("Children" or "Students" or "Pregnant Women" or "Elderlies"):
                  print("Hmm, let's check if you're qualified for special treatment or not. Answer the following,")
  
                  specialcheck1 = input("Where are you originally from?")
                  if specialcheck1 == "Dharan" or specialcheck1 == "DHARAN" or specialcheck1 == "dharan":
                      print("Congratulations!!! You're getting free momos for lifetime! Also a 🙌 from Tutors!")
    
                  else:
                      specialcheck2 = input("How many times have you watched the movie 3 idiots?")
                      if specialcheck2 == "More than ten":
                          print("You get 10 plate of free momos!!!")
        
                      else:
                          specialcheck3 = input("Are you a magician?")
                          numberofmomo = random.randint(1,10)
                          if specialcheck3 == "Yes" or specialcheck3 == "yes":
                                print("You are getting " + str(numberofmomo) + " plates of free momos" )
                          else:
                            print("We're so sorry! Stay safe! 🤗")
              
else:
  print("We're so sorry! Stay safe! 🤗")

