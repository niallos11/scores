import gspread
from google.oauth2.service_account import Credentials
import pyfiglet

result = pyfiglet.figlet_format("SCORES")
print(result)
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('scores')


def main_menu():
    print("1. Add Scores")
    print("2. View Scores")
    print("3. Quit")
    selection = int(input("Enter choice:"))
    if selection == 1:
        get_scores_data()
    elif selection == 2:
        view_scores_data()
    elif selection == 3:
        exit()
    else:
        print("Invalid choice. Enter 1-3")
        main_menu()


def get_scores_data():
    """
    Get name and team input from the user.
    """
    name_str = input("What is your name:\n")
    print(f"Your name is {name_str}")

    team_str = input("What team are you on:\n")
    print(f"Your team is {team_str}")


get_scores_data()

try:
    score_str = int(input("Enter a score:\n"))
    print(f"Your score is {score_str}")
except (SyntaxError, ValueError):
    print("You did not enter a score")

def view_scores_data():
    print("this shows the score data")
main_menu()