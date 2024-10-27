import random
import textwrap
from colorama import Fore, Style, init

# Initialize colorama (for Windows support)
init(autoreset=True)

# Define phishing email scenarios
emails = [
    {
        "content": """
        Dear user,
        Your account has been flagged for suspicious activity. Please log in
        immediately to verify your identity by clicking the link below:
        http://suspicious-login.verification-service.com
        Failure to do so will result in account suspension.
        Best regards,
        Customer Support
        """,
        "red_flags": [
            "Suspicious link",
            "Urgent language",
            "Generic greeting"
        ]
    },
    {
        "content": """
        Hello [Your Name],

        Congratulations! You've won a $1000 gift card from Amazon. 
        Please click the link below to claim your reward:
        
        http://amaz0n-rewards.net/claim-now

        Act fast—this offer expires soon!

        Kind regards,
        The Rewards Team
        """,
        "red_flags": [
            "Misspelled domain",
            "Too-good-to-be-true offer",
            "Urgency"
        ]
    }
]

# Intro message
print(Fore.CYAN + "\nWelcome to the Phishing Quiz! Spot the red flags in these suspicious emails.\n")
print(Fore.YELLOW + "Instructions: After reading each email, you’ll need to identify 2 red flags.")
print("- Type your answers carefully (case-sensitive)!\n")

# Score tracking
score = 0

# Game loop
for i in range(len(emails)):
    print(Fore.MAGENTA + f"Email #{i + 1}:\n")
    print(textwrap.fill(emails[i]["content"], width=70))  # Wrap text for readability
    print(Fore.YELLOW + "\nWhat are two red flags in this email? (Enter one by one)\n")

    # Player input
    for j in range(2):  # User needs to find two red flags
        answer = input(Fore.BLUE + f"Red flag #{j + 1}: ").strip()

        if answer in emails[i]["red_flags"]:
            print(Fore.GREEN + "Correct!\n")
            score += 1
        else:
            print(Fore.RED + "Incorrect. Try again!\n")

# Final score
print(Fore.CYAN + f"Quiz Complete! Your final score is: {score}/{2 * len(emails)}\n")

# Feedback based on score
if score == 2 * len(emails):
    print(Fore.GREEN + "Excellent! You're a phishing expert.")
elif score >= len(emails):
    print(Fore.YELLOW + "Not bad! You're getting the hang of it.")
else:
    print(Fore.RED + "Be careful! Phishing scams can be tricky.")
