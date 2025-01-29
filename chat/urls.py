from django.urls import path
from .views import chat_view, get_messages, send_message

urlpatterns = [
    path("", chat_view, name="chat"),
    path("get_messages/", get_messages, name="get_messages"),
    path("send_message/", send_message, name="send_message"),
]
