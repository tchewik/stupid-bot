from django.shortcuts import render
from .models import Bot
from .forms import MsgForm
from . import tchebot


def home(request):
    #  cleans db every time you open homepage
    if request.user.is_authenticated():
        Bot.objects.filter(guy_id=request.user).delete()
    return render(request, 'tchotchka_with_bot/home.html')

def conversation(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = MsgForm(request.POST)
            if form.is_valid():
                replic = form.save(commit=False)
                replic.guy = request.user
                replic.rep = request.POST.get('rep', '0')
                replic.ans = tchebot.answer(replic)
                replic.save()
                print("<<<REPLIC: ", replic.rep)
                print("<<<ANSWER: ", replic.ans)

        form = MsgForm()
        replics = Bot.objects.filter(guy_id=request.user)
        return render(request, 'tchotchka_with_bot/conversation.html', {'replics': replics, 'form': form})
    return render(request, 'tchotchka_with_bot/log_in.html')