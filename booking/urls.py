from django.urls import path
from .views import base_views, question_views, answer_views
from . import views

app_name = 'booking'
urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
    
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # # path('', views.index),
    # # path('<int:question_id>/', views.detail),
    # path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # path('question/create/', views.question_create, name='question_create'),
    # path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    # path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    # path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    # path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]


# 아래는 generic view 적용 시를 기준함(views.py와 함께 수정 필요
# app_name = 'booking'
# urlpatterns = [
#     path('', views.IndexView.as_view()),
#     path('<int:pk>/', views.DetailView.as_view()),
# ]