# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Channel
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
@login_required
def livetv(request):
    posts = Channel.objects.all().order_by('name')
    return render(request, 'blog/livetv.html', {'posts': posts})