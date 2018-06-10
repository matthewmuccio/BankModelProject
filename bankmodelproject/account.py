class Account:
	def __init__(self, acc_number, acc_type, balance, currency, pin_num):
		self.acc_number = acc_number
		self.acc_type = acc_type
		self.balance = balance
		self.currency = currency
		self.pin_num = pin_num

	def __str__(self):
		return "Account number: {}, account type: {}, balance: {}, currency: {}, pin number: {}".format(self.acc_number, self.acc_type, self.balance, self.currency, self.pin_num)
