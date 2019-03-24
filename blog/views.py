from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def author_list(request):
    return render(request, 'blog/author_list.html', {})
