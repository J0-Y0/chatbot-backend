from django.conf import settings


# open router api doc
from openai import OpenAI
class ChatService:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.OPEN_ROUTER_API_KEY
        )
    
    def ai_response(self, prompt):
        self.completion = self.client.chat.completions.create(
            #   extra_headers={
            #     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
            #     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
            #   },
            extra_body={},
            model="meta-llama/llama-3.3-8b-instruct:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return self.completion
# print(completion.choices[0].message.content)




