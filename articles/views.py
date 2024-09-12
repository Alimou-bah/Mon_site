
# Create your views here.

""" fonction pour les views """

from pipes import Template
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from .models import Article
from .forms import Article_f


class ArticleListView(ListView) :
    """
    cette fonction returne la liste des articles elle herite de la fonction ListView
    """
    model = Article 
    template_name = 'articles/list_articles.html'  
    context_object_name = 'articles'



class ArticleCreateView(CreateView):
 
    
    model = Article
    form_class = Article_f
    template_name = 'articles/ajout.html'
    success_url = reverse_lazy('listview')



class ArticleUpdateView(UpdateView):
    """
    cette fonction permet la modification de l'article séléctionné elle herite de la fonction UpdateView
    """
    model = Article
    form_class =Article_f
    template_name = 'articles/update.html'
    success_url = reverse_lazy('listview')


# fonction pour voir les détails de l'article 
class ArticleDetailView(DetailView):
    
    model = Article 
    template_name = 'articles/detail.html'
    context_object_name = 'article' 

# fonction pour la suppression de l'article sélécttioné
class ArticleDeleteView(DeleteView):

    model = Article
    template_name = "articles/delete.html" 
    success_url = reverse_lazy('listview') 

class Accueil(TemplateView):
    template_name= "articles/index.html"
 
