from django.shortcuts import render
from django.http import JsonResponse
from .reply_factory import generate_bot_responses

def chat(request):
    if not request.session.session_key:
        request.session.create()

    if request.method == 'POST':
        user_message = request.POST.get('message')
        if user_message:
            bot_responses = generate_bot_responses(user_message, request.session)
            return JsonResponse({'responses': bot_responses})

    return render(request, 'chat.html')

 
