class Account:
	def __init__(self, acc_number, acc_type, balance, pin_number):
		self.acc_number = acc_number
		self.acc_type = acc_type
		self.balance = balance
		self.pin_number = pin_number

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
			return True
		return False

	def __str__(self):
		title = "[ ACCOUNT ]".center(30, "-")
		acc_number = "Account number: {0}".format(self.acc_number).center(30, " ")
		acc_type = "Account type: {0}".format(self.acc_type).center(30, " ")
		balance = "Balance: ${0}".format(self.balance).center(30, " ")
		pin_number = "Pin number: {0}".format(self.pin_number).center(30, " ")
		end = "-".center(30, "-")
		return "\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n".format(title, acc_number, acc_type, balance, pin_number, end)
