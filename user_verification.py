# 1) check if a user's name is not empty
# 2) check if the user name is a str, is a None and is longer than 5 characters 
# 3) check if the user is either admin or a moderator
# 4) check if the user is banned

# 5) age is greater than or equal to 18

# 6) password: 8 to 16 characters 2) atleast 1 symbol 3) atleast 1 number 4) atleast 1 upper case letter 5) atleast 1 lower case letter

# 7) check if a user's email is not empty. Contains "@", and ends with ".com, .it, .net. .me"
# 8) check if the user is banned or their e-mail is verified

#---------------------------------------------------------------------------------------------------------------------------------
# USER NAME
user_banned = ("Lorenzo", "Maurizio", "Francesco", "Roberta","Ganea", "Paolo")
user_admin = ("Daniel", "Davide", "Guido")
user_mod = ("Roberto", "Laurent", "luca", "Paolo Enrico", "Edoardo")
while True:
    name = input("Enter your name: ").strip().capitalize().strip() # user input + dealing with upper/lowercases

    if not name: # if the input is left empty, loop again
        print("Your name can't be empty")
        continue
    if name is None or len(name) <= 3 or not name.isalpha(): # rejects and loops again if the name is: None, not alphabetical, less than 3 letters
        print("Invalid Name, please make sure your name contains atleast 4 alphabetical characters")
        continue

    if name in user_banned: # if the user is in the banned list, break the loop
        print(f"{name} is banned.")
        break
    if name in user_admin or name in user_mod: # if the user is a admin/mod break the loop
        print(f"Welcome {name}!")
        break
    else: # if all of the above pass send this message and break the loop
      print(f"welcome in: {name}")
    break
#---------------------------------------------------------------------------------------------------------------------------------
# USER AGE
while True:
    age = input("Enter your age: ").strip()

    if not age.isnumeric():
        print("Please type only numbers")
        continue

    age = int(age)
    if age <= 18:
        print("You most be atleast 18 years old")
    else: 
        print("Age verified")
    break
#---------------------------------------------------------------------------------------------------------------------------------
# USER PASSWORD
special_symbol = ("<", ">", ",", ".", ";", ":", "-", "_", "@", "#", "§", "[", "]", "!", "|", "£", "$", "%", "&", "?")
while True:
    pw = input("Enter your password: ").strip() # askes the user for a password and strips the pw from spaces from both the left/right side

    if " " in pw: # checks if there's a space
        print("spaces aren't allowed in the password")
        continue
    if len(pw) <= 8: # checks if the password characters are less than 8
        print("for security reasons your password has to contain atleast 8 characters")
        continue
    if len(pw) >= 20: # checks if the password characters are more than 20
        print("password length should not be greater than 20 characters")
        continue
    if not any(char in special_symbol for char in pw): # checks if there's a symbol
        print("Your password most have atleast 1 symbol")
        continue
    if not any(char.isdigit() for char in pw): # checks if there's a number 
        print("Your password most have atleast 1 number")
        continue
    if not any(char.isupper() for char in pw): # checks if there's a upper case letter
        print("Your password most have atleast 1 upper case letter")
        continue
    if not any(char.islower() for char in pw): # checks if there's a lower case letter
        print("Your password most have atleast 1 lower case letter")
        continue
    else: # if the above conditions get a pass return the print below and break
        print("that's a valid password")
    break
#---------------------------------------------------------------------------------------------------------------------------------
# EMAIL loop 
valid_domain = ("gmail.com", "hotmail.it", "libero.it", "proton.me", "yahoo.com") # list of valid domains
banned_domain = ("spam.com", "fake.org", "bot.net") # list of banned domains
verified_domain = ("emmi@gmail.com", "davide@hotmail.it", "rob@libero.it", "brescia@yahoo.com") # list of verified domains
while True: # loop to allow to keep asking to input the email for aslong as the user doesn't input a valid domain
  email = input("Enter your email: ").lower().strip() # asks the user to input a email

  if not email: # checks for empty str
     print("your email can't be empty")
     continue # continue looping whenever the input doesn't pass this validation
  if "@" not in email: # checks for @
     print("your email must contain '@',")
     continue 
  if email.endswith (banned_domain): # checks for banned emails
     print("Banned domain")
     continue 
  if not email.endswith(valid_domain): # checks if the input still somehow isn't valid
     print("Email domain is not valid") 
     continue 
  if email in verified_domain: # checks if the input is in said list
    print("Verified email") 
    break
  else: # if the loop gets through here breaks out of the loop
    print("Valid email") 
  break # breaks the loop
#---------------------------------------------------------------------------------------------------------------------------------
