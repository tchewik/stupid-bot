from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'tchotchka_with_bot.views.home', name='home'),
    url(r'^conversation$', 'tchotchka_with_bot.views.conversation', name='conversation'),
    url(r'^app/', include('social.apps.django_app.urls', namespace='social'))
]