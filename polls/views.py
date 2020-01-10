from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.http import Http404
# Create your views here.


# 使用通用视图ListView（作为父类被继承） 显示一个对象的列表
class IndexView(generic.ListView):
    # 指定模板名
    template_name = 'polls/index.html'
    # 上下文变量
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


# 使用通用视图DetailView（作为父类被继承）显示特定类型对象的详细页面
class DetailView(generic.DetailView):
    # 每一种通用视图都需要知道它要作用在哪个模型上，这通过model属性提供。
    model = Question
    # 指定模板名
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    # 指定模板名
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
