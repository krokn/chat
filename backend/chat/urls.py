from django.urls import path

from chat.views import chats_view, send_message

urlpatterns = [
    path('home/', chats_view),
    path('send_message/<int:chat_id>/', send_message, name='send_message'),  # Добавляем маршрут
]