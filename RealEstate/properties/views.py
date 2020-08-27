import sys

from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail,EmailMessage
from django.db.models import Count




# Create your views here.

from .models import properties, agent, user_request, saved
from django.contrib import messages
from django.db.models import Q


def index(request):
    properties_list=properties.objects.filter(available=True)
    data={'properties':properties_list}
    return render(request,'index.html',data)
def detail(request,id):

    property_detail=properties.objects.get(id=id)
    print(property_detail.agent_name)
    data={'property_data':property_detail}

    return render(request,'detail.html',data)
def contactAgent(request,id):
    if request.method == 'POST':

        f_name=request.POST['name']
        email=request.POST['email']
        msg=request.POST['msg']
        aemail=request.POST['aemail']

        a_id=request.POST['a_id']
        aname = agent.objects.get(id=a_id)
        property_id=properties.objects.get(id=id)

        obj=user_request(property_id=property_id,agent_name=aname,full_name=f_name,email=email,message=msg)
        obj.save()
        try:
            subject='Request from user to see property'

            msg1='Hi, This is '+f_name +' '+msg+'my email id is :'+email
            send_mail(subject=subject, message=msg1,from_email=EMAIL_HOST_USER ,recipient_list=[[aemail]])
            messages.info(request, 'your request submitted ')

        except:
            messages.info(request, 'your request not submitted ')
        return redirect('contactAgent',id)
    property_detail = properties.objects.get(id=id)
    agent_info=agent.objects.get(name=property_detail.agent_name)
    data={'property_data':property_detail,'agent':agent_info}
    return render(request,'agent.html',data)

def search(request):
    text=request.GET.get('text')
    if text:
        properties_list = properties.objects.filter(
            Q(address=text) |
            Q(city=text)|
            Q(zipCode=text)|
            Q(type=text)|
            Q(purpose=text)

        ).distinct()
        if not properties_list:
            messages.info(request, 'No result for your search try to check these')
            return redirect('index')

        data={'properties':properties_list}
        messages.info(request, 'Here is the result matching to your search')
        return render(request,'search.html',data)
    return redirect('index')

def getagents(request):
    if request.method == 'POST':
        aid=request.POST['aid']
        print(aid)
        agent_name = agent.objects.get(name=aid)
        properties_list = properties.objects.filter(agent_name=agent_name)
        print(aid)
        data = {'properties': properties_list}
        if properties_list:
            messages.info(request, "Here " +aid+ "'s listing")

            return render(request,'agent_properties.html',data)
        else:
            messages.info(request, 'Sorry this '+aid+' has no listing')
            redirect('getagents')

    agent_list=agent.objects.all()
    data={'agents':agent_list}
    return render(request,'all_agents.html',data)

def houses(request):
    properties_list = properties.objects.filter(type='house')
    data = {'properties': properties_list}
    if properties_list:
       return render(request, 'houses.html', data)
    else:
        messages.info(request, 'Sorry there are no more houses available ')
        return redirect('index')

def buy(request):
    properties_list = properties.objects.filter(purpose='sale')
    data = {'properties': properties_list}
    if properties_list:
       return render(request, 'buy.html', data)
    else:
        messages.info(request, 'Sorry there are no more houses available for buy check these ')
        return redirect('houses')

def rent(request):
    properties_list = properties.objects.filter(purpose='rent',type='house')
    data = {'properties': properties_list}
    if properties_list:
       return render(request, 'rent.html', data)
    else:
        messages.info(request, 'Sorry there are no more houses available for rent check these ')
        return redirect('houses')

def apartments(request):
    properties_list = properties.objects.filter(type='apartments')
    data = {'properties': properties_list}
    print(properties_list)
    if properties_list:
        return render(request, 'apartments.html', data)
    else:
        messages.info(request, 'Sorry there are no more apartments available check these')
        return redirect('index')

def filtering(request,by):
    if by=='popular':
        popular_property = properties.objects.annotate(requ_count=Count('requested')).filter(requ_count__gt=1)
        data = {'properties': popular_property}
        return render(request, 'index.html', data)


    elif by=='recent':

        properties_list = properties.objects.filter(available=True).order_by('-created')
        data = {'properties': properties_list}
        return render(request, 'index.html', data)
    elif by=='high':
        properties_list = properties.objects.filter(available=True).order_by('-price')
        data = {'properties': properties_list}
        return render(request, 'index.html', data)
    elif by=='low':
        properties_list = properties.objects.filter(available=True).order_by('price')
        data = {'properties': properties_list}
        return render(request, 'index.html', data)

def save_propery(request,username,id):
    u_name=User.objects.get(username=username)
    p_id=properties.objects.get(id=id)
    if saved.objects.filter(user_name=u_name, property_id=p_id):
        return redirect('index')
    else:
        obj=saved(user_name=u_name,property_id=p_id)
        obj.save()
        return redirect('index')
def getsaved(request,username):
    saved_property=saved.objects.filter(user_name=username)
    l1=[]
    for i in saved_property:
        l1.append(i.property_id)
    data = {'properties': set(l1)}
    return render(request, 'saved.html', data)

def remove(request,username,id):

    property=properties.objects.get(id=id)

    obj=saved.objects.filter( Q(user_name=username) & Q(property_id=property))
    obj.delete()
    return redirect('mysaved',username)


