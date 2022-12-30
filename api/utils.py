from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


def getAllnotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)

def getSingleNote(request,pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many = False)
    return Response(serializer.data)

def CreateNote(request):
    data = request.data
    body = data['body']
    title=data['title']
    note = Note.objects.create(title=title,body=body)
    serializer = NoteSerializer(note, many = False)
    return Response(serializer.data)

def UpdateNote(request,pk):
    data = request.data
    title=data['title']
    body = data['body']
    note = Note.objects.filter(id=pk).update(title=title,body=body)
    return Response('Updated!')

def DeleteNote(request,pk):
    note = Note.objects.filter(id=pk).delete()
    return Response('Deleted!')
