from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='date/',view=views.get_date, name='date'),
    path(route='pop_list/',view=views.popular_course_list, name='popular_course_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

