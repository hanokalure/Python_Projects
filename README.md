#Project Overview
This is a simple command-line based User Authentication System implemented in Python. The system allows users to register with a username, password, email, and phone number, and later log in using their credentials. The program ensures basic validation during registration, such as checking for password confirmation and ensuring the phone number is exactly 10 digits.

#Features
##User Registration:
Users can register by providing a username, password, email, and phone number.
The system checks that the password and confirmation password match.
The phone number must be exactly 10 digits long.

##User Login:
Users can log in with their username and password.
The system verifies the credentials before granting access.

##Prerequisites
Python 3.x should be installed on your machine.

#How to Run
##Clone or Download the Repository:

If you haven't already, clone or download the project files to your local machine.
Run the Script:

Open your terminal or command prompt.
Navigate to the directory where the user_authentication_system.py file is located.

##Register a New User:
Follow the on-screen prompts to register a new user.
You will be asked to provide a username, password, confirm the password, email, and a 10-digit phone number.

##Log In:
After registration, you can log in using the credentials you provided.
Enter your username and password when prompted.

##Output
============== USER REGISTRATION ==============
User name : john_doe
Password : ********
Confirm Password : ********
Email-id : john.doe@example.com
Phone: 1234567890

Registration Successful!

============== USER LOGIN ==============
User name : john_doe
Password : ********

Login Successful!
