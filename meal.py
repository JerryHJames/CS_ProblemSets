def main():
    # ask the user for the time
    time = input("What time is it? ")
    hours = convert(time)

    # check the time and preint the meal
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

# define a conversion function for the time
def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60

if __name__ == "__main__":
    main()
