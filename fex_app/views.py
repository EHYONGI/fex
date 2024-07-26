from django.shortcuts import render
import random

# Create your views here.
def root(request):
    return render(request, 'root.html')

def index(request):
    return render(request, 'index.html')

def lotto(request):

    luckynum = random.sample(range(1, 46), 6)

    context = {
        'luckynum': luckynum
    }

    return render(request, 'lotto.html', context)

def lunch(request):

    hubo = ['한식', '양식', '중식', '일식', '매운거', '안매운거']

    pick = random.choice(hubo)

    context = {
        'pick': pick
    }

    return render(request, 'lunch.html', context)

def dinner(request):
        
    hubo = ['한식', '양식', '중식', '일식', '매운거', '안매운거']

    pick = random.choice(hubo)

    context = {
        'pick': pick
    }

    return render(request, 'dinner.html', context)
