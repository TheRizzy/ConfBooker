from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.

def main_page(request):
    return render(request, 'main-page.html')


class MainPage(View):
    @staticmethod
    def get(request):
        return render(request, 'main-page.html')