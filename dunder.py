
# # def add(a, b):
# #     print(a + b)
# #     print("abc")
# # add(2, 3)



# class Employee:

#     def __init__(self, empid, ename, eage, esalary, eaddr):  
#         self.eid = empid #instance variable
#         self.empname = ename
#         self.empage = eage
#         self.empsalary = esalary
#         self.empaddr = eaddr
#         # print("I am inside init method, I run automatically, without calling me")

#     # def __str__(self) -> str:  
#     #     return f"{self.__dict__}"
        

#     def __repr__(self) -> str:
#         return f"{self.__dict__}"

#     def get_detail(self):
#         print(f'''Employee Id - {self.eid}
#     Name of Employee - {self.empname}
#     Age of Employee - {self.empage}
#     Salary of Employee - {self.empsalary}
#     Address of Employee - {self.empaddr}
#         ''')

#     @staticmethod
#     def get_details(ls1): #ls1 = [e1, e2, e3]
#         for emp in ls1: #__repr__
#             print(f'''Employee Id - {emp.eid} #__str__
#     Name of Employee - {emp.empname}
#     Age of Employee - {emp.empage}
#     Salary of Employee - {emp.empsalary}
#     Address of Employee - {emp.empaddr}
#         ''')
   
            


# e1 = Employee(101, "ABC", 31, 40000, "Pune")
# e2 = Employee(102, "XYZ", 43, 30333, "Satara")
# e3 = Employee(103, "POP", 11, 63110, "Nashik")
# e4 = Employee(104, "FGH", 27, 30100, "Nashik")

# # e1.get_detail()

# # e1

# print(e1)

# # emp = [e1, e2, e3, [e4]]



# # print(emp) 

# # Employee.get_details(emp)

# # print(e1)
# # print(e2)


