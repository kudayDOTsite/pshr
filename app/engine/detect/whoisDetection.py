import whois
from datetime import datetime, timedelta
from dateutil import parser
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

    def to_datetime(self, date_obj):
        if isinstance(date_obj, datetime):
            return date_obj
        try:
            return parser.parse(str(date_obj))
        except (ValueError, TypeError):
            return None
    
    def get_domain_info(self):
        try:
            domain_info = whois.whois(self.domain_name)
            return domain_info
        except whois.parser.PywhoisError:
            # Hata durumunda None dön
            return None
        
        
    def try_get_attr(self, obj, attr):
        try:
            return getattr(obj, attr)
        except Exception:
            return None

    def to_domain_info_model(self):
        domain_info = self.info
        return DomainInfoModel(
            domain_name=self.domain_name,
            registrar=self.try_get_attr(domain_info, 'registrar'),
            whois_server=self.try_get_attr(domain_info, 'whois_server'),
            updated_date=self.try_get_attr(domain_info, 'updated_date'),
            creation_date=self.try_get_attr(domain_info, 'creation_date'),
            expiration_date=self.try_get_attr(domain_info, 'expiration_date'),
            name_servers=self.try_get_attr(domain_info, 'name_servers'),
            status=self.try_get_attr(domain_info, 'status'),
            emails=self.try_get_attr(domain_info, 'emails'),
            dnssec=self.try_get_attr(domain_info, 'dnssec'),
            org=self.try_get_attr(domain_info, 'org'),
            state=self.try_get_attr(domain_info, 'state'),
            country=self.try_get_attr(domain_info, 'country'),
            is_created_within_1_year=self.is_created_within_1_year(),
            is_created_within_2_years=self.is_created_within_2_years(),
            is_created_within_3_years=self.is_created_within_3_years(),
            is_created_within_4_years=self.is_created_within_4_years(),
            is_created_within_5_years=self.is_created_within_5_years()
        )

    
    def is_created_within_years(self, years):
        if self.info is None:
            return False

        creation_dates = self.info.creation_date
        if creation_dates is None:
            return False

        if not isinstance(creation_dates, list):
            creation_dates = [creation_dates]

        years_ago = datetime.now() - timedelta(days=365 * years)
        for date in creation_dates:
            date = self.to_datetime(date)
            if date and date >= years_ago:
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