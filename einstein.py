# calculate energy using mass and speed of light
def calculate_e(mass):
    c = 300000000
    energy = mass * (c ** 2)
    return energy

# main function
def main():
    mass = int(input("m: "))
    energy = calculate_e(mass)
    print("E:", energy)

# call the main function
main()
