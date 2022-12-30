from django.shortcuts import render


# Create your views here.
def index(request):
    args = {
        'name': 'John',
        'age': 21,
        'vip': True
    }
    return render(request, './polls/index.html', args)
