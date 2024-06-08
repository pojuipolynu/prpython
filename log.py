x = 5
y = 10

str1 = "Hello"
str2 = "World"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(True)
else:
    print(False)

expr1 = (x < 10) and (y > 5)  
expr2 = (x > 3) and (y < 8)   

expr3 = (str1 == "Hello") or (str2 != "World")  
expr4 = (str1 != "Hi") or (str2 == "World")     

print("expr3:", expr3)
print("expr4:", expr4)
print("expr1:", expr1)
print("expr2:", expr2)
