import re
from collections import Counter
import whoisDetection as whois

class DomainCounter:
    def __init__(self):
        self.http_domains = []
        self.https_domains = []

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

    def check_domain_creation_years(self, domains):
        for domain in domains:
            print(f"Domain: {domain}")
            wh = whois.DomainInfo(domain)
            print("1 sene önce mi alınmış: ", wh.is_created_within_years(1))
            print("2 sene önce mi alınmış: ", wh.is_created_within_years(2))
            print("3 sene önce mi alınmış: ", wh.is_created_within_years(3))
            print("4 sene önce mi alınmış: ", wh.is_created_within_years(4))
            print("5 sene önce mi alınmış: ", wh.is_created_within_years(5))
            print("\n")

if __name__ == "__main__":
    text = "Bu bir örnek metin. https://berenkudaygorun.com, https://www.openai.com, ve http://www.example.com/urunler hakkında bilgi içerir."

    counter = DomainCounter()
    counter.text = text  # Metni ayarla

    counter.find_http_domains()
    counter.find_https_domains()

    counter.check_domain_creation_years(counter.http_domains)
    counter.check_domain_creation_years(counter.https_domains)
