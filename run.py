import configparser
import app.engine.email_info_parser as eip
import os
import ast

# Dosyayı oku ve verileri ayrıştır
config = configparser.ConfigParser()
config.read('.env')

# E-posta bilgilerini al
IMAP_SERVER = config.get('Mail Information', 'IMAP_SERVER')
IMAP_USER = config.get('Mail Information', 'IMAP_USER')
IMAP_PASSWORD = config.get('Mail Information', 'IMAP_PASSWORD')
SPECIFIC_SENDERS = ast.literal_eval(config.get('Mail Information', 'SPECIFIC_SENDERS'))

def main():
    eip.IMAP_SERVER = IMAP_SERVER
    eip.IMAP_USER = IMAP_USER
    eip.IMAP_PASSWORD = IMAP_PASSWORD
    eip.SPECIFIC_SENDERS = SPECIFIC_SENDERS
    eip.main()


main()