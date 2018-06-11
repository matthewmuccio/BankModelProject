# BankModelProject

Byte Academy Weekend #2 project

TODO
----
Refactor code structure of the interactive prompt to make it more organized and streamlined.
Add SQL database with SQLite back-end to store, manage, and manipulate user data.
Implement password encryption/hashing using SHA512 so as to not store PII in plaintext.

Instructions
------------
Week 2 weekend assignment - Classes, Objects, & Modules

Think about a bank branch. Think about the customers, the kinds of accounts they have, how they can interact with their accounts and the branch, and so on.

Your assignment is to model this with classes and objects. This is an open-ended design problem. You decide what is important to include and how toimplement it.

The project should be structured with a file called run.py in the root directory and your classes and other modules in one or more directories that
define a module.

run.py should at the least give examples of how your code works. Have it show off the features you have designed.

You might want to take it a step futher and have an interactive prompt with input statements.
A hint on how to do this:

exit = False
while exit is not True:
    # display the options and information you want to display
    # collect the user input
    # set exit equal to True if the user requests to exit
    # otherwise perform actions based on the user input

This is optional though. Some other possible things you could do:

Withdrawals and deposits with different denominations of currency.
International currency conversions.
Password or PIN protect user accounts.
Save the status of accounts to disk with csv, json, or SQL
Loans
Different roles for people. A person could be a customer or work as a teller
Keep track of time in a meaningful way
Analyze someone's account history and produce graphs using matplotlib
(hint: .savefig can output a chart to an image file rather than directly display it in a notebook)

Obviously I don't expect you to do all of this in one weekend. You will be working on a similar project modeling a stock trading application in the coming weeks and I want you to start thinking in terms of larger application design. Just pick some features that interest you and work on implementing
them.

Try to think of your program design in terms of nouns and verbs. An object
is a noun and a class is the definition of that noun. A function or method is
a verb. It is best if a function either produces side effects (actions such
as print statements) or returns a value, but not both. Keep each function 
simple, make it just do one thing that is easy to describe. Break complicated 
tasks into simple parts.

I look forward to seeing what you can do!
