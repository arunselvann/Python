from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from . import models
from . import forms
from comments.models import comment
from django.contrib.contenttypes.models import ContentType
from comments.forms import CommentForm
from django.contrib.auth.decorators import login_required


def posts_list(request):
    queryset_list = models.post.objects.active()
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
                                             Q(title__icontains=query) |
                                             Q(content__icontains=query) |
                                             Q(user__first_name__icontains=query) |
                                             Q(user__last_name__icontains=query)
                                             )
    paginator = Paginator(queryset_list, 1)
    page = request.GET.get('page')
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        query_set = paginator.page(1)
    except EmptyPage:
        query_set = paginator.page(paginator.num_pages)

    context = {
        'object_list': query_set
    }
    return render(request, 'posts/list.html', context)

@login_required
def posts_detail(request, slug=None):
    instance = get_object_or_404(models.post, slug=slug)
    comments = comment.objects.filter_by_instance(instance)
    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('content')
        new_comment, created = comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data
        )

    context = {
        'instance': instance,
        'comments': comments,
        'commentform': form
    }
    return render(request, 'posts/post_detail.html', context)


def posts_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = forms.PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect(instance.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'posts/new_post.html', context)


def posts_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(models.post, slug=slug)
    form = forms.PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute_url())
    context = {
        'form': form,
        'instance': instance
    }
    return render(request, 'posts/new_post.html', context)


def posts_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(models.post, slug=slug)
    instance.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('posts:list')
