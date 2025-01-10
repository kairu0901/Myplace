from django.urls import path
from .views import ChatView

app_name = 'kairu_chat'
urlpatterns = [
    path("kairu_chat/", ChatView.as_view(), name="chat"),
]
