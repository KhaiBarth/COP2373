#In this assignment, we are simulating an email filtration system that detects key words commonly used in Spam emails. This program scans the user's message for these words and leaves a counter, likeliness of a scam, and the words used.



#Formulate spam phrases and spam score
def load_spam_phrases(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def calculate_spam_score(message, spam_phrases):
    spam_score = 0
    matched_phrases = []

    for phrase in spam_phrases:
        if phrase.lower() in message.lower():
            spam_score += 1
            matched_phrases.append(phrase)

    return spam_score, matched_phrases

#Enter text for result scoring after nmessage is written
def rate_spam_likelihood(score, total_phrases):
    if score == 0:
        return "No Spam Detected"
    elif score < total_phrases * 0.5:
        return "Low chance of spam"
    elif score < total_phrases * 0.75:
        return "Moderate chance of spam"
    else:
        return "High likelihood of spam"

#Create email layout text and dialog box for user to enter email message
def main():
    spam_phrases_file = 'spam.txt'
    spam_phrases = load_spam_phrases(spam_phrases_file)

    print("Enter the email below (type 'SEND'):")
    email_message = ''
    while True:
        line = input()
        if line.strip().upper() == 'SEND':
            break
        email_message += line + '\n'

    spam_score, matched_phrases = calculate_spam_score(email_message, spam_phrases)
    likelihood = rate_spam_likelihood(spam_score, len(spam_phrases))
#Display the final score for the user 
    print("\nSpam Score:", spam_score)
    print("Likelihood of Spam:", likelihood)
    if matched_phrases:
        print("Detected words/phrases:")
        for phrase in matched_phrases:
            print(f" - {phrase}")


if __name__ == '__main__':
    main()
