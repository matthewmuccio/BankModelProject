#!/usr/bin/env python3


import sqlite3


# Create a connection to the database.
connection = sqlite3.connect("master.db", check_same_thread=False)

# Create a cursor object to represent the "gaze" of the RDBMS.
cursor = connection.cursor()

# Create a table to store profile data.
cursor.execute(
	"""CREATE TABLE profiles(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		first_name VARCHAR(50),
		last_name VARCHAR(50),
		sex VARCHAR(10),
		age INTEGER NOT NULL,
		username VARCHAR(25),
		password VARCHAR(128)
	);"""
)

# Create a table to store customer data.
cursor.execute(
	"""CREATE TABLE customers(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		first_name VARCHAR(50),
		last_name VARCHAR(50),
		sex VARCHAR(10),
		age INTEGER NOT NULL,
		username VARCHAR(25),
		password VARCHAR(128),
		acc_number VARCHAR(10),
		acc_type VARCHAR(10),
		balance INTEGER NOT NULL,
		pin_number VARCHAR(4)
	);"""
)

# Create a table to store employee data.
cursor.execute(
	"""CREATE TABLE employees(
		pk INTEGER PRIMARY KEY AUTOINCREMENT,
		first_name VARCHAR(50),
		last_name VARCHAR(50),
		sex VARCHAR(10),
		age INTEGER NOT NULL,
		username VARCHAR(25),
		password VARCHAR(128),
		job VARCHAR(50),
		salary FLOAT NOT NULL
	);"""
)

# Close cursor and connection to database.
cursor.close()
connection.close()
