import json

def update_phishing_probability(file_path):
    # JSON dosyasını yükleme
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Analiz ve güncelleme
    for item in data:
        if item['phishing_probability'] == "0":
            # Eğer ': 1' ifadesi analysis_result içinde geçiyorsa
            if ': 1' in item['analysis_result']:
                item['phishing_probability'] = "1"

    # Güncellenmiş veriyi dosyaya yazma
    with open('email_analysis_results.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("[*] Tamam")
    print(len(data))

# Dosya yolu (Örnek: 'email_analysis_results.json')
file_path = 'email_analysis_results.json'
update_phishing_probability(file_path)
