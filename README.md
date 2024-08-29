# **User Authentication System**

## **Description**
This project is a simple user authentication system that allows users to register with a username and password, securely stores these credentials, and permits users to log in. The system includes security features such as limiting the number of login attempts to prevent unauthorized access.

## **Features**
- **User Registration**: Allows users to register by creating a unique username and password. <br>
- **Secure Storage**: Usernames and passwords are stored securely using a dictionary. <br>
- **User Login**: Users can log in by entering their registered credentials. The system checks if the provided credentials match the stored ones. <br>
- **Login Attempt Limit**: The system limits login attempts to 3. After 3 failed attempts, the user is locked out to prevent further attempts. <br>

## **Concepts Involved**
- **Dictionaries**: Used for securely storing usernames and passwords. <br>
- **Functions**: Defined for operations such as registering users, logging them in, and handling lockouts. <br>
- **Loops**: Used to allow users to retry login attempts and handle multiple users. <br>
- **Conditional Statements**: Employed to check login attempts, match credentials, and enforce the lockout mechanism. <br>

## **Usage**
- **Registering a User**: When prompted, users can create a new account by providing a unique username and a secure password. <br>
- **Logging In**: Users can log in by entering their username and password. If the credentials are correct, access is granted; otherwise, the user may retry until they reach the maximum allowed attempts. <br>
- **Lockout Mechanism**: After 3 failed login attempts, the user is locked out and cannot attempt to log in again. <br>

## **Contributing**
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.
