from django.shortcuts import render

def hello_world_html(request):
    return render(request, 'hello.html')

