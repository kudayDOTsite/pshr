import whois
from bs4 import BeautifulSoup
import requests

class EmailInfo:
    def __init__(self, target_addr, target_name, target_domain, date, decoded_subject, email_body, is_forwarded, attacker_email, attacker_name, attacker_domain):
        self.target_addr = target_addr
        self.target_name = target_name
        self.target_domain = target_domain
        self.date = date
        self.subject = decoded_subject
        self.body = email_body
        self.is_forwarded = is_forwarded
        self.attacker_email = attacker_email
        self.attacker_domain = attacker_domain
        self.attacker_name = attacker_name
        self.sender_domain_info = None
        self.urls_info = []
        self.blacklist_info = []

    def set_sender_domain_info(self, sender_domain_info):
        self.sender_domain_info = sender_domain_info

    def get_sender_domain_info(self):
        return self.sender_domain_info

    def set_urls_info(self, urls_info):
        self.urls_info = urls_info

    def get_urls_info(self):
        return self.urls_info

    def set_blacklist_info(self, blacklist_info):
        self.blacklist_info = blacklist_info

    def get_blacklist_info(self):
        return self.blacklist_info




