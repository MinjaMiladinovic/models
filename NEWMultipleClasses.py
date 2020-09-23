# first parent class 
class Manager(object):                   
      def __init__(self, name, idnumber): 
            self.name = name 
            self.idnumber = idnumber 
   
# second parent class       
class Employee(object):                 
      def __init__(self, salary, post): 
            self.salary = salary 
            self.post = post 
   
# inheritance from both the parent classes       
class Person(Manager, Employee):         
      def __init__(self, name, idnumber, salary, post, points): 
            self.points = points 
            Manager.__init__(self, name, idnumber) 
            Employee.__init__(self, salary, post)    
            print(self.salary) 
         
ins = Person('Rahul', 882016, 75000, 'Assistant Manager', 560)
