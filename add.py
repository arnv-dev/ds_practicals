import numpy

print("\n Operations: sum, sub, mult, div, square, root, cuberoot")
operation = input("Enter operation name in lower case: ")



if operation in ["square", "root", "cuberoot"]:
    num1 = int(input("Enter number: "))
else:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))


if operation == "sum":
    result = num1 + num2
    print("sum is :", result)
    
elif operation == "sub":
    result = num1 - num2
    print("substraction  is :", result)
    
elif operation == "mult":
    result = num1 * num2
    print("multiplication is :", result)
    
elif operation == "square":
    result = num1 * num1
    print("square is :", result)
    
elif operation == "root":
     result = numpy.sqrt(num1)
     print(result)
     
elif operation == "cuberoot":
     result = numpy.cbrt(num1)
     print(result)
    
elif operation == "div":
    if num2 != 0:
        result = num1 / num2
        print("division  is :", result)
    else:
        print("Error: Cannot divide by zero!")
        
else: 
    print("Invalid operation entered!")

