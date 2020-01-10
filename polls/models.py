import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    # 问题
    question_text = models.CharField(max_length=200)
    # 发布日期
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    # 外键：每一个Choice关联到一个对应的Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 选项描述
    choice_text = models.CharField(max_length=200)
    # 投票数（默认值设为0）
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
