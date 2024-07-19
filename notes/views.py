from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView, DetailView


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
        
class NotesDetailsView(DetailView):
    model = Notes
    context_object_name = 'note'
