### 1 Question

# What is OOP and why is it important? Write about main principles of OOP.
# Чиро ООП мегуянд ва барои чӣ он лозим аст? Дар бораи принсипҳои асосии он нависед.
# ОПП кори моро осон мекунад ва котро тез ва сон мекунад

### 2 Question

# What are getter and setter and how to use them? Write about properties in python.
# Getter ва setter чист ва чӣ тавр онҳоро истифода мебарем? Дар бораи хусусиятҳо(properties) дар python нависед.

# geter ва setter барои он ба лозим аст ки мо ба ягон атрибут дасраси надорем geter ба мо хамон атрибутро нишон медихад setter
# онро иваз мекунад.properties кори моро элегантли мекунад ва он хамин  корхои getter ва setter ро ичро мекунад

### 3 Question
# Types of variables and methods in a class.
# Кадом намуди атрибутҳо ва методҳо дар клас мавҷуданд. 
# instence vereble 
# instence meted
# class vereble
# class metod

### 5 Question
# Difference between global, local and nonlocal variables.
# Фарқият байни тағйирёбандаҳои global, local and nonlocal.

# global verebles  дар хамачо истивода мебаранд local факат дар дочерни истифода мебаранд nonlocal факат дар худаш истифода мебарем

# task 1
# class kalkulator:
#     def __init__(self):
#         pass
#     def zarbi_a(self,a,b):
#         self.a = a
#         self.b = b
#         print(f"{self.a}x{1}= {self.a * 1}")
#         print(f"{self.a}x{2}= {self.a * 2}")
#         print(f"{self.a}x{3}= {self.a * 3}")
#         print(f"{self.a}x{4}= {self.a * 4}")
#         print(f"{self.a}x{5}= {self.a * 5}")
#         print(f"{self.a}x{6}= {self.a * 6}")
#         print(f"{self.a}x{7}= {self.a * 7}")
#         print(f"{self.a}x{8}= {self.a * 8}")
#         print(f"{self.a}x{9}= {self.a * 9}")
#         print(f"{self.a}x{10}= {self.a * 10}")
#         print()
#         print(f"{self.b}x{1}= {self.b * 1}")
#         print(f"{self.b}x{2}= {self.b * 2}")
#         print(f"{self.b}x{3}= {self.b * 3}")
#         print(f"{self.b}x{4}= {self.b * 4}")
#         print(f"{self.b}x{5}= {self.b * 5}")
#         print(f"{self.b}x{6}= {self.b * 6}")
#         print(f"{self.b}x{7}= {self.b * 7}")
#         print(f"{self.b}x{8}= {self.b * 8}")
#         print(f"{self.b}x{9}= {self.b * 9}")
#         print(f"{self.b}x{10}= {self.b * 10}")
        

# aa = kalkulator()
# aa.zarbi_a(int(input("From = ")),int(input("To = ")))


# task 2

# class Circle:
#     PI = 3.14
    
#     def __init__(self,R):
#         self.R = R
        
        
#     def get_area(self):
#         print(f"area = {2 * self.PI * self.R * self.R }")
#     def get_diametr(self):
#         print(f"diametr = {2 * self.R }")
#     def get_circumference(self):
#         print(f"circumference = {2 * self.PI * self.R}")
#     def get_radius(self):
#         print(f"radius = {self.R}")
    
# a = Circle(int(input()))
# a.get_area()
# a.get_diametr()
# a.get_circumference()
# a.get_radius()

# task 3

# class Kalkulator:
#     def __init__(self):
#         pass
#     def factorial(self,n):
#         self.n = n
#     print(f"{}")
#     def power(self,a,b):
#         self.a = a
#         self.b = b
#         print(self.a ** self.b)
#     def sqrt(self,n):
#         self.n = n
#         print(f"")

# a = Kalkulator()
# a.power(2,2)

# task 4


# class kalkulator:
#     while True:
#         a = int(input("The first number is: "))
#         b = (input("The operation is: "))
#         c = int(input("The second number is: "))

#         if b == "+":
#             print(f"{a} + {c} = {a + c}")
#         if b == "-":
#             print(f"{a} - {c} = {a - c}")
#         if b == "*":
#             print(f"{a} * {c} = {a * c}")
#         if b == "/":
#             print(f"{a} / {c} = {a / c}")
