# defines conversion of text to emoji
def convert(text):
    return text.replace(':)', '🙂').replace(':(', '🙁')

# take user input
user_input = input()

# store the result
result = convert(user_input)

# print the result
print(result)
