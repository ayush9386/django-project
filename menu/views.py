from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse
# Create your views here.
def menu_num(request, menu_id):
    dict ={
        '1': "pasta",
        '2': "noodles",
        '3': "chicken"
    }
    if menu_id not in dict.keys():
        return HttpResponseNotFound('404: page not found using django.http , HttpResponseNotFound')
    res = dict[menu_id]

    return HttpResponse(f'the food you ordered is {res}')

def index(request):
    #print(reverse('name_menu_num', args=(1,)))
    #print(reverse('menu_index'))
    return HttpResponseRedirect(reverse('menu:dummy_page', args=()))

def dummy(request):
    return HttpResponse('this is a dummy page in menu app')

def redirect_other_app(request):
    return HttpResponseRedirect(reverse('myapp:home', args=()))