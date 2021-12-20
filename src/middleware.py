"""
Contient toutes les fonctions de récupérations pour l'ontologie
"""

from rdflib import Literal, URIRef, Graph, RDF, XSD

# A utiliser pour ajouter des trucs dans la bdd
g = Graph ()
g.parse("ontology/final.owl", format = "turtle")


def get_all_user () :
    """
    Renvoie tout les utilisateurs dans l'ontologie
    """
    global g # permet d'utiliser la variable global g

    result = None

    return result

def get_all_itineraire (user_id) :
    """
    Renvoie tout les itinéraires d'un utilisteur spécifique
    
    User_id représente l'id d'un utilisateur
    """
    global g

    result = None

    return result


def get_all_trajet (itineraire_id) :
    """
    Renvoie tout les trajet d'un itineraire spécifique (avec leurs object properties)
    
    itineraire_id représente l'id d'un itineraire
    """
    global g

    result = None

    return result

def get_all_cities () :
    """
    Renvoie toutes les villes dans l'ontologie
    """
    global g

    result = None

    return result

def get_all_place () :
    """
    Renvoie tous les lieux dans l'ontologie
    """
    global g

    result = None

    return result

def get_all_place_in_city (city_id) :
    """
    Renvoie tous les lieux dans une ville donnée par lerus id
    """
    global g

    result = None

    return result


def get_specific_place (place_id) :
    """
    Renvoie tous les object properties d'un lieu
    """
    global g

    result = None

    return result