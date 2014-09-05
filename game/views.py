# encoding: utf8
from django.shortcuts import render
from models import Player, Sentence, Language
import random
from utils import remover_acentos


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
    player = Player.objects.get(user=request.user)
    dados['player'] = player
    dados['option'] = random.choice(
        player.sentences_unlocked.all())
    return render(request, 'play.html', dados)


def correct(request, id):
    dados = {}
    player = Player.objects.get(user=request.user)
    sentence = Sentence.objects.get(id=id)
    answer = request.POST.get('answer')
    if answer.lower() in \
            sentence.translate_text.lower().replace(',', ' ').split():
        player.add_point
        dados['status'] = True
    else:
        dados['status'] = False

    return play(request, dados)


def gera_nova_lista(request):
    f = open('list_words.txt', 'r')
    string = ''
    lang = Language.objects.get(id=1)
    for i in f.readlines():
        string = i.split()
        sent = Sentence(
            language=lang, original_text=string[1],
            translate_text=string[3], level=1)
        sent.save()
