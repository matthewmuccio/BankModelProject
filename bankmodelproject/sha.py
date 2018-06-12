#!/usr/bin/env python3


import hashlib


profiles = {}

# Encrypt a plaintext string (password) with SHA-512 cryptographic hash function.
def encrypt_password(password):
	return hashlib.sha512(str.encode(password)).hexdigest()

# Determine if a plaintext string (password) matches the 512-bit encrypted version that is stored.
def check_log_in(username, password):
	return encrypt_password(password) == profiles[username]


if __name__ == "__main__":
	stop = False
	# Begin interactive prompt
	while not stop:
		print("Hello! How can I help you?")
		print("1: Create an account")
		print("2: Log in to your account")
		print("3: Exit the prompt")
		cmd = input()
		if cmd == "1":
			print("Enter your desired username:")
			username = input()
			print("Enter your desired password:")
			password = input()
			profiles[username] = encrypt_password(password)
			print()
		elif cmd == "2":
			print("Enter your username:")
			username = input()
			print("Enter your password:")
			password = input()
			if check_log_in(username, password):
				print("Logged in successfully!")
			else:
				print("Your username or password was incorrect.")
			print()
		elif cmd == "3":
			print("Thank you, have a great day!")
			stop = True
		else:
			print("Sorry, I cannot do that.")
			print()
	# Loop exited
	print("Program exited.")
