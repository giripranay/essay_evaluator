from django import forms
from .models import Essay

class EssayForm(forms.ModelForm):
    class Meta:
        model = Essay
        fields = ['title', 'body']
    
    def clean_body(self):
        body = self.cleaned_data.get('body', '')
        word_count = len(body.split())
        if word_count > 500:
            raise forms.ValidationError("The essay body cannot exceed 500 words. You have used {} words.".format(word_count))
        return body
