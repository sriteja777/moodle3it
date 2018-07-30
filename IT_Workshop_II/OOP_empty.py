class Employee: pass

john = Employee()
john.name = 'John Doe'
john.dept = 'CS'
john.salary = 1000


print john.__dict__

Employee=type('Employee',(),{})
john = Employee()
john.name = 'John Doe'
john.dept = 'CS'
john.salary = 1000


print john.__dict__
