# lst=[1,2,3]
# my_str="mlops playlist"
# my_int=155

# print(type(lst))
# lst.clear()
# print(lst)

# lst.capitalize()
# #my_str=my_str.capitalize
# print(lst)

# a='x'
# b='y'
# print(a+b)# output xy

from oops_proj import chatbook
# user1=chatbook()

#function vs method below
lst=[1,2,3]
#function
a1=len(lst)
print(a1)

user1=chatbook()
print([m for m in dir(user1) if not m.startswith("_")])
user1.