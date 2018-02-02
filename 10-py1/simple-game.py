import random

def get_guess():
    return list(input(f"What is your guess?"))

# Generate 3 digit code
def code_generator():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return(digits[:3])

# Generate the clues
def generate_clues(code, user_guess):

    if user_guess==code:
        return "CODE CRACKED!"

    clues = []

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues

print("Welcome code breakers!")

secret_code = code_generator()

clue_report = []

while clue_report != "CODE CRACKED!":
    guess = get_guess()

    clue_report = generate_clues(guess, secret_code)
    print("here is the result of your guess:")
    for clue in clue_report:
        print(clue)


clues = ["Close: You've guessed a correct number but in the wrong position",
"Match: You've guessed a correct number in the correct position",
"Nope: You haven't guess any of the numbers correctly"]
