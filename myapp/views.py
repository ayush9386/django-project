from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from .forms import DemoForm
# Create your views here.
def home(request):
    path = request.path
    return HttpResponse(path,content_type = 'text/html', charset = 'utf-8' )

def info(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    
    response = HttpResponse()
    response.headers['age'] = 20
    
    msg = f"""<br>
    <br>path : {path}
    <br>address: {address}
    <br>scheme: {scheme}
    <br>method:{method}
    <br>user_agent: {user_agent}
    <br>path_info:{path_info}
    <br>response_header:{response.headers }
    """
    return HttpResponse(msg, content_type = 'text/html', charset = 'utf-8' )

def get_info_url(request, name, id):
    resp = f'name we picked from url is:{name} <br>  his id is:{id}'
    return  HttpResponse(resp)

def get_info_query(request):
    name = request.GET['name'] 
    id = request.GET['id']
    return HttpResponse(f'name using query: {name} <br> his id is: {id}')

def showform(request): 
    
    return render(request, "name_form.html")

def get_form_details(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
    return HttpResponse(f'id is {id} <br>  name is {name}')

def dummy_view(request):
    return HttpResponse('we are in a dummy view')

def user_view(request):
    return HttpResponseRedirect(reverse('dummy_view' , args=()))

def admin_view(request):
    return HttpResponseRedirect(reverse('dummy_view', args=()))

