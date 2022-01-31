import re
from django.http import JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Idea,Devtool

from .forms import DevForm, IdeaForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def idea_list(request):
    
    post=Idea.objects.all()
    post=Idea.objects.order_by('-id')
    ctx={'posts':post}
    return render(request,template_name='list.html',context=ctx)


def idea_detail(request,pk):
    
    post=get_object_or_404(Idea,id=pk)
    ctx={'post':post}
    
    return render(request,template_name='detail.html',context=ctx)

def idea_create(request):

    if request.method=="POST":
        form=IdeaForm(request.POST,request.FILES)
        
        if form.is_valid():
            post=form.save()
            return redirect('Idea:list')

    else:
        form=IdeaForm()
        ctx={'form':form}
        return render(request,template_name='create.html',context=ctx)


def idea_fix(request,pk):
     post=get_object_or_404(Idea,id=pk)
     if request.method=="POST":
        form=IdeaForm(request.POST,request.FILES,instance=post)
        
        if form.is_valid():
            post=form.save()
            return redirect('Idea:detail',pk)

     else:
        form=IdeaForm(instance=post)
        ctx={'form':form}
        return render(request,template_name='create.html',context=ctx)

def idea_delete(request,pk):
    post=get_object_or_404(Idea,id=pk)
    post.delete()
    return redirect("Idea:list")

def dev_list(request):
    post=Devtool.objects.all()
    ctx={"post":post}
    return render(request,template_name='dev_list.html',context=ctx)


def dev_create(request):

    if request.method=="POST":
        form=DevForm(request.POST)
        if form.is_valid:
            post=form.save()
            return redirect('Idea:dev_list')

    else:
        form=DevForm()
        ctx={'form':form}
        return render(request,template_name='create.html',context=ctx)

def dev_delete(request,pk):
    post=get_object_or_404(Devtool,id=pk)
    post.delete()
    return redirect("Idea:dev_list")

def dev_fix(request,pk):
    post=get_object_or_404(Devtool,id=pk)
    if request.method=="POST":
        form=DevForm(request.POST,instance=post)
        if form.is_valid:
            post=form.save()
            return redirect('Idea:dev_detail',pk)

    else:
        form=DevForm(instance=post)
        ctx={'form':form}
        return render(request,template_name='create.html',context=ctx)

def dev_detail(request,pk):

    post=get_object_or_404(Devtool,id=pk)
    
    idea=Idea.objects.filter(devtool=post)
    print(post.title)
    print(post)
    ctx={'post':post,
    'idea':idea}
    return render(request,template_name="dev_detail.html",context=ctx)
import json
@csrf_exempt
def button_ajax(request):
    req=json.loads(request.body)

    post_id=req['id']
    button_type=req['type']

    post=Idea.objects.get(id=post_id)

    if button_type== 'plus':
        post.like+=1 
    else:
        post.like-=1

    post.save()

    return JsonResponse({'id':post_id,'type':button_type})