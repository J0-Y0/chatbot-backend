from django.db import models
class Session(models.Model):
    token_count = models.IntegerField(null=True,editable=False)
    name = models.CharField(max_length=1000)
    def get_last_3_chats(self,obj):
        chats =  obj.chats.order_by('-created_at')[:3]
        history_prompt = []
        for chat in chats:
            history_prompt.append({"role": "user", "content": chat.prompt})
            history_prompt.append({"role": "assistant", "content": chat.ai_response})
            
        return history_prompt

class Chat(models.Model):
    prompt = models.TextField()
    ai_response = models.TextField(editable=False)
    chat_id = models.CharField(primary_key=True,editable=False,max_length=1000)
    token_count = models.IntegerField(null=True,editable=False)
    parent = models.ForeignKey('self', null=True,blank=True, on_delete=models.CASCADE)
    session = models.ForeignKey(Session,null=True, on_delete=models.CASCADE,related_name="chats")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.prompt[0:50]