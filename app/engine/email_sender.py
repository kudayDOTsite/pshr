import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, smtp_username, smtp_password):
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.smtp_server = "smtp.gmail.com"  # Gmail SMTP sunucu adresi
        self.smtp_port = 587  # Gmail SMTP sunucu portu

    def send_email(self, subject, body, recipient_email):
        # E-posta başlık ve içeriğini hazırla
        msg = MIMEMultipart()
        msg['From'] = self.smtp_username
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # E-posta metni ekleniyor
        msg.attach(MIMEText(body, 'plain'))

        # Gmail SMTP sunucusuna bağlan
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.smtp_username, self.smtp_password)

            # E-postayı gönder
            server.sendmail(self.smtp_username, recipient_email, msg.as_string())
            server.quit()
            print("E-posta gönderildi!")
        except Exception as e:
            print("E-posta gönderme hatası:", str(e))

if __name__ == "__main__":
    gmail_username = "your@gmail.com"  # Gmail hesap kullanıcı adı
    gmail_password = "your_password"  # Gmail hesap şifresi

    
