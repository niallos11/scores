import gspread
from google.oauth2.service_account import Credentials

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
    name_str = input("What is  your name: ")
    print(f"Your name is {name_str}")

    team_str = input("What is  your team you support: ")
    print(f"Your team is {team_str}")


get_scores_data()