from flask import Flask, request, jsonify

app = Flask(__name__)
#app is the name of our application

@app.route("/")
def home():
    return "This is a home page"


#This is a GET METHOD
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Aadarsh",
        "email": "anagrath1@gmail.com"
        }
#A query parameter is used to make path unique, its a extra value that
#can be added to make path different, after ? it can be added
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

#This is a POST METHOD
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201


if __name__== "__main__":
    app.run(debug=True)
    #This will run our flask server |basic initialisation

