from django.http import HttpResponse
from django.urls import path

def hello(request):
    return HttpResponse("""
        <h1>мой первый сайт</h1>
        <p>Здесь будет мой проект на django</p>
        <a href="/about">о проекте</>
        <br>
        <a href="/contacts">контакты</>
""")

def about(request):
    return HttpResponse("""
        <h1>about</h1>
        <p>Здесь будет мой проект на django</p>
        <a href="/">начало</>
        <br>
        <a href="/contacts">контакты</>
""")

def contacts(request):
    return HttpResponse("""
        <h1>contacts</h1>
        <p>Здесь будет мой проект на django</p>
        <a href="/about">о проекте</>
        <br>
        <a href="/">начало</>
""")


urlpatterns = [
    path("",hello),
    path("about/",about),
    path("contacts/",contacts)
    
]
