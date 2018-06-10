class Bank:
	def __init__(self, name, balance, customers, employees):
		self.name = name
		self.balance = balance
		self.customers = customers
		self.employees = employees

	def __str__(self):
		return "Name: {}, balance: {}, customers: {}, employees: {}".format(self.name, self.balance, self.customers, self.employees)
