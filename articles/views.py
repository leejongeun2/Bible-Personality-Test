from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Mbti, Type, Question
from django.core import serializers

# Create your views here.
def index(request):
    context = {}
    return render(request, 'articles/index.html', context)

# @csrf_exempt
# def question(request):
#     received_message = request.POST.get('') 
#     send_message = {'send_data' : 'I received'}
#     return JsonResponse(send_message)

@csrf_exempt
def question(request):
    question = Question.objects.get(pk=1)
    # pk = request.POST.get('pk')
    # # for question in question_list:
    # #     pk = question.pk
    # #     question_pk = request.POST.get('pk', None)
    
    # # try:
    # question = get_object_or_404(Question, pk=pk)
    # context = {
    #     'question': question,
    # }
    # return JsonResponse(context)
    context = {
        'question_pk': question.pk,
        'question': question.question,
        'question_ans1': question.answer1,
        'question_ans2': question.answer2,
    }
    return render(request, 'articles/questiontest.html', context)

    # except:
        # return render(request, 'articles/result.html')
        
@csrf_exempt
def nextPage(request):
    pk = request.POST.get('pk')
    pk=1
    pk = int(pk) + 1
    question = Question.objects.get(pk=pk)
    data = {
        'question_pk': question.pk,
        'question': question.question,
        'question_ans1': question.answer1,
        'question_ans2': question.answer2,
    }
    return JsonResponse(data)

def result(request):
    mbti = Mbti.objects.get(id=1).alphabet # model에서 id=1 alphabet 컬럼에서 데이터 가져오기(ex:'IEESSNTTFJPP')
    types = Type.objects.all()
    
    first = {}
    second = {}
    third = {}
    fourth = {}
    result = ''
    
    first['I'] = mbti.count('I') # first['I'] == key / mbti.count('I') == value / ex: {'I': 1, 'E': 2}
    first['E'] = mbti.count('E') # first['E'] == key / mbti.count('E') == value / ex: {'I': 1, 'E': 2}
    key = max(first, key=first.get) # key = max(dict_name, key=dict_name.get)
    result += key # result += max_value를 가지는 key(ex: 'E')
    
    second['S'] = mbti.count('S')
    second['N'] = mbti.count('N')
    key = max(second, key=second.get)
    result += key
    
    third['T'] = mbti.count('T')
    third['F'] = mbti.count('F')
    key = max(third, key=third.get)
    result += key

    fourth['P'] = mbti.count('P')
    fourth['J'] = mbti.count('J')
    key = max(fourth, key=fourth.get)
    result += key
    
    for type in types:
        if type.mbti == result:
            result_type = Type.objects.get(mbti=type.mbti)
            break
    
    context = {
        # 'result': result,
        'result_type': result_type,
    }
    
    return render(request, 'articles/result.html', context)