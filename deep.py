# get user input
question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# if the answer is 42, forthy-two, or forty two, answer is correct
def correct_answer(answer):
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        return True
    else:
        return False

# if the answer is correct, print "Yes"
def main():
    if correct_answer(question):
        print("Yes")
    else:
        print("No")

main()
