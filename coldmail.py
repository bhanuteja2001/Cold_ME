import smtplib
import os
from jsonify import RecruiterDataProcessor
import json


#coldmail(person['Name'], person['Email'], person['Company'], person['Type'])
# recruiter_emails is a list of objects with structure {"name":<recruiter_name>, "email":<recruiter_email>, "company":<company_name>}
class coldmail:
    def __init__(self, Name, Email, Company, Type):
        if (Type == 'DE_Manager'):
            # compose email for DE Manager
            with open('manager_DE.txt', 'r') as file:
                content = file.read()

            content = content.format(person['Name'], person['Company'])

            subject = "My interest in a SWE internship at {}".format(company_name)
        elif (Type == 'DS_Manager'):
            # compose email for DE Manager
            with open('manager_DS.txt', 'r') as file:
                content = file.read()

            content = content.format(person['Name'], person['Company'])

            subject = "My interest in a SWE internship at {}".format(company_name)
        elif (Type == 'Recruiter'):
            # compose email for DE Manager
            with open('Recruiter.txt', 'r') as file:
                content = file.read()

            content = content.format(person['Name'], person['Company'])

            subject = "My interest in a SWE internship at {}".format(company_name)
        
        
        # establish connection to outlook email
        self.FROM = os.environ["gmail_email"]
        self.TO = [email_address]

        # Prepare message wrapper
        self.full_mail = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

        %s
        """ % (self.FROM, ", ".join(self.TO), subject, message)

        self.send_mail()

    def send_mail(self):
        # Send the mail
        server.sendmail(self.FROM, self.TO, self.full_mail)

if __name__ == "__main__":
    # run the script
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(os.environ["gmail_email"], os.environ["gmail_password"])


    processor = RecruiterDataProcessor()
    people = json.loads(processor.get_json_data())


    # for person in people:
    #     print('Name: ', person['Name'])
    #     print('Email: ', person['Email'])
    #     print('Company: ', person['Company'])
    #     print('Status: ', person['Status'])
    #     print('Type: ', person['Type'])


    # go thru each recruiter, taking the name, company and email
    for person in people:
        coldmail(person['Name'], person['Email'], person['Company'], person['Type'])

    server.quit()

