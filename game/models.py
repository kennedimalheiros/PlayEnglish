from django.db import models
from django.contrib.auth.admin import User


class Player(models.Model):
    user = models.ForeignKey(User)
    level = models.IntegerField()
    points = models.IntegerField()

    def __unicode__(self):
        return self.user.username

    @property
    def get_level(self):
        if self.level == 1:
            return 'Begginer'
        elif self.level == 2:
            return 'Junior'
        else:
            return 'Veteran'

    @property
    def new_sentence(self):
        max_words = 0
        qtd_have = SentenceUnlock.objects.filter(player=self).count()
        if self.level == 1:
            max_words = self.points / 5
        if max_words - qtd_have > 0:
            new_word_for_player(self)
            return True
        else:
            return False

    @property
    def set_new_sentence(self, word):
        obj = SentenceUnlock(self, word)
        obj.save()


class Language(models.Model):
    language_name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.language_name


class BankOfSentences(models.Model):
    language = models.ForeignKey(Language)
    original_text = models.TextField()
    translate_text = models.TextField()
    level = models.IntegerField()

    def __unicode__(self):
        return self.language.language_name + '/ ' +\
            self.original_text + '/' + self.translate_text


class SentenceUnlock(models.Model):
    player = models.ForeignKey(Player)
    sentence = models.ForeignKey(BankOfSentences)


def new_word_for_player(player):
    list_sentence_have = SentenceUnlock.objects.filter(player=player)
    new_word = BankOfSentences.objects.exclude(
        id__in=list_sentence_have.values_list('id', flat=True))[0]
    player.set_new_sentence(new_word)
