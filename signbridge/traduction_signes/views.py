
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def signe_vers_texte(request):
    """Vue pour la traduction signe vers texte"""
    context = {
        'flask_url': 'http://localhost:5001',  # URL de l'app Flask
    }
    return render(request, 'traduction/signe_vers_texte.html', context)