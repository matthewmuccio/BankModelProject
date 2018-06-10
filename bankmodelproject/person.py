class Person:
	def __init__(self, name, gender, age):
		self.name = name
		self.gender = gender
		self.age = age

	def __str__(self):
		return "Name: {}, gender: {}, age: {}".format(self.name, self.gender, self.age)
