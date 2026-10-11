# case scenario: checking if somebody can enter a venue
# request the user to input a valid number of reservation return error if a 12 digit value isn't inputted
# request the user to input their age
# reguest the user for the ticket
# Ask the user wether hes a member 
# Ask the user wether hes a vip 
# access is granted if: age >= 18 / number of reservation is exactly 12 digits / ticket = True / and is either a member or a vip
number_reservation = True
age = 30
has_ticket = True
is_member = True
is_vip = False
access_granted = age >= 18 and has_ticket == True and (is_member or is_vip) # because the last and requires either conditions bethween or to be True and one indeed is, it returns true
#------------------True---------------True------------------True-------False---- = True
print(f"Access granted: {access_granted}") # {access_granted} returns the boolean of the variable access_granted which is True in this case