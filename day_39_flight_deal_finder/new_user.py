import gspread
from oauth2client.service_account import ServiceAccountCredentials


class NewUser:
    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                      "https://www"
                      ".googleapis.com/auth"
                      "/drive.file",
                      "https://www.googleapis.com/auth/drive"]

        self.creds = ServiceAccountCredentials.from_json_keyfile_name(
            "/home/huba/code/authenticate/workout-tracker-331503"
            "-92fddb8799cd.json", self.scope)
        self.first_name = None
        self.second_name = None
        self.email = None
        self.emails = None

    def get_user_data(self):
        self.first_name = input("first name: ")
        self.second_name = input("second name: ")
        self.email = input("email: ")

    def insert_new_user(self):
        self.get_user_data()
        client = gspread.authorize(self.creds)
        sheet = client.open("FlightDeals").sheet1
        new_user = [self.first_name, self.second_name, self.email]

        sheet.insert_row(new_user, 2)
        self.emails = sheet.col_values(3)
