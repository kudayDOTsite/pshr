import requests

# Belirtilen domain listesi
domain_list = ["tokisbasvurum.blogspot.com", "tokivbasvurulari.blogspot.com", "example2.com"]

# Kategoriler ve kaynaklar
categories = {
    "BP": {
        "tr_title": "Bankacılık - Oltalama",
        "en_title": "Financial Phishing",
        "tr_desc": "Finsans sektörüne özel olarak gerçekleştirilen sosyal mühendislik saldırılarına yönelik zararlı alan adı, IP adresi veya bağlantıların bulunduğu kategoridir.",
        "en_desc": ""
    },
    "PH": {
        "tr_title": "Oltalama",
        "en_title": "Phishing",
        "tr_desc": "Finans sektörünün dışındaki sosyal mühendislik saldırılarına yönelik zararlı alan adı, IP adresi veya bağlantıların bulunduğu kategoridir.",
        "en_desc": ""
    },
    "MD": {
        "tr_title": "Zararlı Yazılım Barındıran / Yayan Alan Adı",
        "en_title": "Malware Distribution Domain",
        "tr_desc": "Zararlı yazılımların çalışması için bir bölümünün veya tamamının indirildiği alan adlarına ait kategoridir.",
        "en_desc": ""
    }
}

sources = {
    "US": {
        "tr_title": "USOM",
        "en_title": "TR-CERT"
    },
    "SO": {
        "tr_title": "SOME",
        "en_title": "CERT"
    },
    "RS": {
        "tr_title": "RSA",
        "en_title": "RSA"
    }
}

connection_types = {
    "BP": {
        "tr_title": "Bankacılık - Oltalama",
        "en_title": "Financial Phishing",
        "tr_desc": "Finsans sektörüne özel olarak gerçekleştirilen sosyal mühendislik saldırılarına yönelik zararlı alan adı, IP adresi veya bağlantıların bulunduğu kategoridir.",
        "en_desc": ""
    },
    "PH": {
        "tr_title": "Oltalama",
        "en_title": "Phishing",
        "tr_desc": "Finans sektörünün dışındaki sosyal mühendislik saldırılarına yönelik zararlı alan adı, IP adresi veya bağlantıların bulunduğu kategoridir.",
        "en_desc": ""
    },
    "MD": {
        "tr_title": "Zararlı Yazılım Barındıran / Yayan Alan Adı",
        "en_title": "Malware Distribution Domain",
        "tr_desc": "Zararlı yazılımların çalışması için bir bölümünün veya tamamının indirildiği alan adlarına ait kategoridir.",
        "en_desc": ""
    }
}

results = []

# Her domain için istek gönderme
for domain in domain_list:
    url = f"https://www.usom.gov.tr/api/address/index?url={domain}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "models" in data:
            for item in data["models"]:
                if item["url"] in domain_list:
                    result = {
                        "id": item["id"],
                        "url": item["url"],
                        "type": item["type"],
                        "source": sources.get(item["source"], {}),
                        "date": item["date"],
                        "connectiontype": connection_types.get(item["connectiontype"], {}),
                    }
                    # Kategoriye göre açıklama eklemek
                    if result["type"] in categories:
                        result["desc"] = categories[result["type"]]
                    results.append(result)

# Cevapları işleme
total_count = len(results)
response_data = {
    "totalCount": total_count,
    "count": total_count,
    "models": results,
    "page": 0,
    "pageCount": 1,
}

# JSON formatında cevap
import json

response_json = json.dumps(response_data["models"], ensure_ascii=False, indent=4)
print(response_json)
