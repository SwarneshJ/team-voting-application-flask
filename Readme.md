**Team voting application**

This is a flask web application replica of the team-voting-application-springboot created by me.

https://team-voting-application.herokuapp.com/

Steps to run the application:

Prerequisite - Python 3.7 installed on system

1. Use requirements.txt file to create a virtual environment with the required libraries
2. In the terminal, use "python application.py" command to start this flask application
3. Server will start in debug mode at 127.0.0.1:5000

This application uses SQLite database to keep a track of the email
addresses which have already been used to vote

**Further improvements to be done:**

Verify email addresses using OTP before allowing the user to vote for a team member
