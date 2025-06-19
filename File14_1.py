class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Name:", self.name, ", ID:", self.emp_id, ", Salary:", self.salary)

def main():
    emp1 = Employee("Rohit", 101, 50000)
    emp1.display()

if __name__=="_main_":
    main()