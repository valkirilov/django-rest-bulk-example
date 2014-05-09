# Create your views here.

from api.models import Teacher

# Serializers here
from api.serializers import TeacherSerializer

from rest_framework import filters
from rest_framework import generics, permissions
from rest_framework.renderers import BrowsableAPIRenderer, UnicodeJSONRenderer

from rest_framework_bulk import ListBulkCreateUpdateDestroyAPIView

from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication

class TeachersList(ListBulkCreateUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    #serializer_class = TeacherSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #renderer_classes = (UnicodeJSONRenderer, BrowsableAPIRenderer) # for api view
    model = Teacher
    serializer = TeacherSerializer(queryset, many=True)

