# Single or basic Inheritance 

# # Base Class
# class parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"hello, my name is {self.name}.") 

# # derived class
# class child(parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# #create an instance of child
# child = child("Alice")
# child.greet() #output: hello, my name is Alive.
# child.play() # output: Alice is playing.


#-------------------------------------------------


# Multilevel Inheritance

# #base class
# class Grandparent:
#     def __init__(self, name):
#         self.name = name

#     def tell_story(self):
#         print(f"{self.name} tells a story.")

# #Intermediate class

# class parent(Grandparent):
#     def work(self):
#         print(f"{self.name} is working.")

# # Derived class
# class child(parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# # create an instance of child
# child= child("Charlie")
# child.tell_story()  #output: Charlie tells a story.
# child.work()     #output: Charlie is working.
# child.play()      # output: Charlie is playing.


#------------------------------------------------

# Hierarchical Inheritance

# Base class
class parent:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print(f"Hello, my name is {self.name}")

# Derived class 1
class child1(parent):
    def play(self):
        print(f"{self.name} is playing.")

#Derived class 2
class child2(parent):
    def study(self):
        print(f"{self.name} is studying.")

#create instance of child1 and child2
Child1=child1("dave")
Child2=child2("eve")

Child1.greet() # Output: Hello, my name is Dave.
Child1.play() # Output: Dave is playing.


Child2.greet()   # Output: Hello, my name is Eve.
Child2.study()  # Output: Eve is studying.

#---------------------------------------
 
# Multiple Inheritance (Diamond problem)

# #common base class
# class A:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         print(f"Hello from A, {self.name}.")

# # Intermediate class 1
# class B(A):

#     def greet(self):
#         print(f"Hello from B, {self.name}.")
#         super().greet()

# # Intermediate class 2
# class C(A):
#     def greet(self):
#         print(f"Hello from C, {self.name}.")
#         super().greet()

# # Derived class
# class D(B, C):

#     def greet(self):
#         print(f"Hello from D, {self.name}.")
#         super().greet()

# # Create an instance of D
# d = D("Frank")
# d.greet()
# # Output:
# # Hello from D, Frank.
# # Hello from B, Frank.
# # Hello from C, Frank.
# #Hello from A, Frank.       




# ------------------------------------------------------------

# Hybrid Inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Intermediate class 1 (Hierarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# Intermediate class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived class (Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)  # Explicitly calling the constructor

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# Create an instance of Bat
bat = Bat("Bruce")
bat.sound()     # Output: Bruce makes a sound.
bat.feed()      # Output: Bruce is feeding milk.
bat.fly()       # Output: Bruce is flying.
bat.nocturnal() # Output: Bruce is nocturnal.

#------------------------------------------------------------