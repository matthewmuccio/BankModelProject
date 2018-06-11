from bankmodelproject.person import Person


class Customer(Person):
	def __init__(self, person, account):
		super().__init__(person.first_name, person.last_name, person.sex, person.age, person.id, person.password)
		self.account = account

	def __str__(self):
		first = "[ CUSTOMER ]".center(30, "-")
		second = "First name: {}".format(self.first_name).center(30, " ")
		third = "Last name: {}".format(self.last_name).center(30, " ")
		fourth = "Sex: {}".format(self.sex).center(30, " ")
		fifth = "Age: {}".format(self.age).center(30, " ")
		sixth = "Username: {}".format(self.id).center(30, " ")
		seventh = "Account: {}".format(self.account).center(30, " ")
		last = "-".center(30, "-")
		return "\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(first, second, third, fourth, fifth, sixth, seventh, last)
