#!/usr/bin/env python3


import random
import time
import sqlite3

from bankmodelproject import Account, Bank, Customer, Employee, Profile


if __name__ == "__main__":
	def wait():
		time.sleep(0.25)

	# Creating a central Bank object
	bank = Bank("Byte Bank")
	print("Welcome to {}!".format(bank.name))
	wait()
	stop = False

	# Interactive prompt with user input using a simple while loop.
	while not stop:
		# First question
		print("How may I help you?")
		wait()
		print("1: Create a Byte Bank profile with us to open up a bank account or apply for a job.")
		wait()
		print("2: Sign in to your bank account, if you have a Byte Bank profile with us.")
		wait()
		print("3: More info about Byte Bank.")
		wait()
		print("4: Exit the bank.")
		wait()
		cmd = input()
		print()
		if cmd == "1":
			# Second question: create profile
			print("Thank you for taking the first step in joining Byte Bank.")
			print("Create your Profile ...")
			wait()
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
			# Third question: open bank account or apply for job
			print("What would you like to do next?")
			wait()
			print("1: Open a Byte Bank account")
			wait()
			print("2: Apply for a Byte Bank job")
			wait()
			cmd2 = input()
			print()
			if cmd2 == "1":
				# Fourth question: open bank account
				print("Open your bank account ...")
				wait()
				print("What type of account are you trying to open? (checking or savings)")
				acc_type = input().lower()
				print("Would you like to make an initial deposit? (0 for no, any other value for yes)")
				balance = abs(int(input()))
				print("Choose a pin number (must be a 4-digit number):")
				pin_number = input()
				acc_number = bank.generate_acc_number()
				print("We have assigned you an account number: \n{}".format(acc_number))
				wait()
				account = bank.create_account(acc_number, acc_type, balance, pin_number)
				print("What is your username for your profile?")
				username = input().lower()
				bank.create_customer(username, account)
				print(account)
				print("Bank account created.")
				wait()
				print()
			elif cmd2 == "2":
				# Fifth question: apply for job
				print("Apply for a Byte Bank job ...")
				wait()
				print("What job would you like?")
				job = input().lower().capitalize()
				print("What salary ($ per hour) would you like?")
				salary = int(input())
				print("What is your username for your profile?")
				username = input().lower()
				bank.create_employee(username, job, salary)
				print("You applied for the job of {0}.".format(job))
				wait()
				print("Congratulations! You got the job!")
				wait()
				print()
			else:
				# Unknown input
				print("Sorry, I cannot do that.")
				wait()
				print()
		elif cmd == "2":
			# Sign in to your bank account
			print("Please enter your account credentials ...")
			wait()
			print("Username:")
			username = input().lower()
			print("Password:")
			password = input()
			print()
			if bank.has_profile(username):
				if bank.log_in(username, password):
					customer = bank.get_customer(username)
					print("Welcome back, {0} {1}!".format(customer.first_name, customer.last_name))
					wait()
					print("What would you like to do with your account?")
					wait()
					print("1: Check account balance.")
					wait()
					print("2: Deposit into account.")
					wait()
					print("3: Withdraw from account.")
					wait()
					print("4: Get all account information.")
					cmd2 = input()
					if cmd2 == "1":
						# Check account balance
						print("Your account balance: ${0}".format(customer.account.balance))
						wait()
						print()
					elif cmd2 == "2":
						# Deposit into account
						print("How much would you like to deposit?")
						amount = abs(int(input()))
						bank.deposit(customer.username, amount)
						print("Deposited ${0} in your account.".format(amount))
						wait()
						print()
					elif cmd2 == "3":
						# Withdraw from account
						print("How much would you like to withdraw?")
						amount = int(input())
						if customer.account.withdraw(amount):
							bank.withdraw(amount)
							print("Withdrew {} from your account.".format(amount))
							print("Current balance: ${}".format(customer.account.balance))
							wait()
							print()
						else:
							print("You do not have enough money in your account.")
							print("Current balance: ${}".format(customer.account.balance))
							wait()
							print()
					elif cmd2 == "4":
						# Get all account info
						print(customer.account)
						wait()
						print()
					else:
						# Unknown input
						print("Sorry, I cannot do that.")
						wait()
						print()
				else:
					print("The password you entered was incorrect.")
			else:
				print("Sorry, there is no profile with that username in our database.")
				wait()
		elif cmd == "3":
			# Print string representation of the bank object
			print("Here is some information about the bank ...")
			print(bank)
			wait()
			print()
		elif cmd == "4":
			# Exit bank
			print("Thank you, have a Byte day!")
			wait()
			stop = True
		else:
			# Unknown input
			print("Sorry, I cannot do that.")
			wait()
			print()
	# End of loop
	print("Program exited.")
