# domain_counter.py

import re

class DomainCounter:
    def __init__(self):
        self.text = ""
        self.http_domains = []
        self.https_domains = []

    def set_text(self, text):
        self.text = text
        self.find_http_domains()
        self.find_https_domains()

    def find_http_domains(self):
        http_pattern = r'http://[a-zA-Z0-9.-]+'
        http_urls = re.findall(http_pattern, self.text)
        http_domains = [re.sub(r'http://', '', url).split('/')[0] for url in http_urls]
        self.http_domains = http_domains

    def find_https_domains(self):
        https_pattern = r'https://[a-zA-Z0-9.-]+'
        https_urls = re.findall(https_pattern, self.text)
        https_domains = [re.sub(r'https://', '', url).split('/')[0] for url in https_urls]
        self.https_domains = https_domains



if __name__ == "__main__":
    # Örnek kullanım
    text = "Bu bir örnek metin. https://berenkudaygorun.com, https://www.openai.com, ve http://www.example.com/urunler hakkında bilgi içerir."

    counter = DomainCounter()
    counter.set_text(text)

    counter.find_http_domains()
    counter.find_https_domains()

