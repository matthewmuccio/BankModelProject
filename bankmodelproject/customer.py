import sqlite3

from bankmodelproject.profile import Profile


class Customer(Profile):
	def __init__(self, profile, account):
		super().__init__(profile.first_name, profile.last_name, profile.sex, profile.age, profile.username, profile.password)
		self.account = account

	# Deposits amount into the customer's account balance, and updates database table accordingly.
	def deposit(self, amount):
		self.account.deposit(amount)
		connection = sqlite3.connect("master.db", check_same_thread=False)
		cursor = connection.cursor()
		cursor.execute("UPDATE customers SET balance=? WHERE username=?", (self.account.balance, self.username,))
		cursor.close()
		connection.close()

	def __str__(self):
		title = "[ CUSTOMER ]".center(30, "-")
		first_name = "First name: {0}".format(self.first_name).center(30, " ")
		last_name = "Last name: {0}".format(self.last_name).center(30, " ")
		sex = "Sex: {0}".format(self.sex).center(30, " ")
		age = "Age: {0}".format(self.age).center(30, " ")
		username = "Username: {0}".format(self.username).center(30, " ")
		password = "Password: N/A".center(30, " ")
		account = "Account: \n{0}".format(self.account).center(30, " ")
		end = "-".center(30, "-")
		return "\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n".format(title, first_name, last_name, sex, age, username, password, account, end)
