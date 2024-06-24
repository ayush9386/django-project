from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import get_user_detail,display, edit, delete_data
from .models import user_detail
# Create your views here.
def create(request):
    user_form = get_user_detail()
    if request.method == 'POST':
        user_form = get_user_detail(request.POST)
        #print(user_form)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse('your detail has been captured')
    dict = {'form' : user_form}
    return render(request, 'user_detail.html', dict)

def read(request):
    form = display()
    if request.method  == 'POST':
        form_in =display(request.POST)
        if form_in.is_valid():
            name = form_in.cleaned_data['name']
            try:
                user_obj = user_detail.objects.get(name=name)
                user_details = {
                    'name': user_obj.name,
                    'phone_number': user_obj.phone_num,
                    'no_of_people': user_obj.no_of_people,
                }
                return render(request , 'display_details.html', user_details)
                #return HttpResponse(user_details['name'])
            except:
                return HttpResponse('user not found')
    dict = {'form' : form}
    return render(request ,'display_user_detail.html' , dict )

def update(request):
    #return HttpResponse('you can edit here')
    form = edit()
    if request.method == 'POST':
        form = edit(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            no_of_people_new  = form.cleaned_data['no_of_people']
            try:
                print('in try block')
                user_obj = user_detail.objects.get(name = name)
                print(user_obj.name)
                old_no_of_people =user_obj.no_of_people
                print(old_no_of_people)
                user_obj.no_of_people = no_of_people_new
                user_obj.save()
                return HttpResponse('NO OF PEOPLE CHANGED FROM ' + str(old_no_of_people) + ' to ' + str(no_of_people_new) )
            except:
                return HttpResponse('enter the correct name')

    dict = {'form' : form}
    return render(request, 'edit_seats.html' , dict)

def delete(request):
    form = delete_data()
    dict = {'form': form } 
    print(345)
    if request.method == 'POST':
        form  = delete_data(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            try:
                obj = user_detail.objects.get(name = name)
                obj.delete()
                return HttpResponse(f'your reservation is canceled for name {str(name)}')
            except:
                return HttpResponse('enter correct name')

    return render(request , 'delete_form.html' , dict)

