import imaplib
import email
import quopri
import re
import email_info as ei
import os

env_path = os.path.join(os.path.dirname(__file__), "../.env")


with open(env_path) as f:
    env = dict(line.split("=") for line in f)


IMAP_SERVER = env['IMAP_SERVER']
IMAP_SERVER = IMAP_SERVER[:len(IMAP_SERVER)-1]
IMAP_USER = env['IMAP_USER']
IMAP_PASSWORD = env['IMAP_PASSWORD']

def extract_target_addr(from_header):
    # "From" başlığını işleyen metot
    if '<' in from_header and '>' in from_header:
        return from_header.split('<')[1].split('>')[0]
    else:
        return None

def extract_decoded_subject(subject_header):
    # Başlığı işleyen metot
    subject = email.header.decode_header(subject_header)[0]
    if isinstance(subject[0], bytes):
        return subject[0].decode(subject[1] or 'utf-8')
    else:
        return subject[0]

def extract_email_body(payload):
    # E-posta içeriğini işleyen metot
    forwarded_message = payload.split('---------- Forwarded message ---------')[1] if '---------- Forwarded message ---------' in payload else None
    return forwarded_message.strip() if forwarded_message else "E-posta içeriği çözümlenemedi."

def extract_target_name(from_header):
    # Hedefin adını çıkaran metot
    return from_header.split('<')[0]

def extract_domain(_addr):
    # Hedefin domainini çıkaran metot
    return _addr.split('@')[1]

def extract_date(date_header):
    # Tarihi çıkaran metot
    return date_header

def is_email_forwarded(email_body):
    # E-postanın ileriye yönlendirilip yönlendirilmediğini kontrol eden metot
    return email_body.startswith("---------- Forwarded message ---------")


def extract_attacker(forwarded_email_body):
    # Saldırganın domainini çıkaran metot
    return re.findall(r'<(.*)>', forwarded_email_body)[0]


def fetch_emails_from_sender(sender_email):
    # E-postaları çeken metot
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(IMAP_USER, IMAP_PASSWORD)
    mail.select('inbox')

    latest_emails = []

    status, email_ids = mail.search(None, f'FROM "{sender_email}"')
    email_id_list = email_ids[0].split()
    if email_id_list:
        latest_email_id = email_id_list[-1]

        status, email_data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = email_data[0][1]
        msg = email.message_from_bytes(raw_email)

        target_addr = extract_target_addr(msg['from'])
        target_name = extract_target_name(msg['from'])
        target_domain = extract_domain(target_addr)
        date = extract_date(msg['date'])

        decoded_subject = extract_decoded_subject(msg['subject'])

        email_body = ""
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                payload = part.get_payload(decode=True).decode('utf-8')
                email_body = extract_email_body(payload)

        is_forwarded = email_body.startswith("---------- Forwarded message ---------")

        attacker_email = extract_attacker(email_body)
        attacker_name = extract_target_name(email_body)
        attacker_domain = extract_domain(attacker_email)
        is_forwarded = is_email_forwarded(email_body)

        latest_email = ei.EmailInfo(target_addr, target_name, target_domain, date, decoded_subject, email_body, is_forwarded, attacker_email, attacker_name,  attacker_domain)
        latest_emails.append(latest_email)

    mail.logout()
    return latest_emails

def main():
    specific_senders = ["pentesterpentester14@gmail.com"]
    latest_specific_emails = []
    for sender in specific_senders:
        latest_emails = fetch_emails_from_sender(sender)
        latest_specific_emails.extend(latest_emails)

    for email_info in latest_specific_emails:
        print('Saldırgan:', email_info.attacker_email)
        print('Saldırgan Adı:', email_info.attacker_name)
        print('Saldırgan Domaini:', email_info.attacker_domain)
        print('Hedef:', email_info.target_addr)
        print('Hedef Adı:', email_info.target_name)
        print('Hedef Domaini:', email_info.target_domain)
        print('Tarih:', email_info.date)
        print('Başlık:', email_info.subject)
        print('İçerik:')
        print(email_info.body)
        print()

if __name__ == "__main__":
    main()
