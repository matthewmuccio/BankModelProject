class Account:
	def __init__(self, acc_number, acc_type, balance, currency, pin_number):
		self.acc_number = acc_number
		self.acc_type = acc_type
		self.balance = balance
		self.currency = currency
		self.pin_number = pin_number

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

	def __str__(self):
		first = "[ ACCOUNT ]".center(30, "-")
		second = "Account number: {}".format(self.acc_number).center(30, " ")
		third = "Account type: {}".format(self.acc_type).center(30, " ")
		fourth = "Balance: {}".format(self.balance).center(30, " ")
		fifth = "Currency: {}".format(self.currency).center(30, " ")
		sixth = "Pin number: {}".format(self.pin_number).center(30, " ")
		last = "-".center(30, "-")
		return "\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(first, second, third, fourth, fifth, sixth, last)
