from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])                                      #For viewing all the notes
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)

@api_view(['GET'])                                      #For accessing a particular note
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many = False)
    return Response(serializer.data)

@api_view(['POST'])                                     #For Creating note
def createNote(request):
    data = request.data
    body = data['body']
    note = Note.objects.create(body=body)
    serializer = NoteSerializer(note, many = False)
    return Response(serializer.data)

@api_view(['PUT'])                                      #For modifying notes
def updateNote(request, pk):
    data = request.data
    title=data['title']
    body = data['body']
    note = Note.objects.filter(id=pk).update(title=title,body=body)
    return Response('Updated!')

@api_view(['DELETE'])                                   #For Deleting a Note
def deleteNote(request, pk):
    note = Note.objects.filter(id=pk).delete()
    return Response('Deleted!')

