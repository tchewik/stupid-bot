from django.shortcuts import render
from .models import Bot
from .forms import MsgForm
from . import tchebot
from django.contrib import auth


def home(request):
    if request.user.is_authenticated():
        userinfo = {'name': request.user.username,
                    'firstname': request.user.first_name,
                    'lastname': request.user.last_name,
                    'joined': request.user.date_joined
                    }

        return render(request, 'tchotchka_with_bot/home.html', {'userinfo': userinfo})
    return render(request, 'tchotchka_with_bot/home.html')


def conversation(request):
    if request.user.is_authenticated():
        userinfo = {'name': request.user.username,
                    'firstname': request.user.first_name,
                    'lastname': request.user.last_name,
                    'joined': request.user.date_joined
                    }
        if request.method == "POST":
            form = MsgForm(request.POST)
            if form.is_valid():
                replic = form.save(commit=False)
                replic.guy = request.user
                replic.rep = request.POST.get('rep', '0')
                ans_list = Bot.objects.filter(guy_id=request.user).values_list('ans')
                used_replics = [used_replic[0] for used_replic in ans_list]
                replic.ans = tchebot.reply(replic.rep, used_replics)
                replic.save()

        form = MsgForm()
        replics = Bot.objects.filter(guy_id=request.user)
        return render(request, 'tchotchka_with_bot/conversation.html', {'userinfo': userinfo, 'replics': replics, 'form': form})
    return render(request, 'tchotchka_with_bot/log_in.html')


def profile(request):
    if request.user.is_authenticated():
        userinfo = {'name': request.user.username,
                    'firstname': request.user.first_name,
                    'lastname': request.user.last_name,
                    'joined': request.user.date_joined
                    }
        return render(request, 'tchotchka_with_bot/profile.html', {'userinfo': userinfo})


def logout(request):
    #  cleans db every time you log out
    Bot.objects.filter(guy_id=request.user).delete()
    auth.logout(request)
    return home(request)

