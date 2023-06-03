from django.shortcuts import render
from . models import Post 

# Create your views here.
def blog(request):
    posts = Post.objects.all()

    #post = { 'posts':posts}
    return render(request, 'blog/blog.html', {'posts':posts})
    #return render(request, 'services/services.html', {'services': services})