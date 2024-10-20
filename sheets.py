import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = 'client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

class RecruiterDataFetch:
    @staticmethod
    def recruiter_all_records():
        # Fetch the sheet
        sheet = client.open('RecruiterEmailList').sheet1
        python_sheet = sheet.get_values('A:F')
        
        # Filter records where the Status (E column) is not equal to "Updated"
        filtered_records = [row for row in python_sheet if row[4] != "Email Sent"]

        pp = pprint.PrettyPrinter()
        # pp.pprint(filtered_records)  # Uncomment for debugging
        
        return filtered_records
    
    @staticmethod
    def update_status(people):
        sheet = client.open('RecruiterEmailList').sheet1

        for person in people:
            if person and 'ID' in person:  # Check if 'ID' exists in the person dictionary
                id_to_update = person['ID']  # Assuming ID is stored in 'ID'
                status = "Updated"  # New status to set
                cell = sheet.find(str(id_to_update))  # Find the cell with the ID
                if cell:
                    sheet.update_cell(cell.row, 5, status)  # E column is the 5th column




    