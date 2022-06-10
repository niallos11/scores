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


def main():
    """
    Main menu with options to select add & view functions.
    """
    print("1. Add Scores")
    print("2. View Scores")
    print("3. Quit")
    selection = input("Enter choice:")
    if selection == "1":
        update()
    elif selection == "2":
        view_scores_data()
    elif selection == "3":
        print("Goodbye")
        exit()
    else:
        print("Invalid choice. Enter 1-3")
    main()


def view_scores_data():
    """
    Function To view scores added to worksheet.
    """
    scores = SHEET.worksheet('scores')
    data = scores.get_all_values()
    print(data)


def get_scores_data():
    """
    Get scores figures input from the user.
    Run a while loop to collect a valid string of data.
    """
    while True:

        data_str = input("Enter your score here:\n")

        scores_data = data_str.split(",")

        if validate_data(scores_data):
            print("Data is valid!")
            break

    return scores_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int.
    """
    try:
        [int(value) for value in values]
        if len(values) != 1:
            raise ValueError(
                f"Exactly 1 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet.
    Update the relevant worksheet with the data provided.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def update():
    """
    Run all program functions.
    """
    data = get_scores_data()
    scores_data = [int(num) for num in data]
    update_worksheet(scores_data, "scores")


main()
