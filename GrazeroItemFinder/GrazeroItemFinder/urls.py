"""
Definition of urls for GrazeroItemFinder.
"""

from django.urls import path
from app import forms, views


urlpatterns = [
    path('', views.top, name='top'),
    path('construction/', views.construction, name='construction'),

    path('updata_item_list', views.updata_button, name='updata_item_list'),
]
