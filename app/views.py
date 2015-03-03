"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django.shortcuts import Http404

from models import Category, Element
from datetime import datetime

def home(request):
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'categories': Category.objects.all(),
        })
    )

def all_elements(request):
    return render(
        request,
        'app/all.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'elements': Element.objects.all(),
            'categories': Category.objects.all(),
        })
    )

def all_categories(request):
    return render(
        request,
        'app/all-categories.html',
        context_instance = RequestContext(request,
        {
          'title': '',
          'year': datetime.now().year,
          'categories': Category.objects.all()  
        })
    )

def category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist():
        raise Http404

    return render(
        request,
        'app/category.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'name': category.name,
            'elements': category.element_set.all(),
            'categories': Category.objects.all()
        })
    )