#!/usr/bin/env python3


from bankmodelproject import Account, Bank, Customer, Employee, Person


if __name__ == "__main__":
	account = Account("123456789", "checking", 100)
	bank = Bank("Matt's Bank", 0, [])
	person = Person("Matthew Muccio", "male", 20)
	customer = Customer("Patrick Star", "male", 18, account)
	employee = Employee(person.name, person.gender, person.age, "Owner", 1000000)

	print("Account object:")
	print("This {} account has an account number {} and a balance of {}.\n".format(account.acc_type, account.acc_number, account.balance))

	print("Bank object:")
	print("{} has a balance of {} and has {} customers.\n".format(bank.name, bank.balance, len(bank.customers)))

	print("Person object:")
	print("{} is a {}-year-old {} person.\n".format(person.name, person.age, person.gender))

	print("Customer object:")
	print("{} is a {}-year-old {} customer and has an account ({}).\n".format(customer.name, customer.age, customer.gender, customer.account))

	print("Employee object:")
	print("{} is a {}-year-old {} employee. They work as an {} and have a salary of {}.\n".format(employee.name, employee.age, employee.gender, employee.job, employee.salary))
