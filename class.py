class Student:
    def __init__(self, name, age, student_no, course):
        self.name = name
        self.age = age
        self.student_no = student_no
        self.course = course

#object 1
student1 = Student("Jack",19,"100101","Finance")
print(type(student1))
print(student1)
print(student1.name)
print(student1.age)
print(student1.student_no)
print(student1.course)


#object 2
student2 = Student("Mary",21,"100102","Data Science")
print(type(student2))
print(student2.name)
print(student2.age)
print(student2.student_no)
print(student2.course)