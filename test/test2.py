import pandas as pd
import email
import quopri
import sys
sys.path.append('../')
sys.path.append('../app/engine/')
from email.parser import Parser
import app.engine.email_info as ei
import app.engine.detect.whoisDetection as whois
import app.engine.detect.linkDetection as linkDetection
import app.engine.detect.black_list_detection as blackListDetection
import app.engine.email_analysis as ea
import configparser

config = configparser.ConfigParser()
config.read('../.env')
OPENAI_KEY = config.get('OPENAI', 'OPENAI_KEY')

# CSV dosyasını okuyan fonksiyon
def read_csv(file_path):
    return pd.read_csv(file_path)

# E-posta verilerini parse eden fonksiyon
def parse_email(row):
    email_data = {
        'sender': row['sender'],
        'receiver': row['receiver'],
        'date': row['date'],
        'urls': row['urls'],
        'subject': row['subject'],
        'body': row['body']
    }
    return email_data

# Ana fonksiyon
def main(csv_file_path):
    df = read_csv(csv_file_path)
    parsed_emails = []

    for index, row in df.iterrows():
        email_info = parse_email(row)
        # Burada email_info'yu projenizin analiz kısmına gönderebilirsiniz
        # Örneğin: analyze_email(email_info)
        parsed_emails.append(email_info)

    # İşlenmiş e-postaları döndür
    return parsed_emails


   
        
if __name__ == '__main__':
    csv_file_path = 'datas/Nigerian_Fraud.csv'  # CSV dosyasının yolu
    emails = main(csv_file_path)
    print(len(emails))
    


