import whois
from datetime import datetime, timedelta
from dataclasses import dataclass, field

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
    is_created_within_1_year: bool = field(default=False)
    is_created_within_2_years: bool = field(default=False)
    is_created_within_3_years: bool = field(default=False)
    is_created_within_4_years: bool = field(default=False)
    is_created_within_5_years: bool = field(default=False)


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
            country=domain_info.country,
            is_created_within_1_year=self.is_created_within_1_year(),
            is_created_within_2_years=self.is_created_within_2_years(),
            is_created_within_3_years=self.is_created_within_3_years(),
            is_created_within_4_years=self.is_created_within_4_years(),
            is_created_within_5_years=self.is_created_within_5_years()

        )
    
    def is_created_within_years(self, years):
        creation_date = self.info.creation_date
        if not isinstance(creation_date, list):
            creation_date = [creation_date]

        years_ago = datetime.now() - timedelta(days=365 * years)
        if creation_date[0] >= years_ago:
            return True

        return False

    def is_created_within_1_year(self):
        return self.is_created_within_years(1)

    def is_created_within_2_years(self):
        return self.is_created_within_years(2)

    def is_created_within_3_years(self):
        return self.is_created_within_years(3)

    def is_created_within_4_years(self):
        return self.is_created_within_years(4)

    def is_created_within_5_years(self):
        return self.is_created_within_years(5)