# import pyfiglet module
from google.oauth2.service_account import Credentials
from termcolor import colored
import gspread
import pyfiglet

result = pyfiglet.figlet_format("SCORES") 
print(result)
print(colored("Check your score", 'green'))

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('scores')


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