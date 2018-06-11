from bankmodelproject.person import Person
from bankmodelproject.customer import Customer
from bankmodelproject.employee import Employee
from bankmodelproject.account import Account


class Bank:
	def __init__(self, name, balance, profiles, customers, employees):
		self.name = name
		self.balance = balance
		self.profiles = profiles
		self.customers = customers
		self.employees = employees
		self.users = {}

	#create_person
	def create_profile(self, first_name, last_name, sex, age, id, password):
		p = Person(first_name, last_name, sex, age, id, password)
		self.profiles.append(p)
		self.users[id] = password

	def create_account(self, acc_number, acc_type, balance, currency, pin_number):
		return Account(acc_number, acc_type, balance, currency, pin_number)

	def create_customer(self, person, account):
		c = Customer(person, account)
		self.customers.append(c)

	def create_employee(self, person, job, salary):
		e = Employee(person, job, salary)
		self.employees.append(e)

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

	def __str__(self):
		first = "[ BANK ]".center(30, "-")
		second = "Name: {}".format(self.name).center(30, " ")
		third = "Balance: ${}".format(self.balance).center(30, " ")
		fourth = "Profiles: {}".format(len(self.profiles)).center(30, " ")
		fifth = "Customers: {}".format(len(self.customers)).center(30, " ")
		sixth = "Employees: {}".format(len(self.employees)).center(30, " ")
		last = "-".center(30, "-")
		return "\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(first, second, third, fourth, fifth, sixth, last)
