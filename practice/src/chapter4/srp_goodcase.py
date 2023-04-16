class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}, Salary: {self.salary}"


class SalaryCalculator:
    def __init__(self, employee):
        self.employee = employee

    def calculate_salary(self):
        # ... logic for calculating salary ...
        # Example calculation logic:
        if self.employee.role == "Manager":
            self.employee.salary += 5000
        elif self.employee.role == "Developer":
            self.employee.salary += 3000
        elif self.employee.role == "Tester":
            self.employee.salary += 2000
        else:
            self.employee.salary += 1000

class ReportGenerator:
    def __init__(self, employee):
        self.employee = employee

    def generate_report(self):
        # ... logic for generating report ...
        pass


class EmailSender:
    def __init__(self, employee):
        self.employee = employee

    def send_email(self):
        # ... logic for sending email ...
        pass


class DatabaseUpdater:
    def __init__(self, employee):
        self.employee = employee

    def update_database(self):
        # ... logic for updating database ...
        pass

if __name__ == "__main__":
    # Create an Employee instance
    employee1 = Employee("John Doe", "Manager", 5000)

    # Create a SalaryCalculator instance for the Employee
    salary_calculator1 = SalaryCalculator(employee1)

    # Calculate the salary using the SalaryCalculator
    salary_calculator1.calculate_salary()

    # Display the updated Employee information
    print(employee1)  # Output: Name: John Doe, Role: Manager, Salary: 10000