# In this assignment, I am programming a Magic 8 Ball to give yes or no answers based on the user's typed question.
import random

# Integrate the 8ball responses txt file to the program
def load_responses(file_path):

    try:
        with open(file_path, 'r') as file:
            responses = [line.strip() for line in file]
        return responses
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []


def main():
    responses = load_responses('8ball_responses.txt')

    if not responses:
        print("No response. The 8 Ball is now quitting.")
        return

    # Have the program direct the user to ask a yes/ no question, and respond with a random answer from the list.
    print("Ask a yes or no question. Type 'quit' to end the program.")

# The user enters a question, or enters quit to end the program, and is met with an end message. 
    while True:
        question = input("Ask your question: ")
        if question.lower() == 'quit':
            print("See you later.")
            break

        response = random.choice(responses)
        print(response)


if __name__ == "__main__":
    main()
