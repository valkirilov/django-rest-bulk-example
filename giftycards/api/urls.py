from api import views
from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group, Permission
from api.models import Teacher
from rest_framework import viewsets, routers

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group
    
class PermissionViewSet(viewsets.ModelViewSet):
    model = Permission

class TeachersViewSet(viewsets.ModelViewSet):
    model = Teacher

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permission', PermissionViewSet)

router.register(r'teachers', TeachersViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    #url(r'^free-rooms/$', views.FreeRooms.as_view()),
    url(r'^teachers/$', views.TeachersList.as_view()),
    #url(r'^schedule/$', views.ScheduleList.as_view()),
)