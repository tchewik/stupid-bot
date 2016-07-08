from django.shortcuts import render
from .models import Bot
from .forms import MsgForm
from . import tchebot


def home(request):
    replics = Bot.objects.filter()
    return render(request, 'tchotchka_with_bot/home.html', {'replics': replics})

def conversation(request):
    if request.method == "POST":
        form = MsgForm(request.POST)
        if form.is_valid():
            replic = form.save(commit=False)
            replic.rep = request.POST.get('rep', '0')
            replic.save()
            print("<<<REPLIC: ", replic.rep)
            replic.ans = tchebot.answer(replic)
            print("<<<ANSWER: ", replic.ans)
        return render(request, 'tchotchka_with_bot/conversation.html', {'replics': replic, 'form': MsgForm})
    else:
        form = MsgForm()
        replics = Bot.objects.filter()
        print(">>>", replics)
        return render(request, 'tchotchka_with_bot/conversation.html', {'replics': replics, 'form': form})