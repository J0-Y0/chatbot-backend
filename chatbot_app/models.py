from django.db import models

class Chat(models.Model):
    prompt = models.CharField(max_length=3000)
    ai_response = models.CharField(max_length=1000,editable=False)
    chat_id = models.CharField(primary_key=True,editable=False,max_length=1000)
    token_count = models.IntegerField(null=True,editable=False)
    parent = models.ForeignKey('self', null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.prompt
    