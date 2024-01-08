import pandas as pd
import email
import quopri
import sys
sys.path.append('../')
sys.path.append('../app/engine/')
from email.parser import Parser
import app.engine.email_info as ei
import app.engine.detect.whoisDetection as whois
import app.engine.detect.linkDetection as linkDetection
import app.engine.detect.black_list_detection as blackListDetection
import app.engine.email_analysis as ea
import configparser
import json

config = configparser.ConfigParser()
config.read('../.env')
OPENAI_KEY = config.get('OPENAI', 'OPENAI_KEY')

# CSV dosyasını okuyan fonksiyon
def read_csv(file_path):
    return pd.read_csv(file_path)

# E-posta verilerini parse eden fonksiyon
def parse_email(row):
    receiver = str(row['receiver'])
    if ',' in receiver:
        receiver = receiver.split(',')[0]

    sender = str(row['sender'])
    if ',' in sender:
        sender = sender.split(',')[0]
    email_data = {
        'sender': sender,
        'receiver': receiver,
        'date': row['date'],
        'urls': row['urls'],
        'subject': row['subject'],
        'body': row['body']
    }
    return email_data

# Ana fonksiyon
def main(csv_file_path):
    df = read_csv(csv_file_path)
    parsed_emails = []

    for index, row in df.iterrows():
        email_info = parse_email(row)
        # Burada email_info'yu projenizin analiz kısmına gönderebilirsiniz
        # Örneğin: analyze_email(email_info)
        parsed_emails.append(email_info)

    # İşlenmiş e-postaları döndür
    return parsed_emails


def run(emails):
    results = []  # Tüm e-postaların sonuçlarını saklamak için liste
    index = 0
    for email_data in emails:
        # EmailInfo sınıfı için gerekli bilgileri çıkar
        target_addr = email_data['receiver'] if isinstance(email_data['receiver'], str) else "NULL"
        target_name = target_addr.split('@')[0] if '@' in target_addr else "NULL"
        target_domain = target_addr.split('@')[1] if '@' in target_addr else "NULL"
        date = email_data['date']
        decoded_subject = email_data['subject']
        email_body = email_data['body']
        is_forwarded = 'Forwarded' in email_body # E-postanın iletildiğini kontrol edin
        attacker_email = email_data['sender'] if isinstance(email_data['sender'], str) else "NULL"
        attacker_name = attacker_email.split('@')[0] if '@' in attacker_email else ""
        attacker_domain = attacker_email.split('@')[1] if '@' in attacker_email else ""

        # EmailInfo sınıfı örneği oluştur
        email_info = ei.EmailInfo(
            target_addr, 
            target_name, 
            target_domain, 
            date, 
            decoded_subject, 
            email_body, 
            is_forwarded, 
            attacker_email, 
            attacker_name,  
            attacker_domain
        )

        #Çeşitli debug işlemleri için bırakılmış bir alan
        #if(index == 229):

        wh = whois.DomainInfo(email_info.attacker_domain)
        email_info.set_sender_domain_info(wh.to_domain_info_model())

        ld = linkDetection.DomainCounter()
        ld.set_text(email_info.body)
        email_info.set_http_urls_info(ld.http_domains)
        email_info.set_https_urls_info(ld.https_domains)

        httpBlackListDetection = blackListDetection.DomainChecker(ld.http_domains)
        email_info.set_http_blacklist_info(httpBlackListDetection.get_results())
        httpsBlackListDetection = blackListDetection.DomainChecker(ld.https_domains)
        email_info.set_https_blacklist_info(httpsBlackListDetection.get_results())

        email_info.update_email_content_urls_whois_info()

    

        email_analyzer = ea.EmailAnalysis(OPENAI_KEY)
        analysis_result = email_analyzer.analyze_email(email_info.create_summary())

        email_result = {
            "sender": email_data['sender'],
            "receiver": email_data['receiver'],
            "date": email_data['date'],
            "subject": email_data['subject'],
            "body": email_data['body'],
            "analysis_result": analysis_result,
            "phishing_probability": "1" if ": 1" in analysis_result else "0"
        }

        # Sözlüğü sonuç listesine ekle
        results.append(email_result)
        index += 1
        print(f"[*] {index} adet e-posta analiz edildi!")
        
    
    print(results)
    # Sonuçları düz metin olarak başka bir dosyaya yaz
    with open('email_analysis_results.txt', 'w', encoding='utf-8') as f:
        for result in results:
            f.write(json.dumps(result, ensure_ascii=False, indent=4) + "\n\n")


    # Sonuçları JSON dosyasına yaz
    with open('email_analysis_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print("Analiz sonuçları 'email_analysis_results.json' dosyasına kaydedildi.")

        
if __name__ == '__main__':
    csv_file_path = 'datas/Nigerian_Fraud.csv'  # CSV dosyasının yolu
    emails = main(csv_file_path)
    run(emails)


