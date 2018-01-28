from django.db import models


class Survey(models.Model):
    name = models.CharField('Araştırma Adı', max_length=100)
    active = models.BooleanField('Aktif mi?', null=False, blank=False, default=False)
    created_at = models.DateTimeField('Oluşturulma Tarihi', null=True, blank=True, auto_now=True)
    updated_at = models.DateTimeField('Güncellenme Tarihi', null=True, blank=True, auto_now_add=True)

    class Meta:
        verbose_name = 'Araştırma'
        verbose_name_plural = 'Araştırmalar'

    def __str__(self):
        return str(self.name)

class Question(models.Model):
        survey=models.ForeignKey(Survey,verbose_name='Araştırma',null=False, blank=False)
        title = models.CharField('Soru', max_length=255)
        choice_one = models.CharField('Seçenek-1', max_length=255)
        choice_two = models.CharField('Seçenek-2', max_length=255)
        choice_three = models.CharField('Seçenek-3', max_length=255)
        choice_four = models.CharField('Seçenek-4', max_length=255)

        class Meta:
            verbose_name = 'Soru'
            verbose_name_plural = 'Sorular'

        def __str__(self):
            return str(self.title)