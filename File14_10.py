class Employee:
    def __init__(self, name, department, salary):
        self.name = name            
        self._department = department  
        self.__salary = salary     

    def display_info(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Salary:", self.__salary)  

    def get_salary(self):
        return self.__salary 

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Invalid salary.")

def main():
    emp = Employee("Riya", "IT", 60000)

    print("Public:", emp.name)           
    print("Protected:", emp._department) 


    print("Private (via getter):", emp.get_salary())  

    emp.set_salary(65000)
    emp.display_info()

if __name__=="_main_":
    main()