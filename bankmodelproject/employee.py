from bankmodelproject.person import Person


class Employee(Person):
	def __init__(self, name, gender, age, job, salary):
		super().__init__(name, gender, age)
		self.job = job
		self.salary = salary

	def __str__(self):
		return "Name: {}, gender: {}, age: {}, job: {}, salary: {}".format(self.name, self.gender, self.age, self.job, self.salary)
