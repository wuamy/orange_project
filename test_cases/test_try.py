class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print('hi, i am __init__')

  def do_homework(self):
    print('i am a regular function')
    return "ok!"
  
student1 = Student("amy", 34)
student2 = Student('John', 23)
print(student1.name)
print(student1.age)