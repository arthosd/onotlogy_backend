"""
Contient toutes les fonctions de récupérations pour l'ontologie
"""

from rdflib import Literal, URIRef, Graph, RDF, XSD

# A utiliser pour ajouter des trucs dans la bdd
g = Graph ()
g.parse("ontology/test.owl", format = "turtle")

base_uri = "http://www.semanticweb.org/elie/ontologies/2021/10/Transport/"


def get_all_user () :
    """
    Renvoie tout les utilisateurs dans l'ontologie
    """
    global g # permet d'utiliser la variable global g

    knows_query = """
        SELECT DISTINCT ?user ?nom
        WHERE {
            ?user rdf:type ns1:User .
            ?user ns1:name ?nom .

        }"""

    result = g.query(knows_query)
    result_final = []
    for i in result:
        d = dict()
        d["URI"] = str(i[0])
        d["nom"] = str(i[1])
        result_final.append(d)

    return result_final


def get_all_itineraire (user_name) :
    """
    Renvoie tous les itinéraires d'un utilisateur spécifique avec heure de debut et de fin
    
    User_name représente le nom d'un utilisateur
    """
    global g

    knows_query = """
        SELECT DISTINCT ?itineraire ?nom ?debut ?fin ?date
        WHERE {
            ?user rdf:type ns1:User .
            ?user ns1:name \"""" + user_name + """\"^^xsd:string .
            ?itineraire ns1:est_emprunte_par ?user .
            ?itineraire ns1:name ?nom .
            ?itineraire ns1:heure_debut ?debut .
            ?itineraire ns1:heure_fin ?fin .
            ?itineraire ns1:date ?date .

        }"""
        
    result = g.query(knows_query)
    result_final = []
    for i in result:
        d = dict()
        d["URI"] = str(i[0])
        d["nom"] = str(i[1])
        d["debut"] = str(i[2])
        d["fin"] = str(i[3])
        d["date"] = str(i[4])
        result_final.append(d)

    return result_final

def get_all_trajet (itineraire_id) :
    """
    Renvoie tout les trajets d'un itineraire spécifique (avec leurs object properties)
    
    itineraire_id représente l'id d'un itineraire
    """
    global g

    knows_query = """
        SELECT DISTINCT ?nom ?nomdepart ?nomarrivee ?nomTransport
        WHERE {
            ?itineraire rdf:type ns1:Itineraire .
            ?itineraire ns1:name \"""" + itineraire_id + """\"^^xsd:string .
            ?itineraire ns1:est_combinaison ?trajet .
            ?trajet ns1:utilise ?transport .
            ?transport ns1:name ?nomTransport .
            ?trajet ns1:name ?nom .
            ?trajet ns1:part_de ?depart .
            ?depart ns1:name ?nomdepart.
            ?trajet ns1:arrive_a ?arrivee .
            ?arrivee ns1:name ?nomarrivee.


        }"""
        
    result = g.query(knows_query)

    result_final = []
    for i in result:
        d = dict()
        d["nom"] = str (i[0])
        d["depart"] = str (i[1])
        d["arrivee"] = str (i[2])
        d["transport"] = str(i[3])
        result_final.append(d)

    return result_final


def get_all_cities () :
    """
    Renvoie toutes les villes dans l'ontologie
    """
    global g

    knows_query = """
        SELECT DISTINCT ?ville ?nom
        WHERE {
            ?ville rdf:type ns1:Ville .
            ?ville ns1:name ?nom .
        }"""
        
    result = g.query(knows_query)

    result_final = []
    for i in result:
        d = dict()
        d["URI"] = str (i[0])
        d["ville"] = str (i[1])
        result_final.append(d)

    return result_final

def get_all_place () :
    """
    Renvoie tous les lieux dans l'ontologie
    """
    global g

    knows_query = """
        SELECT DISTINCT ?lieu ?nom
        WHERE {
            ?lieu rdf:type ns1:Lieu .
            ?lieu ns1:name ?nom .
        }"""
        
    result = g.query(knows_query)

    result_final = []
    for i in result:
        d = dict()
        d["URI"] = str (i[0])
        d["lieu"] = str (i[1])
        result_final.append(d)

    return result_final

