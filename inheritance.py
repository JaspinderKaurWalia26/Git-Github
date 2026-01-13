class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print("Department:", self.department)
        print("Role: Manager")


class Developer(Employee):
    def __init__(self, name, emp_id, salary, skill):
        super().__init__(name, emp_id, salary)
        self.skill = skill

    def display_info(self):
        super().display_info()
        print("Skill:", self.skill)
        print("Role: Developer")


manager = Manager("Aman", 101, 80000, "IT")
react_dev = Developer("Riya", 102, 60000, "React Developer")
python_dev = Developer("Karan", 103, 65000, "Python Developer")

print("Manager Details:")
manager.display_info()

print("\nReact Developer Details:")
react_dev.display_info()

print("\nPython Developer Details:")
python_dev.display_info()