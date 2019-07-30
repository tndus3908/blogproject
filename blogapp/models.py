from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title # 타이틀이 바로 뜰 수 있도록

    def summary(self):
        return self.body[:100]