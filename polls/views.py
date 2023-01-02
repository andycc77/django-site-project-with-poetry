from django.shortcuts import render
from .models import TB_1


# Create your views here.
def index(request):
    user_data = TB_1.objects.get(name="Adam")
    return render(request, './polls/index.html', {'user_data': user_data})
