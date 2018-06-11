from bankmodelproject.person import Person


class Employee(Person):
	def __init__(self, person, job, salary):
		super().__init__(person.first_name, person.last_name, person.sex, person.age, person.id, person.password)
		self.job = job
		self.salary = salary

	def __str__(self):
		first = "[ EMPLOYEE ]".center(30, "-")
		second = "First name: {}".format(self.first_name).center(30, " ")
		third = "Last name: {}".format(self.last_name).center(30, " ")
		fourth = "Sex: {}".format(self.sex).center(30, " ")
		fifth = "Age: {}".format(self.age).center(30, " ")
		sixth = "Username: {}".format(self.id).center(30, " ")
		seventh = "Job: {}".format(self.job).center(30, " ")
		eighth = "Salary: {}".format(self.salary).center(30, " ")
		last = "-".center(30, "-")
		return "\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(first, second, third, fourth, fifth, sixth, seventh, eighth, last)
