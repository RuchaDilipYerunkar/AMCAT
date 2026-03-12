phy = int(input("enter the marks of phys :"))
math = int(input("enter the marks of math :"))
chem = int(input("enter the marks of chem :"))
  
total = phy+chem+math
percentage = total / 3.0
print("total=",total)
print("percentage=", percentage)


if percentage >= 60:
    print("you are eligible for placement")
else:
    print("you are not eleigible")
