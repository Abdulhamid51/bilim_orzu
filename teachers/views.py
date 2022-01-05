from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from .models import *
# Create your views here.


class TeamView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        data = {
            'teachers':teachers,
        }
        return render(request, 'team.html', data)



def brithday_view(request):
    days = BrithDays.objects.all()
    context = {
        'days':days
    }
    return context

def contact(request):
    return render(request, 'contact.html')

def get_contact(request):
    name = request.GET.get('name')
    surname = request.GET.get('surname')
    telnum = request.GET.get('phone')
    if name and surname and telnum:
        Contact.objects.create(
            name=name,
            surname=surname,
            tel_number=telnum
        )
        return JsonResponse({'status':'OK'})
    else:
        return JsonResponse({'status':'ERROR'})