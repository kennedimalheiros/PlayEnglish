from django.shortcuts import render
from models import Player, Sentence
import random


def home(request, dados={}):
    player = Player.objects.get(user=request.user)
    dados['list_words'] = player.sentences_unlocked.all()
    dados['player'] = player
    return render(request, 'game.html', dados)


def get_new_sentence(request):
    dados = {}
    player = Player.objects.get(user=request.user)

    if player.can_new_sentence > 0:
        player.add_sentence
        dados['message'] = 'Palavra adicionada'
    else:
        dados['message'] = 'Jogue um pouco mais'
    return home(request, dados)


def play(request, dados={}):
    dados['option'] = random.choice(
        Player.objects.get(user=request.user).sentences_unlocked.all())
    return render(request, 'play.html', dados)


def correct(request, id):
    dados = {}
    player = Player.objects.get(user=request.user)
    sentence = Sentence.objects.get(id=id)
    answer = request.POST.get('answer')
    if answer == sentence.translate_text:
        player.add_point
        dados['message'] = 'Congratulations'
    else:
        dados['message'] = 'Fail'

    return play(request, dados)
