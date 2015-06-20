from django.shortcuts import render
from models import About_me
from django.views.generic.list import ListView


class About_meListView(ListView):
    model = About_me
    context_object_name = 'about_me'