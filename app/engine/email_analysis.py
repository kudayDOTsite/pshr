import openai

class EmailAnalysis:
    def __init__(self, openai_api_key):
        self.client = openai.Client(api_key=str(openai_api_key))
    def analyze_email(self, email_info):

        # OpenAI'ye gönderilecek mesajları hazırla
        messages = [
            {
                "role": "system",
                "content": "Sana verilen içerikte bir mail ile ilgili çeşitli bilgiler var. Bu mailin bir mail'in potansiye oltalama saldırısı olup olmadığını analiz etmeni isteyeceğim. Günün sonunda analizlerini gerçekleştir ve bana mail'in bir oltalama olup olmadığı hakkında yorum yap."
            },
            {
                "role": "user",
                "content": str(email_info)
            }
]


        # OpenAI API'sine istek gönder
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        return response.choices[0].message.content