def get_specific_place (place_id) :
    """
    Renvoie tous les object properties d'un lieu
    """
    global g

    knows_query = """
        SELECT DISTINCT ?name ?details
        WHERE {
            ?lieu rdf:type ns1:Lieu .
            ?lieu ns1:name \"""" + place_id + """\"^^xsd:string .
            ?lieu ns1:name ?name .
            ?lieu ns1:details_lieu ?details .
        }"""
        
    result = g.query(knows_query)

    result_final = []
    for i in result:
        d = dict()
        d["lieu"] = str (i[0])
        d["details"] = str (i[1])
        result_final.append(d)

    return result_final

def get_all_stations () :
    """
    Renvoie toutes les gares dans l'ontologie
    """
    global g

    knows_query = """
        SELECT DISTINCT ?gare ?nom
        WHERE {
            ?gare rdf:type ns1:Gare .
            ?gare ns1:name ?nom .
        }"""
        
    result = g.query(knows_query)

    result_final = []
    for i in result:
        d = dict()
        d["URI"] = str (i[0])
        d["gare"] = str (i[2])
        result_final.append(d)

    return result_final

def get_all_lines () :
    """
    Renvoie toutes les lignes de transport en communs dans l'ontologie
    """
    global g

    knows_query = """
        SELECT DISTINCT ?metro ?ligneMetro ?bus ?ligneBus ?rer ?ligneRer ?tramway ?ligneTramway
        WHERE {
            ?metro rdf:type ns1:Metro .
            ?metro ns1:name ?ligneMetro .
            ?bus rdf:type ns1:Bus .
            ?bus ns1:name ?ligneBus .
            ?rer rdf:type ns1:Rer .
            ?rer ns1:name ?ligneRer .
            ?tramway rdf:type ns1:tramway .
            ?tramway ns1:name ?ligneTramway .
        }"""
        
    result = g.query(knows_query)

    result_final = []
    for i in result:
        d = dict()
        d["URImetro"] = str (i[0])
        d["ligneMetro"] = str (i[1])
        d["URIbus"] = str (i[2])
        d["ligneBus"] = str (i[3])
        d["URIrer"] = str (i[4])
        d["ligneRer"] = str (i[5])
        d["URItramway"] = str (i[6])
        d["ligneTramway"] = str (i[7])
        result_final.append(d)

    return result_final

def get_all_metro () :
    """
    Renvoie toutes les lignes de metro dans l'ontologie
    """
    global g

    knows_query = """
        SELECT DISTINCT ?metro ?ligneMetro
        WHERE {
            ?metro rdf:type ns1:Metro .
            ?metro ns1:name ?ligneMetro .
        }"""
        
    result = g.query(knows_query)

    result_final = []
    for i in result:
        d = dict()
        d["URImetro"] = str (i[0])
        d["ligneMetro"] = str (i[1])
        result_final.append(d)

    return result_final

def get_all_bus () :
    """
    Renvoie toutes les lignes de bus dans l'ontologie
    """
    global g

    knows_query = """
        SELECT DISTINCT ?bus ?ligneBus
        WHERE {
            ?bus rdf:type ns1:Bus .
            ?bus ns1:name ?ligneBus .
        }"""
        
    result = g.query(knows_query)

    result_final = []
    for i in result:
        d = dict()
        d["URIbus"] = str(i[0])
        d["ligneBus"] = str (i[1])
        result_final.append(d)

    return result_final

def get_all_rer () :
    """
    Renvoie toutes les lignes de rer dans l'ontologie
    """
    global g

    knows_query = """
        SELECT DISTINCT ?rer ?ligneRer
        WHERE {
            ?rer rdf:type ns1:Rer .
            ?rer ns1:name ?ligneRer .
        }"""
        
    result = g.query(knows_query)

    result_final = []
    for i in result:
        d = dict()
        d["URIrer"] = str (i[0])
        d["ligneRer"] = str (i[1])
        result_final.append(d)

    return result_final

