import whois
from dataclasses import dataclass

@dataclass
class DomainInfoModel:
    domain_name: str
    registrar: str
    whois_server: str
    updated_date: str
    creation_date: str
    expiration_date: str
    name_servers: list
    status: list
    emails: list
    dnssec: str
    org: str
    state: str
    country: str

class DomainInfo:
    def __init__(self, domain_name):
        self.domain_name = domain_name
        self.info = self.get_domain_info()

    def get_domain_info(self):
        try:
            domain_info = whois.whois(self.domain_name)
            return domain_info
        except whois.parser.PywhoisError as e:
            return str(e)

    def to_domain_info_model(self):
        domain_info = self.info
        return DomainInfoModel(
            domain_name=self.domain_name,
            registrar=domain_info.registrar,
            whois_server=domain_info.whois_server,
            updated_date=domain_info.updated_date,
            creation_date=domain_info.creation_date,
            expiration_date=domain_info.expiration_date,
            name_servers=domain_info.name_servers,
            status=domain_info.status,
            emails=domain_info.emails,
            dnssec=domain_info.dnssec,
            org=domain_info.org,
            state=domain_info.state,
            country=domain_info.country
        )

if __name__ == "__main__":
    # Domain adını belirtin
    domain_name = "berenkudaygorun.com"

    # Domain bilgilerini alın
    domain_info = DomainInfo(domain_name).to_domain_info_model()
    # Alınan bilgileri görüntüleyin
    print("Domain Bilgileri:")
    print(domain_info.domain_name)
    print(domain_info.creation_date)
    # Diğer özelliklere de erişebilirsiniz
