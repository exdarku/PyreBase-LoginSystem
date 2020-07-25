'''
Script made by exdarku
Follow me on github for more python projects!.
https://github.com/exdarku

MythSecPH
https://mythsecph.xyz/profile/exdarku
'''

import os
import getpass
import pyrebase

config = {	
	# Your pyrebase config
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


header = "=========================================="
appName = "Login System"

def main():
	print(header)
	print(appName)
	print(header)
	print("1.) Login\n2.) Register\n3.) Exit")
	choice = input(">")
	if choice == "1":
		login()
	elif choice == "2":
		register()
	elif choice == "3"
		exit()

def login():
	print(header)
	print(appName)
	print(header)
	print("Please enter your details to login.")
	email = input("Your email address:")
	p = getpass.getpass(prompt="Password:")
	user = auth.sign_in_with_email_and_password(email, p)
	main_menu()

def register():
	print(header)
	print(appName)
	print(header)
	print("Please enter your details to register.")
	email = input("Your email address:")
	p = getpass.getpass(prompt="Password:")
	# Remove the hash below to add email verification!.
	# auth.send_email_verification(user['idToken'])
	auth.create_user_with_email_and_password(email, password)
	main()

def main_menu():
	print("This is your main menu.")