from django.shortcuts import render
from .models import Notes
from django.http import Http404


def list(request):
    try:
        all_notes = Notes.objects.all()
    except Notes.DoesNotExist:
        raise Http404('No notes found')
        
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, note_id):
    try:
        note = Notes.objects.get(id=note_id)
    except Notes.DoesNotExist:
        raise Http404('Note not found')
    
    return render(request, 'notes/notes_detail.html', {'note': note})