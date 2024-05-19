from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Essay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = RichTextField(help_text="Please limit your essay to 500 words.")
    feedback = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
