MathEquation = str(input("Math Equation: ")).strip()
x, op, y = MathEquation.split()

x = float(x)
y = float(y)

if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    print(x / y)
