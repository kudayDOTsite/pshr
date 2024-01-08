import openai

class EmailAnalysis:
    def __init__(self, openai_api_key):
        self.client = openai.Client(api_key=str(openai_api_key))
    def analyze_email(self, email_info):

        # OpenAI'ye gönderilecek mesajları hazırla
        messages = [
            {
                "role": "system",
                "content": "Sana verilen içerikte bir mail ve bu mail ile ilgili çeşitli analizler içeren bilgiler bulunmaktadır. " + 
                "Bu içerikte (yani sana verilen mailde) potansiyel bir oltalama saldırısı olup olmadığını analiz etmeni isteyeceğim. " + 
                "Eğer mail içerisinde hedef kişiden ya da kişilerden KVKK ya da GDPR ihlaline sebep olacak kişisel veriler isteyen içerikler mevcutsa bunu potansiyel bir oltalama saldırısı olarak yorumlamanı istiyorum. " +
                "Eğer mail içerisinde hedef kişinin Adres, Cinsiyet, Yaş, Telefon, Meslek, İsim vb. bilgilerini istediği bir form ya da açık bir şekilde bilgi talep edilirse bunu potansiyel bir oltalama saldırısı olarak yorumlamanı istiyorum. " +
                "Eğer mail içerisinde hedef kişiye bir para teklifinde bulunulursa, bir fona yatırım yapma teklifinde bulunulursa, belli bir miktar para gönderimi sonucunda avantajlı bir kar elde edeceği teklifiinde bulunulursa, hızlı bir şekilde kullanıcıdan bu tarz konular için cevap isteğinde bulunulursa bunu potansiyel bir oltalama saldırısı olarak yorumlamanı istiyorum. " +
                "Eğer mail içerisinde hedef kişinin banka hesaplarının herhangi bir yolsuzluğa karıştırıldığı şeklinde ifadeler varsa ve hedef kişiden hızlı bir şekilde aksiyon alınmasını isteyen ifadeler yer alıyorsa bunu potansiyel bir oltalama saldırısı olarka yorumlamanı istiyorum. " + 
                "Eğer mail içerisinde hedef kişiye yüksek karlı bir ortaklık teklifinde bulunuluyorsa bunu potansiyel bir oltalama saldırısı oalrak yorumlamanı istiyorum. " +
                "Eğer mail içerisinde metinde tehditkar içerikler, cazip fırsatlar, kolay yoldan zengin olmak, acele karar verilmesi istenen, duygu sömürüsü yapan, korkutucu içeriğe sahip olan ifadeler yer alırsa bunu potansiyel bir oltalama saldırısı olarak yorumlamanı istiyorum. " +
                "Eğer mail içerisinde hedef kişiden ya da kişilerden herhangi bir hesabına ait kullanıcı adı, parola vb. bilgileri talep eden içerikler varsa direkt olarak bunu bir oltalama saldırısı olarak belirleyebilirsin. "+
                "Eğer mail içerisindeki ifadelerde devrik cümleler, yazım hataları tespit edersen potansiyel bir oltalama saldırısı olarak yorumlamanı istiyorum. " +
                "Mail metni haricinde sana verilmiş olan analizlerde whois bilgileri önemli bir yer tutmaktadır. Eğer domain kaydı çok yeni ise (Örnek olarak son 1 yıl içerisinde alınmış bir domain gibi) bunu potansiyel bir oltalama saldırısı olarak yorumlamanı istiyorum. Eğer whois bilgileri hakkında sana bir bilgi verilmez ise (muhtemelen domain artık kullanımda değildir) whois yorumlaması yapmana gerek yok. Sana verilen diğer talimatlara göre analiz yapmanı istiyorum. " + 
                "Mail metni haricinde sana verilmiş olan analizlerde USOM (Türkiyede geliştirilen Ulusal Siber Olaylara Müdahale Merkezi'nin bir oltalama saldırıları ve dolandırıcılık için geliştirilmiş api hizmeti sunan veritabanıdır) kayıtları yer almaktadır. Eğer sana verilen bilgilerde USOM sonuçlarına göre zararlı bir bağlantı tespit edersen direkt olarak oltama maili olarak yorum yapmanı istiyorum ancak USOM kayıtlarında herhangi bir tespitin olmazsa (büyük ihtimalle api tarafında kayıtlı olmadığı için boş bir cevap gelecektir) sana verilen diğer talimatlara göre analiz yapmanı istiyorum. " +
                "Yorumun en sonunda Mailin oltama maili olma ihtimalini temsil eden bir ifade bırakmanı istiyorum. Bu ifadenin syntax'ı kesinlikle değişmemeli çünkü analiz yaparken sonuçlar için bakacağım kısım burası olacak. Eğer analizlerin sonucunda sana verilmiş olan mail metni hakkında en ufak bir oltalama saldırısı şüphen olursa üreteceğin cevabın sonuna 'Sonuç: 1' ifadesini yazmanı, aksi durumda 'Sonuç : 0' ifadesini yazmanı itiyorum. Bu ifadeyi her cevabın için yazmak zorundasın ve söz dizimini kesinlikle değiştirmemelisin. Syntax'ını kesinlikle değiştirme. "
#                "Ayrıca analizlerinin sonuna şu metni kesinlikle ekle: Bu sonuçlar GPT teknolojisi ile yapılmıştır, kullandığınız yazılım ticari bir ürün olmayıp Koç Üniversitesi Siber Güvenlik Bölümü Yüksek Lisans Dönem ödevidir."
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
