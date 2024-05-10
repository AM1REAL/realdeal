from django.urls import path
from .views import *

urlpatterns = [
    path('', ObjectPList.as_view(), name='objects_list'),
    path('submitData/create/', submit_data, name='object_create'),
    path('submitData/<int:pk>/', get_data, name='object_get'),
    path('submitData/<int:pk>/update', update_data, name='object_update'),
    path('submitData/user__email=<str:email>', AuthEmailObjectPAPI.as_view({'get': 'list'}))
]
