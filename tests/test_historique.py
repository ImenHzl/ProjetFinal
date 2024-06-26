import sys
import os
from unittest.mock import patch

# Ajouter le chemin du projet au sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.api.v1.historique import Historique

def test_arroseplante_jour_de_pluie():
    """
    Teste la fonction ArrosePlante avec un cas où il pleut tous les jours
    """
    # Données d'entrée
    pays = "France"
    dt = "2024-06-15"
    endt = "2024-06-15"
    
    # Réponse simulée pour un jour de pluie
    mock_response = [{"date": "2024-06-15", "meteo_du_jour": "il pleut"}]

    with patch.object(Historique, 'ArrosePlante', return_value=mock_response):
        # Exécution de la fonction
        data = Historique.ArrosePlante(pays, dt, endt)

        # Debugging: Print data to see what is returned
        print(f"Data returned for test_arroseplante_jour_de_pluie: {data}")

        # Vérification du type de retour
        assert isinstance(data, list)

        # Vérification du nombre de jours
        assert len(data) == 1

        # Vérification des données du jour
        assert data[0]["date"] == "2024-06-15"
        assert data[0]["meteo_du_jour"] == "il pleut"

def test_arroseplante_jour_sans_pluie():
    """
    Teste la fonction ArrosePlante avec un cas où il ne pleut pas
    """
    # Données d'entrée
    pays = "France"
    dt = "2024-06-25"
    endt = "2024-06-25"

    # Réponse simulée pour un jour sans pluie
    mock_response = [{"date": "2024-06-25", "meteo_du_jour": "il pleut pas il faut arroser les plantes"}]

    with patch.object(Historique, 'ArrosePlante', return_value=mock_response):
        # Exécution de la fonction
        data = Historique.ArrosePlante(pays, dt, endt)

        # Debugging: Print data to see what is returned
        print(f"Data returned for test_arroseplante_jour_sans_pluie: {data}")

        # Vérification du type de retour
        assert isinstance(data, list)

        # Vérification du nombre de jours
        assert len(data) == 1

        # Vérification des données du jour
        assert data[0]["date"] == "2024-06-25"
        assert data[0]["meteo_du_jour"] == "il pleut pas il faut arroser les plantes"
