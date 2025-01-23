 # views.py
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.urls import reverse_lazy

from openai import OpenAI
from datetime import datetime
import pytz

from .forms import ChatForm
from .models import ChatLog
from local_settings.settings_code import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)
class ChatView(LoginRequiredMixin,FormView):
    template_name = "chat/chat.html"
    form_class = ChatForm
    login_url = reverse_lazy("login")
    success_url = "/"

    def form_valid(self, form):
        user_input = form.cleaned_data['user_input']

        try:
            # Chatモデル用エンドポイントを使用
            response = client.chat.completions.create(model="gpt-3.5-turbo",  # または "gpt-4"
            messages=[
                {"role": "system", "content": "あなたは親切なアシスタントです。"},
                {"role": "user", "content": user_input},
            ],
            max_tokens=500,
            temperature=0.7)
            response_text = response.choices[0].message.content
            ChatLog.objects.create(
                user_input = user_input,
                gpt_response  = response_text,
                created_at = datetime.now(pytz.timezone('Asia/Tokyo'))
            )
        except Exception as e:
            response_text = f"エラーが発生しました: {e}"

        return self.render_to_response(self.get_context_data(form=form, response_text=response_text))

