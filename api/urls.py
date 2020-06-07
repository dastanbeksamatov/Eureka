from django.urls import path
from . import views

urlpatterns = [
    path('', views.APIRootList.as_view(), name='root'),
    path('users/', views.UserList.as_view(), name='users'),
    path('languages/', views.LanguageList.as_view(), name='languages'),
    path('dimensions/', views.DimensionList.as_view(), name='dimensions'),
    path('features/', views.FeatureList.as_view(), name='features'),
    path('words/', views.WordList.as_view(), name='words'),
    path('lemmas', views.LemmaList.as_view(), name='lemmas'),
    path('genuses/', views.GenusList.as_view(), name='genuses'),
    path('tagsets/', views.TagSetList.as_view(), name='tagsets'),
    path('families/', views.FamilyList.as_view(), name='families'),
]
