#else if ladder

per = int(input("enter your percentage"))

if  per>=90:
    print("grade a")
elif per>=80 and per<=90:
    print("grade b")
elif per>= 60 and per <80:
    print("grade c")
else:
    print("fail")