from flask import Flask, request

from src.middleware import add_user, add_lieu

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
            request.json["place_description"]
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

# get tout les lieux
@app.route(base_url+"places")
def get_all_place () :
    """
    Return all places
    """

    return {
        "places" : [{
            "name" : "Tour-Eiffel",
            "city" : "Paris",
            "Descriptions" : "C'est une tour située en pleins cenetre du 15 ieme arrondissemment de Paris",
            "id" : "675-56YTGHY-TR"
        },{
            "name" : "Tour-Eiffel",
            "city" : "Paris",
            "Descriptions" : "C'est une tour située en pleins cenetre du 15 ieme arrondissemment de Paris",
            "id" : "675-JHIU-TR"
        }
        ]
    } 
    

# get users specific trajets
@app.route(base_url+"user/<user_token>/tajet/<trajet_id>", methods = ['GET', 'POST'])
def get_add_specific_trajet (user_token, trajet_id) :
    """
    Return all the itineraries of a trajet
    """

    if request.method == 'GET':
        
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

    else :

        return {
            "itineraire" : [{

            }]
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


# get users all's trajets
@app.route(base_url+"user/<user_token>/tajets", methods = ['GET'])
def get_user_all_trajets (user_token) :
    """
    Return all the trajet of a specific users
    """

    return {
        "data" : [{
            "name" : "Maison - Boulot",
            "id" : "UYUJHUB-UHUZY"
        },
        {
            "name" : "Maison Juliette",
            "id" : "JHU78UY-YTYGFGVCDE-UHUZY"
        }]
    }

# Add or Get specific user
@app.route(base_url+"users/<user_token>", methods = ['GET', 'POST'])
def get_add_user (user_token) :
    """
    Get specific users / or Add a specific user
    """

    if request.method == 'GET':

        return {
            "name" : "elie EL DEBS",
            "id" : str(user_token)
        } 
    
    # Si la requete est en post, on créer l'utilisateur
    result = add_user (user_token.replace(" ","_"))

    return {
        "status" : 200,
        "id" : str(user_token)
    } if result == True else {
        "status" : 400,
        "message" : "Could not add user to database."
    }

# Get all the users from ontology
@app.route(base_url+"users")
def get_all_users () :
    """
    Get all users
    """

    return { "data" : [{
        "name" : "elie EL DEBS",
        "id" : "uiyta-Y6tyue"
    },{
       "name" : "Julien Champagne",
       "id" : "UY7t-IUYU-TRF-Y6tyue" 
    }] }

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
