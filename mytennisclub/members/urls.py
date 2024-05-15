from django.urls import path
from members.views import *

urlpatterns = [
    path('members/', members, name='members'),
    path('add-member/', add_member, name='add_member'),
    path('update-member/<int:id>/', update_member, name='update_member'),
    path('delete-member/<int:id>/', delete_member, name='delete_member'),   
]
