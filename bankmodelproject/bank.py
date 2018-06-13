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

	def create_account(self, acc_number, acc_type, balance, pin_number):
		a = Account(acc_number, acc_type, balance, pin_number)
		self.balance += balance
		return a

	def create_customer(self, profile, account):
		c = Customer(profile, account)
		return c

	def create_employee(self, profile, job, salary):
		e = Employee(profile, job, salary)
		return e

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
