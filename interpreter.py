def main():
    # take an input of a math expression
    problem = input("Expression: ")
    x, y, z = problem.split(" ")
    x = int(x)
    z = int(z)

    # check the operator and do the math
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    # print the result
    print(f"{result:.1f}")

main()

