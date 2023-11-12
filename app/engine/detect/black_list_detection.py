import requests
import json

class DomainChecker:
    def __init__(self, domain_list):
        self.domain_list = domain_list
        self.results = []
        self.categories = {
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
        self.sources = {
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
        self.connection_types = {
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

        self.check_domains()

    def check_domains(self):
        for domain in self.domain_list:
            url = f"https://www.usom.gov.tr/api/address/index?url={domain}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if "models" in data:
                    for item in data["models"]:
                        if item["url"] in self.domain_list:
                            result = {
                                "id": item["id"],
                                "url": item["url"],
                                "type": item["type"],
                                "source": self.sources.get(item["source"], {}),
                                "date": item["date"],
                                "connectiontype": self.connection_types.get(item["connectiontype"], {}),
                            }
                            # Kategoriye göre açıklama eklemek
                            if result["type"] in self.categories:
                                result["desc"] = self.categories[result["type"]]
                            self.results.append(result)

    def get_results(self):
        total_count = len(self.results)
        response_data = {
            "totalCount": total_count,
            "count": total_count,
            "models": self.results,
            "page": 0,
            "pageCount": 1,
        }
        return response_data

# Örnek kullanım
if __name__ == "__main__":
    domain_list = ["tokisbasvurum.blogspot.com", "tokivbasvurulari.blogspot.com", "example2.com"]
    domain_checker = DomainChecker(domain_list)
    domain_checker.check_domains()
    response_data = domain_checker.get_results()
    response_json = json.dumps(response_data, ensure_ascii=False, indent=4)
    print(response_json)
