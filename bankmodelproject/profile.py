class Profile:
	def __init__(self, first_name, last_name, sex, age, username, password):
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
		self.age = age
		self.username = username
		self.password = password

	def __str__(self):
		title = "[ PROFILE ]".center(30, "-")
		first_name = "First name: {0}".format(self.first_name).center(30, " ")
		last_name = "Last name: {0}".format(self.last_name).center(30, " ")
		sex = "Sex: {0}".format(self.sex).center(30, " ")
		age = "Age: {0}".format(self.age).center(30, " ")
		username = "Username: {0}".format(self.username).center(30, " ")
		password = "Password: N/A".center(30, " ")
		end = "-".center(30, "-")
		return "\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n".format(title, first_name, last_name, sex, age, username, password, end)
