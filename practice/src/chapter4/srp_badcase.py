class Employee:
    """Bad case when we didn`t adhere the SRP in making the class"""
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def calculate_salary(self):
        # ... logic for calculating salary ...
        pass

    def generate_report(self):
        # ... logic for generating report ...
        pass

    def send_email(self):
        # ... logic for sending email ...
        pass

    def update_database(self):
        # ... logic for updating database ...
        pass



### monolithic class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        # ... code for login functionality ...
        pass
    def logout(self):
        # ... code for logout functionality ...
        pass
    def change_password(self, new_password):
        # ... code for changing password functionality ...
        pass
    def send_email(self, recipient, subject, message):
        # ... code for sending email functionality ...
        pass
    def upload_file(self, file):
        # ... code for uploading file functionality ...
        pass
    def download_file(self, file):
        # ... code for downloading file functionality ...
        pass
    # ... many other unrelated methods ...