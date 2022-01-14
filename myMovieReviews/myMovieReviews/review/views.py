from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm


def movie_list(request):
    posts=Post.objects.all()
    ctx={'posts':posts}
    return render(request,template_name='list.html',context=ctx)
# Create your views here.

def movie_create(request):
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save()
            return redirect('reviews:review')
    else:
        form=PostForm()
        ctx={'form':form}
        return render(request,template_name='create.html',context=ctx)

def movie_detail(request,pk):
    post=get_object_or_404(Post,id=pk)
    ctx={'post':post}

    return render(request,template_name='detail.html',context=ctx)

def movie_update(request,pk):
    post=get_object_or_404(Post,id=pk)
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            
            post=form.save()
            return redirect('reviews:detail',pk)
    else:
        
        form=PostForm(instance=post)
        ctx={'form':form}
        return render(request,template_name='create.html',context=ctx)

def movie_delete(request,pk):
    post=get_object_or_404(Post,id=pk)
    post.delete()
    return redirect('reviews:review')