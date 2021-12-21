"""
Contient toutes les fonctions de récupérations pour l'ontologie
"""

from rdflib import Literal, URIRef, Graph, RDF, XSD

# A utiliser pour ajouter des trucs dans la bdd
g = Graph ()
g.parse("ontology/final.owl", format = "turtle")

base_uri = "http://www.semanticweb.org/elie/ontologies/2021/10/Transport/"


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


# -------------------- Add middleware --------------------------

def add_user (user_name) :
    """
    Ajoute une utilisteur à la base de données
    """
    global base_uri
    global g

    user_uri = URIRef(base_uri+"User")
    user_individual = URIRef(base_uri+"User/"+user_name)
    name_uri = URIRef(base_uri+"name")
    name_literal = Literal(str(user_name), datatype=XSD.string)

    try :
        g.add((user_individual, RDF.type, user_uri)) # Adding individuals
        g.add( (user_individual, name_uri, name_literal) ) # adding name

    except Exception :
        return False

    return True


def add_itineraire_for_user (user_name, itineraire_name) :
    """
    Rajoute un itineraire dans l'ontologie
    """
    global base_uri
    global g

    # On créer le type itinéraire ainsi que l'individu itineraire
    itineraire_uri = URIRef(base_uri+"itineraire")
    itineraire_individuals_uri = URIRef(base_uri+"itineraire/"+itineraire_name)

    # On créer l'individu user
    user_individual_uri = URIRef(base_uri+"User/"+user_name)

    # On créer le lien qui uni les deux
    effectue_uri = URIRef(base_uri+"effectue")

    try :

        # On ajoute l'individu itineraire
        g.add( (itineraire_individuals_uri, RDF.type, itineraire_uri) )

        # On lies les deux
        g.add( (user_individual_uri, effectue_uri, itineraire_individuals_uri) )
    except Exception :
        print ("ERROR !")
        return False

    return True

def add_trajet_for_itineraire (itineraire_name, trajet_config) :
    """
    Ajoute un trajet specific pour un itineraire donnée
    """
    # Variable global
    global base_uri
    global g

    trajet_name = trajet_config ["trajet_name"] # nom du trajet
    gare_depart_uri = URIRef(trajet_config ["gare_depart"]) # gare de départ
    gare_fin_uri = URIRef(trajet_config ["gare_fin"]) # Gare fin
    dure = trajet_config ["dure"]

    trajet_depart = URIRef(base_uri+"trajet_depart")
    trajet_fin = URIRef(base_uri+"trajet_fin")

    # On pointe l'itinéraire
    itineraire_individuals_uri = URIRef(base_uri+"itineraire/"+itineraire_name)

    trajet_uri = URIRef(base_uri+"/Trajet")
    trajet_individual_uri = URIRef(base_uri+"/Trajet/"+trajet_name)


    # On créer le trajet
    g.add((trajet_individual_uri, RDF.type, trajet_uri)) # Adding individuals

    # On  lies l'itinéraire avec le trajets
    emprunte_uri = URIRef (base_uri+"emprunte")
    g.add ( (itineraire_individuals_uri, emprunte_uri, trajet_individual_uri) )

    # On le lies avec tout les objects properties
    g.add( (trajet_individual_uri, trajet_depart, gare_depart_uri))
    g.add( (trajet_individual_uri, trajet_fin, gare_fin_uri))

    # On créer le litteral
    dure_trajet_uri = URIRef(base_uri+"duree_trajet")
    dure_litteral = Literal(str(dure), datatype=XSD.int)

    # On lies le trajet avec sa duré
    g.add(trajet_individual_uri, dure_trajet_uri, dure_litteral)
    


def add_lieu ()