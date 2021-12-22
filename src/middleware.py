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

    knows_query = """
        SELECT DISTINCT ?nom
        WHERE {
            ?user rdf:type ns1:User .
            ?user ns1:name ?nom .

        }"""

    result = g.query(knows_query)

    return result

def get_all_itineraire (user_id) :
    """
    Renvoie tout les itinéraires d'un utilisteur spécifique
    
    User_id représente l'id d'un utilisateur
    """
    global g

    knows_query = """
        SELECT DISTINCT ?itineraire ?nom
        WHERE {
            ?itineraire rdf:type ns1:Itineraire .
            ?itineraire ns1:est_emprunte_par \"""" + user_id + """\" .
            ?itineraire ns1:name ?nom .

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
            ?itineraire rdf:type ns1:Itineraire .
            ?itineraire ns1:est_combinaison \"""" + itineraire_id + """\" .
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
        SELECT DISTINCT ?name
        WHERE {
            ?lieu rdf:type ns1:Lieu .
            ?lieu ns1:name ? name .
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
            ?ville ns1:id \"""" + city_id + """\" .
            ?lieu ns1:Lieu .
        }"""
        
    result = g.query(knows_query)

    return result


def get_specific_place (place_id) :
    """
    Renvoie tous les object properties d'un lieu
    """
    global g

    knows_query = """
        SELECT DISTINCT ?name ?details
        WHERE {
            ?lieu rdf:type ns1:Lieu .
            ?lieu ns1:id = \"""" + place_id + """\" .
            ?lieu ns1:name ?name.
            ?lieu ns1:details_lieu ?details .
        }"""
        
    result = g.query(knows_query)

    return result


# -------------------- Add middleware --------------------------

def add_user (user_name) :
    """
    Ajoute une utilisteur à la base de données
    """
    global base_uri
    global g

    user_name_treated = user_name.replace(" ", "_")

    print("Triggered")
    user_uri = URIRef(base_uri+"User")
    user_individual = URIRef(base_uri+"User/"+user_name_treated)
    name_uri = URIRef(base_uri+"name")
    name_literal = Literal(str(user_name), datatype=XSD.string)

    try :
        g.add((user_individual, RDF.type, user_uri)) # Adding individuals
        g.add( (user_individual, name_uri, name_literal) ) # adding name

        g.serialize(destination='ontology/test.owl', format='turtle')

    except Exception :
        return False

    return True


def add_itineraire_for_user (user_name, itineraire_name, horaire_debut, horaire_fin) :
    """
    Rajoute un itineraire dans l'ontologie
    """
    global base_uri
    global g

    itineraire_name_treated = itineraire_name.replace (" ", "_")

    # On créer le type itinéraire ainsi que l'individu itineraire
    itineraire_uri = URIRef(base_uri+"Itineraire")
    itineraire_individuals_uri = URIRef(base_uri+"Itineraire/"+itineraire_name_treated)

    # Horraire des itinéraires
    horaire_depart_uri = URIRef(base_uri+"heure_debut")
    horaire_fin_uri = URIRef(base_uri+"heure_fin")

    hdi = Literal (horaire_debut, datatype=XSD.string)
    hfi = Literal (horaire_fin, datatype=XSD.string)

    # On créer l'individu user
    user_individual_uri = URIRef(base_uri+"User/"+user_name)

    # On créer le lien qui uni les deux
    effectue_uri = URIRef(base_uri+"effectue")

    try :

        # On ajoute l'individu itineraire
        g.add( (itineraire_individuals_uri, RDF.type, itineraire_uri) )
        g.add( (itineraire_individuals_uri, horaire_depart_uri, hdi) )
        g.add( (itineraire_individuals_uri, horaire_fin_uri, hfi) )

        # On lies les deux
        g.add( (user_individual_uri, effectue_uri, itineraire_individuals_uri) )

        g.serialize(destination='ontology/test.owl', format='turtle')

    except Exception :
        print ("ERROR !")
        return False

    return True

