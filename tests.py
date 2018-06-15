#!/usr/bin/env python3


from bankmodelproject import Account, Bank, Customer, Employee, Profile


if __name__ == "__main__":
	account = Account("123456789", "checking", 100, "1234")
	bank = Bank("Matt's Bank")
	bank.create_profile("Matthew", "Muccio", "male", 20, "matthewmuccio", "password")
	bank.create_profile("Patrick", "Star", "male", 18, "pstar123", "123123")
	bank.create_customer("matthewmuccio", account)
	bank.create_employee("pstar123", "Teller", 15)

	print("Account object:")
	print(account)

	print("\nBank object:")
	print(bank)

	print(bank.has_profile("matthewmuccio")) # True
	print(bank.has_profile("pstar123")) # True
	print(bank.has_customer("matthewmuccio")) # True
	print(bank.has_employee("pstar123")) # True
	print(bank.has_profile("notreal")) # False
	print(bank.has_customer("alsonotreal")) # False
	print(bank.has_employee("unittest")) # False

	bank.get_profile("matthewmuccio") # Should print all info about profile.
	bank.get_customer("matthewmuccio") # Should print all info about customer.
	bank.get_employee("pstar123") # Should print all info about employee.

	bank.get_profile("notaprofile") # Should print an error message.
	bank.get_customer("notacustomer") # Should print an error message.
	bank.get_employee("notanemployee") # Should print an error message.

	bank.create_customer("jack", account) # Should not create customer and print error message.
	bank.create_employee("john", "Teller", 20) # Should not create employee and print error message.

	print(bank.log_in("matthewmuccio", "password")) # True
	print(bank.log_in("pstar123", "123123")) # True
	print(bank.log_in("notaprofile", "false")) # False
	print(bank.log_in("fake", "no")) # False
