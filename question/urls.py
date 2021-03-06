from django.urls import path
from .views import QuestionListView, GeneratePdf, GeneratePdfDownload, AboutQuestionCreate
from . import views

app_name = 'question'

urlpatterns = [
   #path('',views.index, name = 'index'),
   #path('<int:question_id>/', views.detail, name='detail'),

   path('', views.IndexView.as_view(), name='index'),
   path('desc/', views.AboutQuestionCreate.as_view(), name='q-desc'),
   path('register/', views.UserFormView.as_view(), name='register'),
   path('<int:pk>/', views.DetailView.as_view(), name='detail'),
   path('edit/', views.QuestionList.as_view(), name='edit'),
   path('udt/<int:pk>', views.update, name='edit'),

   path('edit/<int:pk>', views.QuestionDetails.as_view(), name='edit'),
   path('question/add', views.QuestionCreate.as_view(), name='q-add'),
   path('question/<int:pk>/', views.QuestionUpdate.as_view(), name='q-update'),
   path('<int:pk>/delete/', views.QuestionDelete.as_view(), name='q-delete'),
   path('question/',  QuestionListView.as_view(), name='q-list'),
   path('set/',  views.setQ , name='q'),
   path('question/pdf',  GeneratePdf.as_view(), name='q-pdf'),
   path('selected/', views.IndexView.as_view(), name='selected'),
   path('qsee/', views.QuestionAdd.as_view(), name='qsee'),
   path('question/pdf/download',  GeneratePdfDownload.as_view(), name='q-pdf-download'),

]
