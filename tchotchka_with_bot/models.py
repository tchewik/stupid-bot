from django.db import models


class Bot(models.Model):
    rep = models.CharField("Ваша реплика", max_length=240)
    ans = models.CharField("Елена парирует", max_length=240)

    def __str__(self):
        return self.rep
