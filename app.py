# Login Details Storage Program
# Written by mal64 (mal64#5482)
# 07.04.23


# Imports
import os


# Variables
password = 0
username = 0
sitename = 0
yesorno = 0


# Print title
print("✨ mal64's Login Details Storage Program ✨")
print()


# Get input
username = input('Enter your username: ')
password = input('Enter your password: ')
sitename = input('What website are these details for? (example: www.youtube.com) ')
print()


# Check if website exists
ip_list = [sitename]
for ip in ip_list:
    response = os.popen(f"C:\Windows\System32\ping {ip}").read()
    if "Received = 4" in response:
        print('Website authenticity verified.')
    else:
        print('Could not verify authenticity of website, please restart the program and try again. If the URL you entered is valid, the website may be down.')
        print()
        input('Press enter to close the program. ')
        quit()


# Print details
print()
print('Username: ' + username)
print('Password: ' + password)
print('Website URL: ' + sitename)


# Are these correct?
print()
yesorno = (input('Are these details correct? ("1" for Yes or "0" for No) '))
print()
if yesorno == '1':
    # Saving details
    file = open('details.txt', 'w')
    file.write(username + '\n')
    file.write(password + '\n')
    file.write(sitename)
    file.close()
    print("Login details saved.")
    print()
    input('Press enter to close the program. ')
    quit()
if yesorno == '0':
    print('Please close the program and enter your details again.')
    print()
    input('Press enter to close the program. ')
    quit()
