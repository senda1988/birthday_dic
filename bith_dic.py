# Der Code erstellt eine Flask-Webanwendung, die Benutzerdaten (mit Namen und Geburtsdatum) aus einer JSON-Datei lädt und speichert.
# Route /users (GET) Abrufen des Geburtstags eines Benutzers anhand des Namens
# Route /users/<id> (PUT) Aktualisieren des Geburtstags eines Benutzers anhand seiner ID.
# Alle Änderungen und Daten werden in einer lokalen JSON-Datei gespeichert, die beim Start geladen wird.
from flask import Flask, request
from classes.birthday_d import users


import json

app = Flask(__name__)

# Pfad zur Datei, in der die Benutzerdaten gespeichert werden
USERS_FILE_PATH = "users_data.json"


# Funktion zum Laden der Benutzerdaten aus der JSON-Datei
def load_users():
    try:
        with open(USERS_FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Wenn die Datei noch nicht existiert, gib eine leere Liste zurück
        return []


# Funktion zum Speichern der Benutzerdaten in die JSON-Datei
def save_users(users):
    with open(USERS_FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)


# Benutzerliste laden
users = load_users()


# dict_birthday = [
#     {"name": "Albert Einstein", "birthday": "14/03/1879"},
#     {"name": "Benjamin Franklin", "birthday": "01/17/1706"},
#     {"name": "Ada Lovelace", "birthday": "10/12/1815"},
# ]


@app.route("/users", methods=["GET"])
def get_user():
    print(f"Welcome to the birthday dictionary. We know the birthdays of:")
    # for i in users:
    #     print(i["name"])
    choice = request.args.get("name")
    # choice = input(" Who's birthday do you want to look up?")

    for i in users:
        if i["name"] == choice:
            return f"{choice}´s birthday is {i['birthday']}"


@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    credentials = request.get_json()
    new_birthday = credentials.get("birthday")
    for i in users:
        if id == i["id"]:
            i["birthday"] = new_birthday
            user = i

    save_users(users)
    return f"User {id} updated successfully user updated: , {user}", 200


if __name__ == "__main__":
    app.run(debug=True, port=6060)
