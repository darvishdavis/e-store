from django.db import models

# Create your models here.

class SearchBox(models.Model):
    value = models.CharField(max_length=20, null=True)
    date_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'searchbox'

    def __str__(self):
        return '{}' .format(self.value)
