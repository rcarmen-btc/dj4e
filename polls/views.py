from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.http import Http404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = """
    
    You're looking at the results of question %s."""
    return render(request, 'polls/res.html')
   # return HttpResponse(response % question_id)


def vote(request, question_id):
    return render(request, 'polls/res.html')


def owner(request):
    return HttpResponse("Hello, 12c7c68e world. 496ad113 is the polls index.")
