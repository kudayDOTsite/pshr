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
        

    def get_target_address(self):
        return self.target_addr

    def get_target_name(self):
        return self.target_name

    def get_target_domain(self):
        return self.target_domain

    def get_date(self):
        return self.date

    def get_subject(self):
        return self.subject

    def get_body(self):
        return self.body

    def is_email_forwarded(self):
        return self.is_forwarded

    def get_attacker_email(self):
        return self.attacker_email

    def get_attacker_domain(self):
        return self.attacker_domain

    def get_attacker_name(self):
        return self.attacker_name