def get_all_tramway () :
    """
    Renvoie toutes les lignes de tramway dans l'ontologie
    """
    global g

    knows_query = """
        SELECT DISTINCT ?tramway ?ligneTramway
        WHERE {
            ?tramway rdf:type ns1:Tramway .
            ?tramway ns1:name ?ligneTramway .
        }"""
        
    result = g.query(knows_query)

    result_final = []
    for i in result:
        d = dict()
        d["URItramway"] = str (i[0])
        d["ligneTramway"] = str (i[1])
        result_final.append(d)

    return result_final

def get_all_transport () :
    """
    Renvoie tous les moyens de transport dans l'ontologie
    """
    global g

    knows_query = """
        SELECT DISTINCT ?transport ?nom
        WHERE {
            ?transport rdf:type ns1:Transport .
            ?transport ns1:name ?nom .
        }"""
        
    result = g.query(knows_query)

    result_final = []
    for i in result:
        d = dict()
        d["URI"] = str (i[0])
        d["nom"] = str (i[1])
        result_final.append(d)

    return result_final


# -------------------- Add middleware --------------------------

def add_user (user_name) :
    """
    Ajoute une utilisteur à la base de données
    """
    global base_uri
    global g

    user_name_treated = user_name.replace(" ", "_")

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


def add_itineraire_for_user (user_name, itineraire_name,date ,horaire_debut, horaire_fin) :
    """
    Rajoute un itineraire dans l'ontologie
    """
    global base_uri
    global g

    itineraire_name_treated = itineraire_name.replace (" ", "_")

    name_uri = URIRef(base_uri+"name")
    itineraire_name_literal = Literal(str(itineraire_name), datatype=XSD.string)

    # Date
    date_uri_litteral = Literal(str(date), datatype=XSD.string)
    date_uri = URIRef(base_uri+"date")

    # On créer le type itinéraire ainsi que l'individu itineraire
    itineraire_uri = URIRef(base_uri+"Itineraire")
    itineraire_individuals_uri = URIRef(base_uri+"Itineraire/"+itineraire_name_treated)

    # Inverse properties
    est_emprunte_par_uri = URIRef(base_uri+"est_emprunte_par")


    # Horraire des itinéraires
    horaire_depart_uri = URIRef(base_uri+"heure_debut")
    horaire_fin_uri = URIRef(base_uri+"heure_fin")

    hdi = Literal (horaire_debut, datatype=XSD.string)
    hfi = Literal (horaire_fin, datatype=XSD.string)

    # On créer l'individu user
    user_individual_uri = URIRef(base_uri+"User/"+user_name)

    # On créer le lien qui uni les deux
    emprunte_uri = URIRef(base_uri+"emprunte")

    try :

        # On ajoute l'individu itineraire
        g.add( (itineraire_individuals_uri, RDF.type, itineraire_uri) )
        g.add( (itineraire_individuals_uri, date_uri, date_uri_litteral) )
        g.add( (itineraire_individuals_uri, name_uri, itineraire_name_literal) )
        g.add( (itineraire_individuals_uri, horaire_depart_uri, hdi) )
        g.add( (itineraire_individuals_uri, horaire_fin_uri, hfi) )

        # On lies les deux
        g.add( (user_individual_uri, emprunte_uri, itineraire_individuals_uri) )

        # On ajoute les fonctions inverse
        g.add( (itineraire_individuals_uri, est_emprunte_par_uri,user_individual_uri) )

        # On enregistre
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

    name_uri = URIRef(base_uri+"name")
    trajet_name_literal = Literal(str(trajet_config["trajet_name"]), datatype=XSD.string)

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

    g.add ( (trajet_individual_uri,name_uri, trajet_name_literal) )

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



"""result = get_all_trajet('maison')

for res in result :
    print ('-----------------')
    print (res)
"""

"""
print (add_user("Elie"))

print (add_itineraire_for_user("Elie","maison","02/11/1999","20h30", "21h00") )

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

print (add_itineraire_for_user("Julien_Champagne","Universite maison","02/11/2002","20h30", "21h00") )
print (add_itineraire_for_user("Julien_Champagne","Parc des princes","02/11/2005","20h30", "21h00") )

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