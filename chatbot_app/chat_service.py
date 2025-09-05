from django.conf import settings


# open router api doc
from openai import OpenAI
class ChatService:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.OPEN_ROUTER_API_KEY
        )
    
    def ai_response(self, prompt,history_prompt=None):
        messages = history_prompt or []
        
        # Append the new user prompt to the message list
        messages.append({
            "role": "user", 
            "content": prompt
        })

        self.completion = self.client.chat.completions.create(
            #   extra_headers={
            #     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
            #     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
            #   },
            extra_body={},

            model="meta-llama/llama-3.3-8b-instruct:free",
            
            messages=messages
        )

        return self.completion
# print(completion.choices[0].message.content)




