# encoding: utf8
from django.db import models
from django.contrib.auth.admin import User


class Language(models.Model):
    language_name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.language_name


class Sentence(models.Model):
    language = models.ForeignKey(Language)
    original_text = models.TextField()
    translate_text = models.TextField()
    level = models.IntegerField()

    def __unicode__(self):
        return self.language.language_name + '/ ' +\
            self.original_text + '/' + self.translate_text


class Player(models.Model):
    user = models.OneToOneField(User)
    level = models.IntegerField()
    points = models.IntegerField()
    sentences_unlocked = models.ManyToManyField(Sentence)

    def __unicode__(self):
        return self.user.username

    @property
    def get_level(self):
        if self.points <= 100:
            return 'Begginer'
        elif self.level <= 300:
            return 'Junior'
        else:
            return 'Veteran'

    @property
    def can_new_sentence(self):
        max_words = 0
        qtd_have = self.sentences_unlocked.count()

        if self.level == 1:
            max_words = self.points / 5
        elif self.level == 2:
            max_words = self.points / 10
        else:
            max_words = self.points / 20

        return max_words - qtd_have

    @property
    def add_sentence(self):
        list_sent = Sentence.objects.exclude(
            id__in=self.sentences_unlocked.values_list('id', flat=True))
        self.sentences_unlocked.add(list_sent[0])
        self.save()

    @property
    def add_point(self):
        if self.get_level == 'Begginer':
            self.points += 2
        elif self.get_level == 'Junior':
            self.points += 4
        else:
            self.points += 9

        self.save()
