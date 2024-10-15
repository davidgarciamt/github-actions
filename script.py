def greet(name):print('Hello, '+name)
greet('world')
numbers=[1, 2,3]
for num in numbers: print(num)
def calculate_area(radius): return 3.14*radius*radius
area=calculate_area(5); print('Area:', area)
if area > 50: print('Large area') 
else: print('Small area')
class Person: 
    def __init__(self, name, age): self.name=name; self.age=age
john = Person('John', 30); print(john.name, john.age)