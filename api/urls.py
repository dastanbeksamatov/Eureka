from django.urls import path
from . import views

urlpatterns = [
    path('', views.APIRootList.as_view(), name='root'),
    path('users/', views.UserList.as_view(), name='users'),
    path('languages/', views.LanguageList.as_view(), name='languages'),
    path('dimensions/', views.DimensionList.as_view(),
         name='dimensions'),
    path('dimensions/<slug:name>/', views.DimensionDetail.as_view(),
         name='dimensionDetail'),
    path('features/', views.FeatureList.as_view(), name='features'),
    path('features/<slug:name>/', views.FeatureDetail.as_view(),
         name='featureDetail'),
    path('words/', views.WordList.as_view(), name='words'),
    path('words/<slug:name>/', views.WordDetail.as_view(),
         name='wordDetail'),
    path('lemmas/', views.LemmaList.as_view(), name='lemmas'),
    path('lemmas/<slug:name>/', views.LemmaDetail.as_view(), name='lemmaDetail'),
    path('genuses/', views.GenusList.as_view(), name='genuses'),
    path('tagsets/', views.TagSetList.as_view(), name='tagsets'),
    path('tagsets/<slug:name>/', views.TagSetDetail.as_view(),
         name='tagsetDetail'),
    path('families/', views.FamilyList.as_view(), name='families')
]
