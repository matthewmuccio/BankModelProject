import sqlite3
import hashlib
import random

from bankmodelproject.account import Account
from bankmodelproject.customer import Customer
from bankmodelproject.employee import Employee
from bankmodelproject.profile import Profile


class Bank:
	def __init__(self, name):
		self.name = name
		self.balance = 0
		self.num_profiles = 0
		self.num_customers = 0
		self.num_employees = 0

	# Encrypt a plaintext string (password) with SHA-512 cryptographic hash function.
	def encrypt_password(self, password):
		return hashlib.sha512(str.encode(password)).hexdigest()

	# Generates a random 10-digit string for the user's account number.
	def generate_acc_number(self):
		return "".join([str(random.randint(0,9)) for _ in range(10)])

	# Checks if there exists a row in the profiles database table with the specifed username and password.
	def log_in(self, username, password):
		password = self.encrypt_password(password)
		connection = sqlite3.connect("master.db", check_same_thread=False)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM profiles WHERE username=? AND password=?", (username, password,))
		result = len(cursor.fetchall()) == 1
		cursor.close()
		connection.close()
		return result

	# Creates a Profile, and adds all its data and attributes to the profiles database table.
	def create_profile(self, first_name, last_name, sex, age, username, password):
		self.num_profiles += 1
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

	# Checks if there is a profile in the profiles database table with the specified username.
	def has_profile(self, username):
		connection = sqlite3.connect("master.db", check_same_thread=False)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM profiles WHERE username=?", (username,))
		result = len(cursor.fetchall()) == 1
		cursor.close()
		connection.close()
		return result

	# Gets the Profile object with the specified username from the profiles database table.
	def get_profile(self, username):
		if not self.has_profile(username):
			print("There is no profile with username \"{0}\" in our database.".format(username))
		else:
			connection = sqlite3.connect("master.db", check_same_thread=False)
			cursor = connection.cursor()
			cursor.execute("SELECT * FROM profiles WHERE username=?", (username,))
			row = cursor.fetchall()
			id, first_name, last_name, sex, age, username, password = row[0]
			cursor.close()
			connection.close()
			return Profile(first_name, last_name, sex, age, username, password)

	# Creates a Customer, and adds all its data and attributes to the customers database table.
	def create_customer(self, username, account):
		if not self.has_profile(username):
			print("There is no profile with username \"{0}\" in our database.".format(username))
			print("Please create a profile with us before creating a bank account.")
		else:
			self.num_customers += 1
			connection = sqlite3.connect("master.db", check_same_thread=False)
			cursor = connection.cursor()
			cursor.execute("SELECT * FROM profiles WHERE username=?", (username,))
			row = cursor.fetchall() # List of tuples (rows)
			id, first_name, last_name, sex, age, username, password = row[0]
			cursor.execute(
				"""INSERT INTO customers(first_name, last_name, sex, age, username, password, acc_number, acc_type, balance, pin_number)
				VALUES(?,?,?,?,?,?,?,?,?,?);""", (first_name, last_name, sex, age, username, password, account.acc_number, account.acc_type, account.balance, account.pin_number)
			)
			connection.commit()
			cursor.close()
			connection.close()

	# Checks if there is a customer in the customers database table with the specified username.
	def has_customer(self, username):
		connection = sqlite3.connect("master.db", check_same_thread=False)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM customers WHERE username=?", (username,))
		result = len(cursor.fetchall()) == 1
		cursor.close()
		connection.close()
		return result

	# Gets the Customer object with the specified username from customers database table.
	def get_customer(self, username):
		if not self.has_customer(username):
			print("There is no customer with username \"{0}\" in our database.".format(username))
		else:
			connection = sqlite3.connect("master.db", check_same_thread=False)
			cursor = connection.cursor()
			cursor.execute("SELECT * FROM customers WHERE username=?", (username,))
			row = cursor.fetchall()
			id, first_name, last_name, sex, age, username, password, acc_number, acc_type, balance, pin_number = row[0]
			cursor.close()
			connection.close()
			return Customer(Profile(first_name, last_name, sex, age, username, password), Account(acc_number, acc_type, balance, pin_number))

	# Creates an Employee, and adds all its data and attributes to the employees database table.
	def create_employee(self, username, job, salary):
		if not self.has_profile(username):
			print("There is no profile with username \"{0}\" in our database.".format(username))
			print("Please create a profile with us before applying to be an employee.")
		else:
			self.num_employees += 1
			connection = sqlite3.connect("master.db", check_same_thread=False)
			cursor = connection.cursor()
			cursor.execute("SELECT * FROM profiles WHERE username=?", (username,))
			row = cursor.fetchall() # List of tuples (rows)
			id, first_name, last_name, sex, age, username, password = row[0]
			cursor.execute(
				"""INSERT INTO employees(first_name, last_name, sex, age, username, password, job, salary)
				VALUES(?,?,?,?,?,?,?,?);""", (first_name, last_name, sex, age, username, password, job, salary)
			)
			connection.commit()
			cursor.close()
			connection.close()

	# Checks if there is a employee in the employee database table with the specified username.
	def has_employee(self, username):
		connection = sqlite3.connect("master.db", check_same_thread=False)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM employees WHERE username=?", (username,))
		result = len(cursor.fetchall()) == 1
		cursor.close()
		connection.close()
		return result

	# Gets the Employee object with the specified username from employees database table.
	def get_employee(self, username):
		if not self.has_employee(username):
			print("There is no employee with username \"{0}\" in our database.".format(username))
		else:
			connection = sqlite3.connect("master.db", check_same_thread=False)
			cursor = connection.cursor()
			cursor.execute("SELECT * FROM employees WHERE username=?", (username,))
			row = cursor.fetchall()
			id, first_name, last_name, sex, age, username, password, job, salary = row[0]
			cursor.close()
			connection.close()
			return Employee(Profile(first_name, last_name, sex, age, username, password), job, salary)

	# Creates and returns an Account with the specified attributes.
	def create_account(self, acc_number, acc_type, balance, pin_number):
		a = Account(acc_number, acc_type, balance, pin_number)
		self.balance += balance
		return a

	# Deposits amount into the Bank's balance.
	def deposit(self, username, amount):
		connection = sqlite3.connect("master.db", check_same_thread=False)
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM customers WHERE username=?", (username,))
		row = cursor.fetchall()
		id, first_name, last_name, sex, age, username, password, acc_number, acc_type, balance, pin_number = row[0]
		new_balance = balance + amount
		cursor.execute("UPDATE customers SET balance=? WHERE username=?", (new_balance, username,))
		connection.commit()
		cursor.close()
		connection.close()
		self.balance += amount

	# Withdraws amount into the Bank's balance.
	def withdraw(self, username, user_balance, amount):
		if user_balance - amount >= 0:
			connection = sqlite3.connect("master.db", check_same_thread=False)
			cursor = connection.cursor()
			cursor.execute("SELECT * FROM customers WHERE username=?", (username,))
			row = cursor.fetchall()
			id, first_name, last_name, sex, age, username, password, acc_number, acc_type, balance, pin_number = row[0]
			new_balance = balance - amount
			cursor.execute("UPDATE customers SET balance=? WHERE username=?", (new_balance, username,))
			connection.commit()
			cursor.close()
			connection.close()
			self.balance -= amount
			return True
		else:
			return False

	# Prints the string representation of a Bank.
	def __str__(self):
		title = "[ BANK ]".center(30, "-")
		name = "Name: {0}".format(self.name).center(30, " ")
		balance = "Balance: ${0}".format(self.balance).center(30, " ")
		num_profiles = "Profiles: {0}".format(self.num_profiles).center(30, " ")
		num_customers = "Customers: {0}".format(self.num_customers).center(30, " ")
		num_employees = "Employees: {0}".format(self.num_employees).center(30, " ")
		end = "-".center(30, "-")
		return "\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n".format(title, name, balance, num_profiles, num_customers, num_employees, end)
