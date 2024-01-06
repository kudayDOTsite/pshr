import openai

class EmailAnalysis:
    def __init__(self, openai_api_key):
        self.client = openai.Client(api_key=str(openai_api_key))
    def analyze_email(self, email_info):

        # OpenAI'ye gönderilecek mesajları hazırla
        messages = [
            {
                "role": "system",
                "content": "Sana verilen içerikte bir mail ile ilgili çeşitli bilgiler var." + 
                "Bu mailin potansiyel oltalama saldırısı olup olmadığını analiz etmeni isteyeceğim. " + 
                "Ancak çok katı bir şekilde karalar almanı istemiyorum. Genelde kullanıcıdan kişisel verilerini isteyen, banka bilgilerini isteyen, tehditkar bir şekilde onları yönlendiren, onlara şaşırtıcı düzeyde cazip fırsatlar sunan maillerin oltalama saldırısı olma ihtimali daha yüksektir." +
                "Aynı zamanda kullanıcıların kimlik bilgilerini, parolalarını isteyen mailer ya da bu bilgileri değiştirme yönünde talimatlar veren mailler oltalama saldırısı olabilir. Bu şekilde bir mail ile karşılaşırsan mail içerisindeki adreslerin whois ve USOM sonuçlarına göre değerlendirme yapmanı isteyeceğim. Eğer adresler gerçekten güvenilir kaynaklar ise ve mailde güvenilir bir kaynaktan geliyorsa mail'e güvenebilirsin. Ancak resmi ve güvenilir kuruluşların direkt olarak bir parola sıfırlama linki göndermek yerine doğrulama kodu gönderdiğinide unutma." +
                "Mail analizi yapılırken cümle yapısında bir hata görmezsen, yazım hatası görmezsen, devrik cümleler ile karşılaşmazsan, bağlantıların whois bilgilerinin güvenilir olduğunu düşünürsen, USOM veritabanında bir bulgu ile karşılaşmazsan gelen mailin güvenilir olduğu hakkında yorum yapabilirsin ancak tedirginlik yaratacak bir şey bulursan bunu belirtmelisin. " +
                "Günün sonunda analizlerini gerçekleştir ve bana mail'in bir oltalama olup olmadığı hakkında yorum yap." +
                "Yorumun en sonunda Mailin oltama maili olma ihtimalini temsil eden 1 ya da 0 gibi bir değer belirt. Örneğin cevabının en sonuna 'Oltalama Mail Olma İhtimali : 1' gibi bir değer yazmalısın. Eğer mailin oltalama maili olmadığını düşünüyorsan 0 yazacaksın."
                "Ayrıca analizlerinin sonuna şu metni kesinlikle ekle: Bu sonuçlar GPT teknolojisi ile yapılmıştır, kullandığınız yazılım ticari bir ürün olmayıp Koç Üniversitesi Siber Güvenlik Bölümü Yüksek Lisans Dönem ödevidir."
            },
            {
                "role": "user",
                "content": str(email_info)
            }
]


        try:
            # OpenAI API'sine istek gönder
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=messages
            )
            return response.choices[0].message.content

        except Exception as e:
            # OpenAI API'den gelen hata mesajını yazdır
            print(f"OpenAI API hatası: {e}")
            return "API hatası nedeniyle analiz yapılamadı."
