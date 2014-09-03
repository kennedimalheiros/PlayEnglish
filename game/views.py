from django.shortcuts import render
from models import Player, SentenceUnlock


def home(request):
    dados = {}
    player = Player.objects.get(user=request.user)
    dados['list_words'] = SentenceUnlock.objects.filter(player=player)
    dados['player'] = player
    return render(request, 'play.html', dados)


def get_new_sentence(request):
    dados = {}
    player = Player.objects.get(user=request.user)

    if player.new_sentence:
        dados['message'] = 'Palavra adicionada'
    else:
        'Jogue um pouco mais'
    return render(request, 'play.html', dados)
