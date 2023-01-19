from django.shortcuts import render
from .models import Mbti

# Create your views here.
def index(request):
    context = {}
    return render(request, 'articles/index.html', context)

def result(request):
    mbti = Mbti().alphabet
    
    first = {}
    second = {}
    third = {}
    fourth = {}
    result = ''
    
    first['I'] = mbti.count('I')
    first['E'] = mbti.count('E')
    result += max(first.keys())
    
    second['S'] = mbti.count('S')
    second['N'] = mbti.count('N')
    result += max(second.keys())
    
    third['T'] = mbti.count('T')
    third['F'] = mbti.count('F')
    result += max(third.keys())

    fourth['P'] = mbti.count('P')
    fourth['J'] = mbti.count('J')
    result += max(fourth.keys())
    
    context = {
        'result': result,
    }
    
    return render(request, 'articles/result.html', context)