def add_trajet_for_itineraire (itineraire_name, trajet_config) :
    """
    Ajoute un trajet specifique pour un itineraire donnée
    """
    # Variable global
    global base_uri
    global g

    # Itineraire
    itineraire_individual = URIRef(base_uri+"Itineraire/"+str(itineraire_name))
    est_combinaison_uri = URIRef(base_uri+"est_combinaison")

    # Trajet
    trajet_uri = URIRef(base_uri+"Trajet")
    trajet_individual_uri = URIRef(base_uri+"Trajet/"+trajet_config["trajet_name"])

    utilise_uri =  URIRef(base_uri+"utilise")
    transport_uri = URIRef(trajet_config["transport"])

    g.add( (trajet_individual_uri, RDF.type, trajet_uri) ) # On créer l'instance du trajet

    # Lieux
    lieu_depart_uri = URIRef(trajet_config["lieu_depart"])
    lieu_fin_uri = URIRef(trajet_config["lieu_fin"])

    # Lieu object type
    arrive_a_uri = URIRef(base_uri+"arrive_a")
    part_de_uri = URIRef(base_uri+"part_de")

    # On lies tout
    g.add ( (trajet_individual_uri, arrive_a_uri,lieu_fin_uri) )
    g.add ( (trajet_individual_uri, part_de_uri,lieu_depart_uri) )

    g.add( (trajet_individual_uri, utilise_uri, transport_uri) )

    # On lie le trajet avec l'itineraire
    g.add ( (itineraire_individual, est_combinaison_uri, trajet_individual_uri) )

    g.serialize(destination='ontology/test.owl', format='turtle')

    return True


def add_lieu (nom_lieu, detail_lieu) :
    """
    Ajoute des lieux dans la base de données
    """

    global g
    global base_uri

    nom_lieu_treated = nom_lieu.replace(" ", "_")

    lieu_uri = URIRef(base_uri+"Lieu")
    lieu_individual_uri = URIRef(base_uri+"Lieu/"+nom_lieu_treated)
    name_uri = URIRef(base_uri+"name")
    detail_uri = URIRef(base_uri+"details_lieu")

    # On créer les literal
    name_literal = Literal(str(nom_lieu), datatype=XSD.string)
    detail_literal = Literal(str(detail_lieu), datatype=XSD.string)


    try : 

        g.add ( (lieu_individual_uri, RDF.type, lieu_uri) ) # Instancie le lieu
        g.add ( (lieu_individual_uri, name_uri, name_literal) ) # On lies avec le noms
        g.add ( (lieu_individual_uri, detail_uri, detail_literal) ) # On lies avec le noms

        g.serialize(destination='ontology/test.owl', format='turtle')

    except Exception :
        print ("ERROR !")
        return False

    return True



"""print (add_user("Elie"))

print (add_itineraire_for_user("Elie","maison","20h30", "21h00") )

result = add_trajet_for_itineraire("maison", {
    "trajet_name" : "part_1",
    "transport" : base_uri + "Rer/C00006",
    "lieu_depart" : base_uri+"/Gare/IDFM:10027",
    "lieu_fin" : base_uri+"/Gare/IDFM:10014"
})

result = add_trajet_for_itineraire("maison", {
    "trajet_name" : "part_2",
    "transport" : base_uri + "Rer/C00006",
    "lieu_depart" : base_uri+"/Gare/IDFM:10027",
    "lieu_fin" : base_uri+"/Gare/IDFM:10014"
})

result = add_trajet_for_itineraire("maison", {
    "trajet_name" : "part_2",
    "transport" : base_uri + "Rer/C00006",
    "lieu_depart" : base_uri+"/Gare/IDFM:10027",
    "lieu_fin" : base_uri+"/Gare/IDFM:10014"
})


print (add_user("Julien Champagne"))

print (add_itineraire_for_user("Julien_Champagne","Universite maison","20h30", "21h00") )
print (add_itineraire_for_user("Julien_Champagne","Parc des princes","20h30", "21h00") )

result = add_trajet_for_itineraire("Universite_maison", {
    "trajet_name" : "julien_1",
    "transport" : base_uri + "Tramway/C01389",
    "lieu_depart" : base_uri+"/Gare/IDFM:10027",
    "lieu_fin" : base_uri+"/Gare/IDFM:10014"
})
result = add_trajet_for_itineraire("Universite_maison", {
    "trajet_name" : "julien_2",
    "transport" : base_uri + "Rer/C00006",
    "lieu_depart" : base_uri+"/Gare/IDFM:10027",
    "lieu_fin" : base_uri+"/Gare/IDFM:10014"
})


result = add_trajet_for_itineraire("Parc_des_princes", {
    "trajet_name" : "parc_1",
    "transport" : base_uri + "Rer/C00006",
    "lieu_depart" : base_uri+"/Gare/IDFM:10027",
    "lieu_fin" : base_uri+"/Gare/IDFM:10014"
})
print (add_lieu("Le parc des princes", "Je vais voir du foot la bas lol"))

"""