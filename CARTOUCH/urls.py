from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^ajout/', views.ajout_cartouche, name='ajout'),
    url(r'^ajoutinfo/', views.ajout_info, name='ajout'),
    url(r'^lesdocuments/(?P<matiere>)$', views.lesdocuments, name='documents'),
    url(r'^document/(?P<ref>)$', views.document, name='document'),
    url(r'^lesmatieres/', views.lesmatieres, name='documents'),
    url(r'^mdp/', views.mdp, name='mdp'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
