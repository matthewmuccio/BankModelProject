#!/usr/bin/env python3


import time

from bankmodelproject import Account, Bank, Customer, Employee, Person


if __name__ == "__main__":
	def create_bank(name, balance, customers):
		return Bank(name, balance, customers)

	bank = create_bank("Byte Bank", 0, [])
	print("Welcome to {}!".format(bank.name))
	stop = False

	# Interactive prompt with user input using a simple while loop.
	while not stop:
		print("How may I help you?")
		print("Type the number (1, 2, 3) to select option.")
		print("1: Create a new account")
		print("2: Log in to your account")
		print("3: Exit the bank")
		cmd = input()
		if cmd == "1":
			print("Creating your new account...")
			time.sleep(2)
			print()
		elif cmd == "2":
			print("Logging you in ...")
			time.sleep(2)
			print()
		elif cmd == "3":
			stop = True
			print("Thanks very much, have a nice day!")
		else:
			print("Sorry, I cannot do that.")
			time.sleep(2)
			print()
