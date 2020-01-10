from django.contrib import admin
from .models import Choice, Question
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# 创建一个继承admin.ModelAdmin的模型管理类
class QuestionAdmin(admin.ModelAdmin):
    # 字段集合fieldsets中每一个元组的第一个元素是该字段集合的标题
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


# 将QuestionAdmin作为第二个参数传递给admin.site.register()，第一个参数则是Question模型本身
admin.site.register(Question, QuestionAdmin)