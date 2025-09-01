def add(P,Q):
    return P+Q

def substract(P,Q):
    return P-Q

def multiply(P,Q):
    return P*Q

def divide(P,Q):
    return P/Q

def main():
    print("Welcome to Calculator")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))
    print("Please select Proper Operation: ")
    print("a : Add \t s : Substract \t m : Multiply  \t d:Divide")

    choice = input("Enter your Choice - a : s : m : d")


    if choice == 'a':
        print("num1 is added to num2: ",add(num1,num2))
        
    elif choice == 's':
        print("num2 is subtracted from num1",substract(num1,num2))

    elif choice == 'm':
        print("multiply num1 and num2", multiply(num1,num2))

    elif choice == 'd':
        print("Divide num1 by num2",divide(num1,num2))

    else:
        print("Invalid Input")

    
if __name__ == "__main__":
  main()