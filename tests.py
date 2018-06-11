#!/usr/bin/env python3


from bankmodelproject import Account, Bank, Customer, Employee, Person


if __name__ == "__main__":
	account = Account("123456789", "checking", 100, "US", "1234")
	bank = Bank("Matt's Bank", 0, [], [], [])
	person = Person("Matthew", "Muccio", "male", 20, "matthewmuccio", "password")
	person2 = Person("Patrick", "Star", "male", 18, "pstar123", "123123")
	customer = Customer(person, account)
	employee = Employee(person, "Owner", 1000)

	print("Account object:")
	print(account)

	print("\nBank object:")
	print(bank)

	print("\nPerson object:")
	print(person)

	print("\nCustomer object:")
	print(customer)

	print("\nEmployee object:")
	print(employee)
