from bankmodelproject.person import Person


class Customer(Person):
	def __init__(self, name, gender, age, account):
		super().__init__(name, gender, age)
		self.account = account

	def __str__(self):
		return "Name: {}, gender: {}, age: {}, account: {}".format(self.name, self.gender, self.age, self.account)
