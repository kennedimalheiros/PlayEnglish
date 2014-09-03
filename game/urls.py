from django.conf.urls import patterns, url

urlpatterns = patterns(
    'game.views',
    url(r'^$', 'home', name='game_home'),
    url(r'^get_new_sentence/$', 'get_new_sentence', name='get_new_sentence'),
)
