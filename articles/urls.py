from django.urls import path
from .views import ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView, Accueil

urlpatterns = [
    path('ArticleListView',ArticleListView.as_view(), name="listview"),
    path('createview/', ArticleCreateView.as_view(), name="createviews"),
    path('<int:pk>/modifier',ArticleUpdateView.as_view(), name="updatev"),
    path('<int:pk>/suprimer',ArticleDeleteView .as_view(), name="delatev"),
    path('<int:pk>/detail',ArticleDetailView.as_view(), name="detailv"),
    path('', Accueil.as_view(), name="affiche"), 
    
]