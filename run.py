#!/usr/bin/env python3


import os
import random
import time

from bankmodelproject import Account, Bank, Customer, Employee, Profile


if __name__ == "__main__":
	def wait(n):
		time.sleep(n)

	def clear():
		os.system("clear")

	# Creating a central Bank object
	bank = Bank("Byte Bank")
	print("Welcome to {}!".format(bank.name))
	wait(0.25)
	stop = False

	# Interactive prompt with user input using a simple while loop.
	while not stop:
		# First question
		print("How may I help you?")
		wait(0.25)
		print("1: Create a Byte Bank profile.")
		wait(0.25)
		print("2: Create/open a new bank account.")
		wait(0.25)
		print("3: Apply for a job.")
		wait(0.25)
		print("4: Sign in to your bank account.")
		wait(0.25)
		print("5: More information about Byte Bank.")
		wait(0.25)
		print("6: Exit the bank.")
		wait(0.25)
		cmd = input()
		print()
		if cmd == "1":
			# Create profile
			clear()
			print("Thank you for taking the first step in joining Byte Bank.")
			print("Create your Profile ...")
			wait(0.25)
			print("First name (maximum: 50 characters):")
			first_name = input().lower().capitalize()
			print("Last name (maximum: 50 characters):")
			last_name = input().lower().capitalize()
			print("Sex (male/m, female/f, other/x):")
			sex = input().lower()
			print("Age (years):")
			age = int(input())
			print("Username (maximum: 25 characters):")
			username = input().lower()
			print("Password:")
			password = input()
			bank.create_profile(first_name, last_name, sex, age, username, password)
			print(Profile(first_name, last_name, sex, age, username, password))
			print("Profile created.")
			print()
		elif cmd == "2":
			# Create/open a new bank account.
			clear()
			print("Create a new bank account ...")
			wait(0.25)
			print("In order to create a new bank account, enter the username for your profile below.")
			wait(0.25)
			print("If you have not yet created a profile, enter \"exit\" and then enter \"1\" to create one.")
			wait(0.25)
			username = input("Username: \n").lower()
			# TODO: Handle exiting this inner loop.
			if username == "exit":
				break
			wait(0.25)
			print("Which type of account are you trying to open? (checking or savings)")
			acc_type = input().lower()
			print("Would you like to make an initial deposit? (0 for no, any other value for yes)")
			balance = abs(int(input()))
			print("Choose a pin number (must be a 4-digit number):")
			pin_number = input()
			acc_number = bank.generate_acc_number() # TODO: Read from database to check if account number has been assigned.
			print("We have assigned you an account number: \n{0}".format(acc_number))
			wait(0.25)
			account = bank.create_account(acc_number, acc_type, balance, pin_number)
			bank.create_customer(username, account)
			print(account)
			print("Bank account created.")
			wait(0.25)
			print()
		elif cmd == "3":
			# Apply for a job.
			clear()
			print("Apply for a Byte Bank job ...")
			wait(0.25)
			print("In order to apply for a job, enter the username for your profile below.")
			wait(0.25)
			print("If you have not yet created a profile, enter \"exit\" and then enter \"1\" to create one.")
			wait(0.25)
			username = input("Username: \n").lower()
			# TODO: Handle exiting this inner loop.
			if username == "exit":
				break
			wait(0.25)
			print("What job would you like?")
			job = input().lower().capitalize()
			print("What salary ($ per hour) would you like?")
			salary = int(input())
			print("You applied for the job of {0}.".format(job))
			wait(0.25)
			print("Management is conducting a background check, and reviewing your resume ...")
			wait(2)
			print("Please wait ...")
			wait(1)
			print(".")
			wait(1)
			print(".")
			wait(1)
			print(".")
			wait(1)
			x = random.randint(0, 3)
			if x == 0:
				print("Congratulations! You got the job!")
				bank.create_employee(username, job, salary)
			elif x > 0:
				print("Sorry, you did not get the job. Please re-apply again soon!")
			wait(0.25)
			print()
		elif cmd == "4":
			# Sign in to your bank account.
			clear()
			print("Sign in to your bank account ...")
			wait(0.25)
			print("If you have not yet created a profile or bank account, enter \"exit\", then \"1\" and \"2\" to create them.")
			wait(0.25)
			print("Username:")
			username = input().lower()
			# TODO: Handle exiting this inner loop.
			if username == "exit":
				break
			print("Password:")
			password = input()
			print()
			# If there exists a profile in the database with this username.
			if bank.has_profile(username):
				# If the password for this username in the database matches the entered password.
				if bank.log_in(username, password):
					log_in_stop = False
					# Emulates a user bank account session until they log out.
					while not log_in_stop:
						clear()
						customer = bank.get_customer(username)
						print("Welcome back, {0} {1}!".format(customer.first_name, customer.last_name))
						wait(0.25)
						print("What would you like to do with your bank account?")
						wait(0.25)
						print("1: Check account balance.")
						wait(0.25)
						print("2: Deposit into account.")
						wait(0.25)
						print("3: Withdraw from account.")
						wait(0.25)
						print("4: Get all account information.")
						wait(0.25)
						print("5: Log out of your bank account.")
						cmd2 = input()
						print()
						if cmd2 == "1":
							# Check account balance
							clear()
							print("Your account balance: ${0}".format(customer.account.balance))
							input("Press \"Enter\" to return to the menu ...")
						elif cmd2 == "2":
							# Deposit into account
							clear()
							print("How much would you like to deposit?")
							amount = abs(int(input()))
							bank.deposit(customer.username, amount)
							print("Deposited ${0} in your account.".format(amount))
							print("Account balance: ${0}".format(customer.account.balance + amount))
							input("Press \"Enter\" to return to the menu ...")
						elif cmd2 == "3":
							# Withdraw from account
							clear()
							print("How much would you like to withdraw?")
							amount = abs(int(input()))
							if bank.withdraw(customer.username, customer.account.balance, amount):
								print("Withdrew ${0} from your account.".format(amount))
								print("Account balance: ${0}".format(customer.account.balance - amount))
								input("Press \"Enter\" to return to the menu ...")
							else:
								print("You do not have enough money in your account.")
								print("Account balance: ${0}".format(customer.account.balance))
								input("Press \"Enter\" to return to the menu ...")
						elif cmd2 == "4":
							# Get all account info
							clear()
							print(customer.account)
							input("Press \"Enter\" to return to the menu ...")
						elif cmd2 == "5":
							# Logs out of bank account and returns to main menu.
							log_in_stop = True
						else:
							# Unknown input
							print("Sorry, I cannot do that.")
							input("Press \"Enter\" to return to the menu ...")
				else:
					print("The password you entered was incorrect.")
					wait(0.25)
					print()
			else:
				print("Sorry, there is no profile with that username in our database.")
				wait(0.25)
				print()
		elif cmd == "5":
			clear()
			# Prints string representation of the main Bank object.
			print("Here is some information about this bank ...")
			print(bank)
			wait(0.25)
			print()
		elif cmd == "6":
			# Exits bank.
			print("Thank you, enjoy the rest of your day!")
			wait(0.25)
			stop = True
		else:
			# Handles unknown input.
			print("Sorry, I cannot do that.")
			wait(0.25)
			print()
	# End of loop.
	print("Program exited.")
