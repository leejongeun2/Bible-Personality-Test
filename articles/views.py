from django.shortcuts import render
from .models import Mbti

# Create your views here.
def index(request):
    context = {}
    return render(request, 'articles/index.html', context)

def result(request):
    mbti = Mbti.objects.get(id=1).alphabet
    
    first = {}
    second = {}
    third = {}
    fourth = {}
    result = ''
    
    first['I'] = mbti.count('I')
    first['E'] = mbti.count('E')
    key = max(first, key=first.get)
    result += key
    
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