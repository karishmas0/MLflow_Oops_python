# intitiate a class
class employee:
    # special methord/magic method/dunder method- constructor
    def __init__(self):
        # print(id(self))
        # print("started executing attributes/data")
        self.id= 123
        self.salary= 50000
        self.designation="SDE"
        # print("attributes/data have been initiated")

    def travel(self,destination):
        print("this travel func was called manually")
        print(f"Employee is now travelling to {destination}")

# #create an object/instance of the class
sam= employee()
sam.name ="sam Kumar"
print(sam.name)
# print(id(sam))

# shaktiman = employee()
# print(id(shaktiman))
# print(sam.id)
# print(sam.salary)
# print(sam.designation)

# #calling a method
# #function ko hamesha call karna pdta hai means method ko
sam.travel("kerala")

# print(type(sam))
