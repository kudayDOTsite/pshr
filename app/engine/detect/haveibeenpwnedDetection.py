import requests
from bs4 import BeautifulSoup

# Kullanılacak URL ve e-posta adresi
base_url = "https://haveibeenpwned.com"
search_url = f"{base_url}/unifiedsearch/"
email = "test@example.com"  # Sorgulanacak e-posta adresi

# Kullanıcı ajanı (User-Agent) ayarları
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Safari/537.36"

# Oturumu başlat
session = requests.Session()

# İsteğin başlıklarını ayarla (User-Agent)
headers = {"User-Agent": user_agent}
session.headers.update(headers)

# İlk sayfaya GET isteği gönder
response = session.get(base_url)

# Oturumun çerezlerini al
cookies = session.cookies.get_dict()
print(cookies)
# Çerezleri sonraki isteklerde kullanmak için sakla

# BeautifulSoup kullanarak sayfanın HTML içeriğini analiz et
soup = BeautifulSoup(response.text, "html.parser")
print(response.text)

# cf-turnstile-response adında bir input elementi bul
cf_turnstile_input = soup.find("input", {"name": "cf-turnstile-response"})

if cf_turnstile_input:
    # cf-turnstile-response elementinin 'value' özelliğini al
    cf_turnstile_value = cf_turnstile_input.get("value")

    # Cf-Turnstile-Response header'ını oluştur
    cf_turnstile_header = {"Cf-Turnstile-Response": cf_turnstile_value}

    # E-posta sorgusu için başka bir URL oluştur
    email_check_url = f"{search_url}{email}"

    # Son sayfaya GET isteği gönder
    response = session.get(email_check_url, cookies=cookies, headers=cf_turnstile_header)

    # Yanıtı kontrol et
    if response.status_code == 200:
        print("Başarılı istek:")
        print(response.text)
    elif response.status_code == 404:
        print("Clean")
    else:
        print(f"İstek başarısız. HTTP Kodu: {response.status_code}")
else:
    print("cf-turnstile-response input elementi bulunamadı.")
