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
        self.sender_domain_info = []
        self.http_urls_info = []
        self.https_urls_info = []
        self.http_blacklist_info = []
        self.https_blacklist_info = []

    def set_sender_domain_info(self, sender_domain_info):
        self.sender_domain_info = sender_domain_info

    def get_sender_domain_info(self):
        return self.sender_domain_info

    def set_http_urls_info(self, http_urls_info):
        self.http_urls_info = http_urls_info

    def set_https_urls_info(self, https_urls_info):
        self.https_urls_info = https_urls_info

    def get_http_urls_info(self):
        return self.http_urls_info
    
    def get_https_urls_info(self):
        return self.https_urls_info

    def set_http_blacklist_info(self, http_blacklist_info):
        self.http_blacklist_info = http_blacklist_info

    def get_http_blacklist_info(self):
        return self.http_blacklist_info
    
    def set_https_blacklist_info(self, https_blacklist_info):
        self.https_blacklist_info = https_blacklist_info

    def get_https_blacklist_info(self):
        return self.https_blacklist_info




