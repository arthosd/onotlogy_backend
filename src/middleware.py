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

    knows_query = """
        SELECT DISTINCT ?nom
        WHERE {
            ?nom rdf:type ns1:User .
            ?nom ns1:name ?nom .

        }"""

    result = g.query(knows_query)

    return result

def get_all_itineraire () :
    """
    Renvoie tout les itinéraires d'un utilisteur spécifique
    
    User_id représente l'id d'un utilisateur
    """
    global g

    knows_query = """
        SELECT DISTINCT ?itineraire
        WHERE {
            ?itineraire rdf:type ns1:Itineraire .
            ?itineraire ?p ?o
        }"""
        
    result = g.query(knows_query)

    return result


def get_all_trajet (itineraire_id) :
    """
    Renvoie tout les trajet d'un itineraire spécifique (avec leurs object properties)
    
    itineraire_id représente l'id d'un itineraire
    """
    global g

    knows_query = """
        SELECT DISTINCT ?trajet ?duree
        WHERE {
            ?trajet rdf:type ns1:Trajet .
            ?trajet ns1:id itineraire_id .
            ?trajet ns1:name .
            ?trajet ns1:duree_trajet ?duree .
        }"""
        
    result = g.query(knows_query)

    return result

def get_all_cities () :
    """
    Renvoie toutes les villes dans l'ontologie
    """
    global g

    knows_query = """
        SELECT DISTINCT ?name
        WHERE {
            ?ville rdf:type ns1:Ville .
            ?ville ns1:name ?name .
        }"""
        
    result = g.query(knows_query)

    return result

def get_all_place () :
    """
    Renvoie tous les lieux dans l'ontologie
    """
    global g

    knows_query = """
        SELECT DISTINCT ?lieu
        WHERE {
            ?lieu rdf:type ns1:Lieu .
        }"""
        
    result = g.query(knows_query)

    return result

def get_all_place_in_city (city_id) :
    """
    Renvoie tous les lieux dans une ville donnée par leurs id
    """
    global g

    knows_query = """
        SELECT DISTINCT ?lieu
        WHERE {
            ?ville rdf:type ns1:Ville .
            ?ville ns1:id city_id .
            ?lieu ns1:id .
        }"""
        
    result = g.query(knows_query)

    return result


def get_specific_place (place_id) :
    """
    Renvoie tous les object properties d'un lieu
    """
    global g

    knows_query = """
        SELECT DISTINCT ?lieu ?details
        WHERE {
            ?lieu rdf:type ns1:Lieu .
            ?lieu ns1:name .
            ?lieu ns1:details_lieu ?details .
        }"""
        
    result = g.query(knows_query)

    return result


#cities = get_all_cities()
#users = get_all_user()
itineraire = get_all_itineraire()

for row in itineraire:
    print(row[0])