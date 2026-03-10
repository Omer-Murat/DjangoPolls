from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # General View Routes
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("register/", views.RegisterView.as_view(), name="register"),

    # Poll Management Routes
    path("my-polls/", views.MyPollsView.as_view(), name="my_polls"),
    path("create/", views.PollCreateView.as_view(), name="create"),
    path("<int:pk>/manage/", views.PollManageView.as_view(), name="manage"),
    path("<int:pk>/delete/", views.PollDeleteView.as_view(), name="delete"),
    
    # Choice Management Routes
    path("<int:question_id>/choice/add/", views.ChoiceCreateView.as_view(), name="choice_add"),
    path("choice/<int:pk>/edit/", views.ChoiceUpdateView.as_view(), name="choice_edit"),
    path("choice/<int:pk>/delete/", views.ChoiceDeleteView.as_view(), name="choice_delete"),
]
