from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
from .utils import getAllnotes,getSingleNote,CreateNote,UpdateNote,DeleteNote



@api_view(['GET'])                                      #For viewing all the notes
def getNotes(request):
    return getAllnotes(request)

@api_view(['GET'])                                      #For accessing a particular note
def getNote(request, pk):
    return getSingleNote(request,pk)

@api_view(['POST'])                                     #For Creating note
def createNote(request):
    return CreateNote(request)

@api_view(['PUT'])                                      #For modifying notes
def updateNote(request, pk):
    return UpdateNote(request,pk)

@api_view(['DELETE'])                                   #For Deleting a Note
def deleteNote(request, pk):
    return DeleteNote(request,pk)

