from django.shortcuts import render
from django.shortcuts import render, redirect

from insta.form import InstaForm
from .models import Post
# Create your views here.

def list_insta(request):
    posts=Post.objects.all()

    ctx={"posts":posts}

    return render(request,template_name='list.html',context=ctx)


def create_insta(request):
    
    if request.method=='POST':
        form=InstaForm(request.POST)
        if form.is_valid():
            form=form.save()
            return redirect("insta:list_insta")

    else:
        form=InstaForm()
        ctx={'form':form}

        return render(request,template_name='create_form.html',context=ctx)

        