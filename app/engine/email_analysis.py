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
                " Bu mailin bir mail'in potansiye oltalama saldırısı olup olmadığını analiz etmeni isteyeceğim. " + 
                "Ancak çok katı bir şekilde karalar almanı istemiyorum. Genelde kullanıcıdan kişisel verilerini isteyen, banka bilgilerini isteyen, tehditkar bir şekilde onları yönlendiren, onlara şaşırtıcı düeyde cazip fırsatlar sunan maillerin oltalama saldırısı olma ihtimali daha yüksektir." +
                " Mail analizi yapılırken eğer genel olarak cümle yapısında bir hata görmezsen, bağlantıların whois bilgilerinin güvenilir olduğunu düşünürsen, USOM veritabanında bir bulgu ile karşılaşmazsan gelen mailin güvenilir olduğu hakkında yorum yapabilirsin ancak tedirginlik yaratacak bir şey bulursan bunu belirtmelisin. " +
                "Günün sonunda analizlerini gerçekleştir ve bana mail'in bir oltalama olup olmadığı hakkında yorum yap." +
                " Ayrıca analizlerinin sonuna şu metni kesinlikle ekle: Bu sonuçlar GPT teknolojisi ile yapılmıştır, kullandığınız yazılım ticari bir ürün olmayıp Koç Üniversitesi Siber Güvenlik Bölümü Yüksek Lisans Dönem ödevidir."
            },
            {
                "role": "user",
                "content": str(email_info)
            }
]


        # OpenAI API'sine istek gönder
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages
        )

        return response.choices[0].message.content
