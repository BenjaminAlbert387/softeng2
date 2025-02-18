class Student:
  def __init__(self, name, identifier, module_1, module_2, module_3, module_4):
    self.name = name
    self.identifier = identifier
    self.module_1 = module_1
    self.module_2 = module_2
    self.module_3 = module_3
    self.module_4 = module_4

p1 = Student("Adam", 1001, 55, 67, 58, 77)

print(p1.module_4)

f = open("demofile.txt", "r")
print(f.read())