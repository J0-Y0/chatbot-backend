from django.db import models

class Chat(models.Model):
    prompt = models.CharField(max_length=1000)
    ai_response = models.CharField(max_length=1000)
    chat_id = models.AutoField(primary_key=True)
    token_count = models.IntegerField(null=True)
    parent = models.ForeignKey('self', null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.prompt