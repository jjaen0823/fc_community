from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.board_list, name='list')
    # path('write/', views.write, name='write')
]