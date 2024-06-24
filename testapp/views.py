from django.shortcuts import render
from django.http import HttpResponse , request
from .forms import InputForm, LogForm
# Create your views here.

def form_view(request):
    form = InputForm()
    context = {"form" : form}
    return render(request,"home.html", context)


def form_view_post(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            #print('here')
            form.save()
    context = {"form" : form}
    return render(request,"home.html", context)

def about(request):
    about_content = {
        'about':'Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day.',
        'food' : 'salad'
                }
    return render(request, 'about.html', {'content':about_content})

def menu(request):
    newmenu = {'mains':[
        {'name' : 'falafal', 'price': '12'},
        {'name' : 'shawrma', 'price': '15'},
        {'name' : 'gyro', 'price': '10'},
               ]}
    return render(request , 'menu.html',{'content': newmenu})


from .models import Menu
def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu' : newmenu}
    return render(request,'menu_card.html', newmenu_dict)

def home_extend(request):
    return render(request ,'home_extend.html')
def about_extend(request):
    return render(request ,'about_extend.html')
def menu_extend(request):
    return render(request ,'menu_extend.html')