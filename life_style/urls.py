from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from life_style.models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],template_name="life_style/home.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name='life_style/post.html'))
]