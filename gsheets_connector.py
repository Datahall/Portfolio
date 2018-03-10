import gspread
import pandas as pd

class GSheets:
    def change_connection(self, json_file_path, name):
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(json_file_path, scope)
        self.client = gspread.authorize(creds)
        self.sheet = client.open(name).sheet1
    
    def __init__(self, json_file_path, name):
        self.change_connection(json_file_path,name)
    
    def get_all_data(self):
        return pd.DataFrame(self.sheet.get_all_records())