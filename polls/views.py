from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

from .models import Question,Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    # template = loader.get_template('polls/index.html') #另一种输出方法1
    context = {
        'latest_question_list': latest_question_list,
    }
    # output = ' , '.join([q.question_text for q in latest_question_list]) #另一种输出方法2
    # return HttpResponse(template.render(context, request))  #另一种输出方法1
    return render(request, 'polls/index.html', context) #另一种输出方法3

# 详情页面
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You are looking at question %s ." % question_id)

# 结果页面
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    return render(request, 'polls/results.html', {'question': question})

# 投票页面
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

