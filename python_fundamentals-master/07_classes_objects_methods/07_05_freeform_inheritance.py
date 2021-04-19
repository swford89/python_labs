'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''
class BusinessCompany():

    def __init__(self, company_name) -> None:
        self.company_name = company_name

    def __str__(self) -> str:
        return f"{self.company_name} //"

class Employee(BusinessCompany):
    
    def __init__(self, company_name, identification, first_name, last_name) -> None:
        super().__init__(company_name)
        self.identification = identification
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return super().__str__() + f" {self.identification}: {self.first_name} {self.last_name}"

class ComputerProgrammer(Employee):

    def __init__(self, company_name, identification, job_title, first_name, last_name) -> None:
        super().__init__(company_name, identification, first_name, last_name)
        self.job_title = job_title

    def __str__(self) -> str:
        return f"{self.company_name} // {self.identification}: {self.job_title} - {self.first_name} {self.last_name}"

class Customer(BusinessCompany):
    
    def __init__(self, company_name, identification, first_name, last_name) -> None:
        super().__init__(company_name)
        self.identification = identification
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return super().__str__() + f" {self.identification}: {self.first_name} {self.last_name}"

    
some_employee = Employee("Elite Three", "Employee", "Scott", "Ford")
some_customer = Customer("Elite Three", "Customer", "Azhar", "Merali")
some_programmer = ComputerProgrammer("Elite Three", "Employee", "Computer Programmer", "Nahim", "Amlani")
print(some_employee)
print(some_customer)
print(some_programmer)