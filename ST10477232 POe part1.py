import re


class Login:
    def __init__(self):
        self.registered_users = {}  # Stores user details in the format: username -> (password, first_name, last_name)

    def check_user_name(self, username):
        """
        Check if the username contains an underscore and is no more than five characters long.
        """
        return bool(re.match(r"^[a-zA-Z0-9_]{1,5}$", username)) and "_" in username

    def check_password_complexity(self, password):
        """
        Check if the password meets complexity rules:
        At least 8 characters long, contains a capital letter, a number, and a special character.
        """
        return bool(re.match(r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password))

    def check_cell_phone_number(self, phone_number):
        """
        Check if the cell phone number contains the international country code and is no more than ten digits long.
        """
        return bool(re.match(r"^\+27\d{9}$", phone_number))

    def register_user(self, username, password, phone_number, first_name, last_name):
        """
        Register a user and return appropriate messages for the conditions (username, password, phone).
        """
        if not self.check_user_name(username):
            return "Username is not correctly formatted, please ensure that your username contains an underscore and is no more than five characters in length."
        if not self.check_password_complexity(password):
            return "Password is not correctly formatted; please ensure that the password contains at least eight characters, a capital letter, a number, and a special character."
        if not self.check_cell_phone_number(phone_number):
            return "Cell phone number is incorrectly formatted or does not contain an international code, please correct the number and try again."
        self.registered_users[username] = (password, first_name, last_name)
        return "User registered successfully."

    def login_user(self, username, password):
        """
        Verify if the login details entered match the stored details.
        """
        return username in self.registered_users and self.registered_users[username][0] == password

    def return_login_status(self, username, password):
        """
        Return appropriate messages for a successful or failed login.
        """
        if self.login_user(username, password):
            first_name, last_name = self.registered_users[username][1], self.registered_users[username][2]
            return f"Welcome {first_name} {last_name}, it is great to see you again."
        return "Username or password incorrect, please try again."