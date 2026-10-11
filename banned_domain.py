# request a user input for the email:
# if the domain of the email is within the banned list, deny access to the user
# otherwise welcome them in
domain = ["gmail.com", "proton.io", "hotmail.it", "hotmail.com", "libero.it"]
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)