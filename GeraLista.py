f = open('list_words.txt', 'r')
from game.models import Sentence


sent = Sentence()
for i in f.readlines():
    s = i.split()
    sent(1, s[1], s[3])
    sent.save()
