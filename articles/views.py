from django.shortcuts import render
from .models import Mbti

# Create your views here.
def index(request):
    context = {}
    return render(request, 'articles/index.html', context)

def question(request):
    return render(request, 'articles/question.html')

def result(request):
    mbti = Mbti.objects.get(id=1).alphabet # model에서 id=1 alphabet 컬럼에서 데이터 가져오기(ex:'IEESSNTTFJPP')
    
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

    
    context = {
        'result': result,
    }
    
    return render(request, 'articles/result.html', context)