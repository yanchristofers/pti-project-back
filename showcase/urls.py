from django.urls import path

from . import views
urlpatterns = [
  path('<str:sort>', views.FilmList.as_view()),
  path('<int:id>/<str:action>', views.FilmDetail.as_view())
]