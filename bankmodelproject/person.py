class Person:
	def __init__(self, first_name, last_name, sex, age, id, password):
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
		self.age = age
		self.id = id
		self.password = password

	def __str__(self):
		first = "[ PROFILE ]".center(30, "-")
		second = "First name: {}".format(self.first_name).center(30, " ")
		third = "Last name: {}".format(self.last_name).center(30, " ")
		fourth = "Sex: {}".format(self.sex).center(30, " ")
		fifth = "Age: {}".format(self.age).center(30, " ")
		sixth = "Username: {}".format(self.id).center(30, " ")
		last = "-".center(30, "-")
		return "\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(first, second, third, fourth, fifth, sixth, last)
