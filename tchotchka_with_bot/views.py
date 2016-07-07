from django.shortcuts import render
from .models import Bot
from .forms import MsgForm


def home(request):
    replics = Bot.objects.filter()
    return render(request, 'tchotchka_with_bot/home.html', {'replics': replics})

def conversation(request):
    form = MsgForm()
    if request.method == "POST":
        
        return render(request, 'tchotchka_with_bot/conversation.html', {'replics': None, 'form': form})
    else:
        replics = Bot.objects.filter()
        print(">>>", replics)
        return render(request, 'tchotchka_with_bot/conversation.html', {'replics': replics, 'form': form})