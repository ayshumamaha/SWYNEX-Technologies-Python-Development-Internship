Task 3 Public User Information System
Project Overview

The Public User Information System is a simple Python application that consumes a public REST API to retrieve and display user information. The application uses the JSONPlaceholder public API. The user enters a User ID between 1 and 10, and the program retrieves information such as name, username, email, phone, website, and company. The project also includes input validation and error handling to make the application reliable and easy to use.

Features
Accepts User ID from the user
Validates the entered User ID
Checks that the User ID is between 1 and 10
Connects to a public REST API
Retrieves user information in JSON format
Displays user details in a readable format
Handles invalid input
Handles API connection errors
Handles unsuccessful API responses
Runs directly in Google Colab
Technologies Used
Python
Requests Library
JSON
JSONPlaceholder REST API
Google Colab
Public API Used

API: JSONPlaceholder

Endpoint used:

https://jsonplaceholder.typicode.com/users/{user_id}

The API provides sample user data in JSON format.

Requirements

Python 3.x and the requests library are required.

The program can be executed directly in Google Colab.

If requests is not available, install it using:

!pip install requests
How to Run
Open Google Colab.
Create a new notebook.
Copy the Python program into a code cell.
Run the cell.
Enter a User ID between 1 and 10.
The program retrieves the information from the public API.
The user information is displayed on the screen.
Example

Input:

Enter User ID (1-10): 1

Output:

=============================================
           USER INFORMATION
=============================================
Name     : Leanne Graham
Username : Bret
Email    : Sincere@april.biz
Phone    : 1-770-736-8031 x56442
Website  : hildegard.org
Company  : Romaguera-Crona
=============================================
Data retrieved successfully.
Input Validation

The application validates the User ID before making the API request.

If the user enters text instead of a number:

Error: Please enter a number from 1 to 10.

If the user enters a number outside the accepted range:

Error: User ID must be between 1 and 10.
Error Handling

The application handles different types of errors, including:

Invalid user input
User ID outside the valid range
API connection failure
User not found
Unexpected errors

This prevents the program from terminating unexpectedly.

Project Structure
Public-User-Information-System/
│
├── app.py
└── README.md
Concepts Demonstrated
Python programming
User input
Conditional statements
Exception handling
REST API consumption
HTTP requests
JSON response processing
Input validation
Data extraction
Future Enhancements
Add a graphical or web-based interface
Allow searching for multiple users
Add more API endpoints
Display address and location information
Save retrieved information to a file
Add search history
Improve the user interface
Project Purpose

The project demonstrates how Python can communicate with a public REST API and process JSON data. It also demonstrates basic validation and error handling required when developing applications that depend on external services.

Author
M. Ayshwarya
