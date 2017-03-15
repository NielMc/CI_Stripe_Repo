from django.conf.urls import url
from .views import profile, logout

urlpatterns = [
    url(r'^profile$', profile, name='profile'),
    url(r'^logout$', logout, name='logout')
]