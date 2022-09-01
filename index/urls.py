from django.urls import path
from .views import *
app_name = 'nikita_sos'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('blog/', Blog.as_view(), name='blog')
]
