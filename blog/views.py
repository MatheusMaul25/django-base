# from django.http import HttpResponse


# def blog(request):
#     return HttpResponse('blog do app 1')

# def exemplo(request):
#     return HttpResponse('exemplo do app 1')

from django.shortcuts import render
from blog.data import posts
from django.http import Http404
def blog(request):

    context = {
        'text': 'Estamos no blog',
        'title': 'Blog',
        'posts': posts,
        }

    return render(
        request, 
        'blog/index.html',
        context, 
        )

def post(request, post_id):

    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
        
    if found_post is None:
        raise Http404('Post não existe')

    context = {
        'title': found_post['title'],
        'post': found_post,
        }

    return render(
        request, 
        'blog/post.html',
        context, 
        )


def exemplo(request):

    context = {
        'text': 'Estamos no exemplo do blog',
        'title': 'Exemplo do blog'}

    return render(
        request, 
        'blog/exemplo.html',
        context,
        )