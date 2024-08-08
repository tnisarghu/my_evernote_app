from rest_framework import viewsets, permissions
from .models import Note
from .serializers import NoteSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

@login_required
def index(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'base.html', {'notes': notes})