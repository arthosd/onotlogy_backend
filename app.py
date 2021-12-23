from flask import Flask, request

from src.middleware import add_trajet_for_itineraire,add_user, add_lieu,add_itineraire_for_user
from src.middleware import get_all_transport, get_all_tramway,get_all_rer,get_all_bus, get_all_metro, get_all_lines, get_all_user, get_all_itineraire, get_all_trajet, get_all_cities, get_all_place, get_specific_place, get_all_stations

app = Flask (__name__)
base_url = "/api/V1/ontology/"


@app.route(base_url+"places/add", methods = ['POST'])
def add_place ():
    """
    Add place in ontology
    """
    if request.method == 'POST':
        result = add_lieu(
            request.json["place_name"],
            request.json["place_description"],
            request.json["ville_uri"]
        )

        return {
            "status" : 200,
            "meesage" : "Place added"
        } if result == True else {
            "status" : 500,
            "meesage" : "Server error !"
        }

    return {
        "status" : 400,
        "meesage" : "Bad request !"
    }


# Add trajets
@app.route(base_url+"user/<user_token>/tajets/<trajet_id>", methods = ['POST'])
def add_user_trajets (user_token, trajet_id) :
    """
    Return all the trajet of a specific users
    """
    if request.method == 'POST':
        
        return {
        "status" : 200,
        "itineraire" : [{
            "name" : "Maison - Boulot",
            "id" : "UYUJHUB-UHUZY"
        },
        {
            "name" : "Maison Juliette",
            "id" : "JHU78UY-YTYGFGVCDE-UHUZY"
        },
        {
            "name" : "Université - Maison",
            "id" : str(trajet_id)
        }]
    } 


# Add or Get specific user
@app.route(base_url+"users/<user_token>", methods = ['POST'])
def add_user_api (user_token) :
    """
    Get specific users / or Add a specific user
    """
    
    # Si la requete est en post, on créer l'utilisateur
    result = add_user (user_token.replace(" ","_"))

    return {
        "status" : 200,
        "id" : str(user_token)
    } if result == True else {
        "status" : 400,
        "message" : "Could not add user to database."
    }

# Add itinerairies
@app.route(base_url+"itineraire", methods = ['POST'])
def add_itineraire_api () :
    """
    Get specific users / or Add a specific user
    """
    
    # Si la requete est en post, on créer l'utilisateur
    result = add_itineraire_for_user (
        request.json["user_name"],
        request.json["itineraire_name"],
        request.json["date"],
        request.json["heure_debut"],
        request.json["heure_fin"]
    )

    return {
        "status" : 200,
        "message" : "Good !"
    } if result == True else {
        "status" : 400,
        "message" : "Could not add user to database."
    }

# Add trajet
@app.route(base_url+"itineraire/trajet", methods = ['POST'])
def add_trajet_api () :
    """
    Get specific users / or Add a specific user
    """
    
    # Si la requete est en post, on créer l'utilisateur
    result = add_trajet_for_itineraire (
        request.json["itineraire_name"],
        {
            "trajet_name" : request.json["trajet_name"],
            "transport" : request.json["transport"],
            "lieu_depart" : request.json["lieu_depart"],
            "lieu_fin" : request.json["lieu_fin"]

        }
    )
    return {
        "status" : 200,
        "message" : "Good !"
    } if result == True else {
        "status" : 400,
        "message" : "Could not add trajet to database."
    }

# Get all the users from ontology
@app.route(base_url+"users")
def get_all_users () :
    """
    Get all users
    """

    result = get_all_user()

    return {
        "data" : result,
        "status" : 200
    }

# Get all the user's itineraries from ontology
@app.route(base_url+"itineraire/<user_name>")
def get_all_itineraries (user_name) :
    """
    Get all user itineries
    """
    print (user_name)
    result = get_all_itineraire(user_name)

    return {
        "data" : result,
        "status" : 200
    }

# Get all the user's itineraries from ontology
@app.route(base_url+"trajet/<itineraire_name>")
def get_trajet (itineraire_name) :
    """
    Get all trajet of itinerairies
    """

    result = get_all_trajet(itineraire_name)

    return {
        "data" : result,
        "status" : 200
    }

# Get all cities
@app.route(base_url+"cities")
def get_cities () :
    """
    Get all cities
    """

    result = get_all_cities()

    return {
        "data" : result,
        "status" : 200
    }


# Get all places
@app.route(base_url+"cities/places")
def get_places () :
    """
    Get all cities
    """

    result = get_all_place()

    return {
        "data" : result,
        "status" : 200
    }

# Get a place place
@app.route(base_url+"cities/places/<name>")
def get_spe_place (name) :
    """
    Get a place
    """

    result = get_specific_place(name)

    return {
        "data" : result,
        "status" : 200
    }

@app.route(base_url+"stations")
def get_station () :
    """
    Get all stations
    """

    result = get_all_stations()

    return {
        "data" : result,
        "status" : 200
    }

@app.route(base_url+"lines")
def get_lines () :
    """
    Get all lines
    """

    result = get_all_lines ()

    return {
        "data" : result,
        "status" : 200
    }


@app.route(base_url+"lines/metro")
def get_metro () :
    """
    Get all metro
    """

    result = get_all_metro ()

    return {
        "data" : result,
        "status" : 200
    }

@app.route(base_url+"lines/bus")
def get_bus () :
    """
    Get all bus
    """

    result = get_all_bus ()

    return {
        "data" : result,
        "status" : 200
    }

@app.route(base_url+"lines/rer")
def get_rer () :
    """
    Get all bus
    """

    result = get_all_rer()

    return {
        "data" : result,
        "status" : 200
    }

@app.route(base_url+"lines/tramway")
def get_tramway () :
    """
    Get all tramways
    """

    result = get_all_tramway ()

    return {
        "data" : result,
        "status" : 200
    }

@app.route(base_url+"transport")
def get_transport () :
    """
    Get all transport
    """

    result = get_all_transport ()

    return {
        "data" : result,
        "status" : 200
    }


@app.route(base_url+"destination")
def get_all_place_gare () :
    """
    Get all gares and place
    """

    result_statitions = get_all_stations ()
    result_place = get_all_place()

    return {
        "data" : result_statitions + result_place,
        "status" : 200
    }

@app.route(base_url+"navigation")
def get_all_navigation () :
    """
    Get all metro, rer, tramway
    """

    result_bus = get_all_bus ()
    result_metro = get_all_metro()
    result_tramvay = get_all_tramway()
    result_rer = get_all_rer()

    result = result_bus + result_metro + result_tramvay + result_rer

    return {
        "data" : result,
        "status" : 200
    }

# Server info
@app.route("/info")
def info () :

    return {
        "server" : "Flask",
        "author" : "Elie EL DEBS and Julien CHAMPAGNE",
        "version" : 1.0,
        "status" : 200
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
