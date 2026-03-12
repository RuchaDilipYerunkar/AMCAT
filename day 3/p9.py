ch = ord(input("enter any character"))
if ch>=65 and ch<=91:
    print("you enterd character in upper case")
elif ch>=97 and ch <= 122:
    print("your eneterd character in lower case")
elif ch>=48 and ch<=57:
    print("your entered character is a digit")
else:
    print("special symbol")