from django.shortcuts import render
from .models import Bot
from .forms import MsgForm
from . import tchebot


def home(request):
    Bot.objects.filter().delete()
    return render(request, 'tchotchka_with_bot/home.html')

def conversation(request):
    if request.method == "POST":
        form = MsgForm(request.POST)
        if form.is_valid():
            replic = form.save(commit=False)
            replic.rep = request.POST.get('rep', '0')
            replic.ans = tchebot.answer(replic)
            replic.save()
            print("<<<REPLIC: ", replic.rep)
            print("<<<ANSWER: ", replic.ans)

    form = MsgForm()
    replics = Bot.objects.filter()
    return render(request, 'tchotchka_with_bot/conversation.html', {'replics': replics, 'form': form})