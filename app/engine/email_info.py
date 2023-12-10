import whois
from bs4 import BeautifulSoup
import requests
import detect.whoisDetection as whois

class EmailInfo:
    def __init__(self, target_addr, target_name, target_domain, date, decoded_subject, email_body, is_forwarded, attacker_email, attacker_name, attacker_domain):
        self.target_addr = target_addr #Oltalama saldırısı yapılabilecek olan kişinin adresi
        self.target_name = target_name #Oltalama saldırısı yapılabilecek olan kişinin ismi
        self.target_domain = target_domain #Oltalama saldırısı yapılabilecek olan kişinin mail adresinin domaini
        self.date = date #mailin atıldığı tarih
        self.subject = decoded_subject #mailin konusu
        self.body = email_body #mailin içeriği
        self.is_forwarded = is_forwarded 
        self.attacker_email = attacker_email #potansiyel oltalama saldırısnı yapan kişinin eposta adresi
        self.attacker_domain = attacker_domain #potansiyel oltalama saldırısını yapan kişinin eposta adresinin domain adresi
        self.attacker_name = attacker_name #potansiyel oltalama saldırısını yapan kişinin ismi
        self.sender_domain_info = [] 
        self.http_urls_info = []
        self.https_urls_info = []
        self.http_blacklist_info = []
        self.https_blacklist_info = []
        self.email_content_urls_whois_info = [] 

    def set_sender_domain_info(self, sender_domain_info):
        self.sender_domain_info = sender_domain_info

    """
    Örnek çıktı:
    DomainInfoModel(domain_name='gmail.com', registrar='MarkMonitor, Inc.', whois_server='whois.markmonitor.com', updated_date=datetime.datetime(2023, 7, 11, 10, 10, 13), creation_date=[datetime.datetime(1995, 8, 13, 4, 0), datetime.datetime(1995, 8, 13, 7, 0)], expiration_date=[datetime.datetime(2024, 8, 12, 4, 0), datetime.datetime(2024, 8, 12, 0, 0)], name_servers=['NS1.GOOGLE.COM', 'NS2.GOOGLE.COM', 'NS3.GOOGLE.COM', 'NS4.GOOGLE.COM', 'ns1.google.com', 'ns3.google.com', 'ns2.google.com', 'ns4.google.com'], status=['clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited', 'clientTransferProhibited https://icann.org/epp#clientTransferProhibited', 'clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited', 'serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited', 'serverTransferProhibited https://icann.org/epp#serverTransferProhibited', 'serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited', 'clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)', 'clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)', 'clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)', 'serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)', 'serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)', 'serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)'], emails=['abusecomplaints@markmonitor.com', 'whoisrequest@markmonitor.com'], dnssec='unsigned', org='Google LLC', state='CA', country='US', is_created_within_1_year=False, is_created_within_2_years=False, is_created_within_3_years=False, is_created_within_4_years=False, is_created_within_5_years=False)
    """
    def get_sender_domain_info(self):
        return self.sender_domain_info

    def set_http_urls_info(self, http_urls_info):
        self.http_urls_info = http_urls_info

    def set_https_urls_info(self, https_urls_info):
        self.https_urls_info = https_urls_info

    """
    Örnek çıktı:
    ['hakkindaguncelsikayetlern.merkezitr.app', '101spotcuzdanbinancemasak2.line.pm']
    """
    def get_http_urls_info(self):
        return self.http_urls_info
    
    """
    Örnek çıktı:
    ['hakkindaguncelsikayetlern.merkezitr.app', '101spotcuzdanbinancemasak2.line.pm']
    """
    def get_https_urls_info(self):
        return self.https_urls_info


    def set_http_blacklist_info(self, http_blacklist_info):
        self.http_blacklist_info = http_blacklist_info

    """
    Örnek çıktı:
    {'totalCount': 2, 'count': 2, 'models': [{'id': 591204, 'url': 'hakkindaguncelsikayetlern.merkezitr.app', 'type': 'domain', 'source': {}, 'date': '2023-12-10 18:34:40.45598', 'connectiontype': {'tr_title': 'Oltalama', 'en_title': 'Phishing', 'tr_desc': 'Finans sektörünün dışındaki sosyal mühendislik saldırılarına yönelik zararlı alan adı, IP adresi veya bağlantıların bulunduğu kategoridir.', 'en_desc': ''}}, {'id': 591184, 'url': '101spotcuzdanbinancemasak2.line.pm', 'type': 'domain', 'source': {'tr_title': 'SOME', 'en_title': 'CERT'}, 'date': '2023-12-10 18:22:54.559033', 'connectiontype': {'tr_title': 'Oltalama', 'en_title': 'Phishing', 'tr_desc': 'Finans sektörünün dışındaki sosyal mühendislik saldırılarına yönelik zararlı alan adı, IP adresi veya bağlantıların bulunduğu kategoridir.', 'en_desc': ''}}], 'page': 0, 'pageCount': 1}
    """
    def get_http_blacklist_info(self):
        return self.http_blacklist_info
    
    def set_https_blacklist_info(self, https_blacklist_info):
        self.https_blacklist_info = https_blacklist_info

    """
    Örnek çıktı:
    {'totalCount': 2, 'count': 2, 'models': [{'id': 591204, 'url': 'hakkindaguncelsikayetlern.merkezitr.app', 'type': 'domain', 'source': {}, 'date': '2023-12-10 18:34:40.45598', 'connectiontype': {'tr_title': 'Oltalama', 'en_title': 'Phishing', 'tr_desc': 'Finans sektörünün dışındaki sosyal mühendislik saldırılarına yönelik zararlı alan adı, IP adresi veya bağlantıların bulunduğu kategoridir.', 'en_desc': ''}}, {'id': 591184, 'url': '101spotcuzdanbinancemasak2.line.pm', 'type': 'domain', 'source': {'tr_title': 'SOME', 'en_title': 'CERT'}, 'date': '2023-12-10 18:22:54.559033', 'connectiontype': {'tr_title': 'Oltalama', 'en_title': 'Phishing', 'tr_desc': 'Finans sektörünün dışındaki sosyal mühendislik saldırılarına yönelik zararlı alan adı, IP adresi veya bağlantıların bulunduğu kategoridir.', 'en_desc': ''}}], 'page': 0, 'pageCount': 1}
    """
    def get_https_blacklist_info(self):
        return self.https_blacklist_info
    
    def query_whois_for_urls(self, urls):
        domain_info_list = []
        for url in urls:
            if url:
                domain_info = whois.DomainInfo(url)
                domain_info_model = domain_info.to_domain_info_model()
                domain_info_list.append(domain_info_model)
        return domain_info_list
    
    def update_email_content_urls_whois_info(self):
        # Mail içeriğindeki HTTP ve HTTPS URL'lerini al
        http_urls = self.get_http_urls_info()
        https_urls = self.get_https_urls_info()

        # URL'ler için whois bilgilerini al ve sakla
        self.email_content_urls_whois_info = self.query_whois_for_urls(http_urls + https_urls)

    """
    Örnek çıktı:
    [DomainInfoModel(domain_name='hakkindaguncelsikayetlern.merkezitr.app', registrar='Squarespace Domains II LLC', whois_server='whois.google.com', updated_date=datetime.datetime(2023, 7, 24, 15, 45, 39), creation_date=datetime.datetime(2023, 7, 19, 15, 45, 39), expiration_date=datetime.datetime(2024, 7, 19, 15, 45, 39), name_servers=['carlos.ns.cloudflare.com', 'gloria.ns.cloudflare.com'], status=['clientTransferProhibited https://icann.org/epp#clientTransferProhibited', 'clientTransferProhibited https://www.icann.org/epp#clientTransferProhibited'], emails=['registrar-abuse@google.com', 'abuse-complaints@squarespace.com'], dnssec='unsigned', org='Contact Privacy Inc. Customer 7151571251', state='ON', country='CA', is_created_within_1_year=True, is_created_within_2_years=True, is_created_within_3_years=True, is_created_within_4_years=True, is_created_within_5_years=True), DomainInfoModel(domain_name='101spotcuzdanbinancemasak2.line.pm', registrar='KEY-SYSTEMS GmbH', whois_server=None, updated_date=None, creation_date=None, expiration_date=datetime.datetime(2025, 6, 28, 19, 55, 19), name_servers=None, status=['ACTIVE', 'active', 'associated', 'not identified'], emails=['info@key-systems.net', 'dnsexit@gmail.com'], dnssec=None, org=None, state=None, country=None, is_created_w
    """
    def get_email_content_urls_whois_info(self):
        # Mail içeriğindeki URL'lerin whois bilgilerini döndür
        return self.email_content_urls_whois_info
    
    def create_summary(self):
        # Metni formatlayarak oluştur
        summary = (
            f"{self.attacker_email} adresinden {self.attacker_name} isminde potansiyel bir saldırgan tarafından, "
            f"{self.target_addr} adresine atılan potansiyel oltalama saldırısı {self.date} tarihinde "
            f"{self.subject} adı altında bir konu olarak atılmıştır. Epostanın içeriği şu şekildedir: {self.body}. "
            f"Eposta içerisinde HTTP olarak {self.get_http_urls_info()} ve HTTPS olarak {self.get_https_urls_info()} adresleri bulunmaktadır. "
            f"Bu adresler USOM veri tabanında sorgulandığında elde edilen bilgiler; HTTP adresleri için {self.get_http_blacklist_info()} ve "
            f"HTTPS adresleri için {self.get_https_blacklist_info()} şeklindedir. Saldırganın whois bilgileri ise {self.get_sender_domain_info()} şeklindedir. "
            f"Aynı zamanda mail içeriğindeki HTTP ve HTTPS adreslerinin whois bilgilerinin içeriği ise {self.get_email_content_urls_whois_info()} şeklinde belirtilmiştir."
        )
        return summary




