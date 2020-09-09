from django.urls import path
# flake8: noqa
import api.views as views
from urllib import parse

urlpatterns = [
    path('', views.APIRootList.as_view(), name='root'),
    # All-models views
    path('users/', views.UserList.as_view(), name='users'),
    path('families/', views.FamilyList.as_view(), name='families'),
    path('languages/', views.LanguageList.as_view(), name='languages'),
    path('dimensions/', views.DimensionList.as_view(),name='dimensions'),
    path('features/', views.FeatureList.as_view(), name='features'),
    path('genuses/', views.GenusList.as_view(), name='genuses'),
    path('tagsets/', views.TagSetList.as_view(), name='tagsets'),
    path('lemmas/', views.LemmaList.as_view(), name='lemmas'),
    path('words/', views.WordList.as_view(), name='words'),
    # Detail-Views
    path('dimensions/<str:name>/', views.DimensionDetail.as_view(), name='dimensionDetail'),
    path('features/<str:name>/', views.FeatureDetail.as_view(),name='featureDetail'),
    path('words/<str:name>/', views.WordDetail.as_view(),name='wordDetail'),
    path('lemmas/<str:name>/', views.LemmaDetail.as_view(), name='lemmaDetail'),
    path('tagsets/<str:name>/', views.TagSetDetail.as_view(),name='tagsetDetail'),
    # Download Views
    path('download/dimensions/', views.DimensionDownload.as_view(),name='dim-down'),
    path('download/features/', views.FeatureDownload.as_view(),name='feat-down'),
    path('download/languages/', views.LanguageDownload.as_view(),name='lang-down'),
    path('download/genuses/', views.GenusDownload.as_view(),name='gen-down'),
    path('download/families/', views.FamilyDownload.as_view(),name='fam-down'),
    path('download/words/<str:languageName>/', views.WordDownload.as_view()),
    path('download/families/<str:familyName>/', views.FamilyQueryDownload.as_view()),
    path('download/genuses/<str:genusName>/', views.GenusQueryDownload.as_view()),
    path('download/all/', views.AllLanguagesDownload.as_view()),
]
