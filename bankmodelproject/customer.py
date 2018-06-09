from bankmodelproject.person import Person


class Customer(Person):
	def __init__(self, name, gender, age, account):
		super().__init__(name, gender, age)
		self.account = account
