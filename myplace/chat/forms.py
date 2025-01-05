from django import forms

class ChatForm(forms.Form):
    user_input = forms.CharField(
        label='質問',
        max_length=500,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '質問を入力してください'})
    )
