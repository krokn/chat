from django.shortcuts import render, redirect


# Create your views here.


def chats_view(request):
    # Список чатов
    chats = [
        {'id': 1, 'name': 'Рабочий чат'},
        {'id': 2, 'name': 'Друзья'},
        {'id': 3, 'name': 'Семья'},
    ]

    # Получаем chat_id из запроса (по умолчанию None)
    chat_id = request.GET.get('chat_id')

    # Выбираем чат по chat_id
    selected_chat = next((chat for chat in chats if str(chat['id']) == chat_id), None)

    # Сообщения в зависимости от выбранного чата
    chat_messages = {
        1: [
            {'sender': 'Алексей', 'text': 'Привет! Как дела?'},
            {'sender': 'Ты', 'text': 'Привет! Все хорошо, спасибо!'},
        ],
        2: [
            {'sender': 'Мария', 'text': 'Когда встречаемся?'},
            {'sender': 'Ты', 'text': 'Давай завтра!'},
        ],
        3: [
            {'sender': 'Мама', 'text': 'Не забудь купить хлеб!'},
            {'sender': 'Ты', 'text': 'Ок, куплю!'},
        ],
    }

    # Получаем сообщения для выбранного чата
    messages = chat_messages.get(int(chat_id), []) if chat_id else []

    return render(request, 'chat/home.html', {
        'chats': chats,
        'selected_chat': selected_chat,
        'messages': messages,
    })


def send_message(request, chat_id):
    if request.method == "POST":
        message_text = request.POST.get("message")
        print(f"Новое сообщение в чат {chat_id}: {message_text}")  # Временно логируем сообщение
    return redirect(f"/chats/home/?chat_id={chat_id}")
