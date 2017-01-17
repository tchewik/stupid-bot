from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'tchotchka_with_bot.views.home', name='home'),
    url(r'^conversation$', 'tchotchka_with_bot.views.conversation', name='conversation'),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^accounts/profile', 'tchotchka_with_bot.views.profile', name='profile'),
    url(r'^logout', 'tchotchka_with_bot.views.logout', name='logout')
]