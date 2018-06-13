import sqlite3
import hashlib

from bankmodelproject.account import Account
from bankmodelproject.customer import Customer
from bankmodelproject.employee import Employee
from bankmodelproject.profile import Profile


class Bank:
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance

	def create_profile(self, first_name, last_name, sex, age, username, password):
		pw = self.encrypt_password(password)
		connection = sqlite3.connect("master.db", check_same_thread=False)
		cursor = connection.cursor()
		cursor.execute(
			"""INSERT INTO profiles(first_name, last_name, sex, age, username, password)
			VALUES(?,?,?,?,?,?);""", (first_name, last_name, sex, age, username, pw)
		)
		connection.commit()
		cursor.close()
		connection.close()

	# Encrypt a plaintext string (password) with SHA-512 cryptographic hash function.
	def encrypt_password(self, password):
		return hashlib.sha512(str.encode(password)).hexdigest()

	# Generates a random 10-digit string for the user's account number.
	def generate_acc_number():
		return "".join([str(random.randint(0,9)) for _ in range(10)])

	def create_account(self, acc_number, acc_type, balance, pin_number):
		a = Account(acc_number, acc_type, balance, pin_number)
		self.balance += balance
		return a

	def create_customer(self, username, account):
		connection = sqlite3.connect("master.db", check_same_thread=False)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM profiles WHERE username=?", (username,))
		row = cursor.fetchall() # List of tuples (rows)
		print(row)
		i, first_name, last_name, sex, age, username, password = row[0]
		cursor.execute(
			"""INSERT INTO customers(first_name, last_name, sex, age, username, password, acc_number, acc_type, balance, pin_number)
			VALUES(?,?,?,?,?,?,?,?,?,?);""", (first_name, last_name, sex, age, username, password, account.acc_number, account.acc_type, account.balance, account.pin_number)
		)
		connection.commit()
		cursor.close()
		connection.close()

	def create_employee(self, profile, job, salary):
		e = Employee(profile, job, salary)
		connection = sqlite3.connect("master.db", check_same_thread=False)
		cursor = connection.cursor()
		cursor.execute(
			"""INSERT INTO employees(first_name, last_name, sex, age, username, password, job, salary)
			VALUES(?,?,?,?,?,?,?,?);""", (first_name, last_name, sex, age, username, password, job, salary)
		)
		connection.commit()
		cursor.close()
		connection.close()

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

	def __str__(self):
		title = "[ BANK ]".center(30, "-")
		name = "Name: {0}".format(self.name).center(30, " ")
		balance = "Balance: ${0}".format(self.balance).center(30, " ")
		end = "-".center(30, "-")
		return "\n{0}\n{1}\n{2}\n{3}\n".format(title, name, balance, end)
