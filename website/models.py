from django.db import models


class Entry(models.Model):
    id = models.UUIDField(primary_key=True)
    word = models.CharField(max_length=200, unique=True)
    simplified_word = models.CharField(max_length=200)
    language = models.CharField(max_length=5)
    audio_url = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word


class Meaning(models.Model):
    id = models.UUIDField(primary_key=True)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    language_from = models.CharField(max_length=5)
    language_to = models.CharField(max_length=5)
    meaning_text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.entry.word} {self.meaning_text}'


class LookupCount(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE, primary_key=True)
    lookup_count = models.IntegerField()

    def __str__(self):
        return f'{self.entry.word} {self.lookup_count}'


class LookupCountDaily(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE, primary_key=True)
    lookup_count = models.IntegerField()
    day_number = models.IntegerField(default=0)  # Number of days since the epoch

    def __str__(self):
        return f'{self.entry.word} {self.lookup_count} {self.day_number}'
