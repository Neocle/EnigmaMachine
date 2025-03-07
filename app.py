from flask import Flask, render_template, request, session, jsonify
from modules.classe_enigma import Enigma

app = Flask(__name__)
app.secret_key = "clétrèssécurisétqt"

@app.route('/')
def home():
    if "enigma" not in session:
        session["rotor1"] = "1"
        session["rotor2"] = "2"
        session["rotor3"] = "3"
        session["reflector"] = "1"

    return render_template("index.html")

@app.route('/set_enigma', methods=['POST'])
def set_enigma():
    data = request.get_json()
    session["rotor1"] = data.get("rotor1")
    session["rotor2"] = data.get("rotor2")
    session["rotor3"] = data.get("rotor3")

    session["start1"] = data["start1"]
    session["start2"] = data["start2"]
    session["start3"] = data["start3"]

    session["reflector"] = data.get("reflector")

    return jsonify({"message": "Settings updated"})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    letter = data.get("letter")

    if not letter or len(letter) != 1:
        return jsonify({"error": "Invalid letter"}), 400

    print(session)

    enigma = Enigma(session["rotor1"], session["rotor2"], session["rotor3"], session["reflector"])
    enigma.Set_Configuration_depart(session["start1"], session["start2"], session["start3"])

    decrypted_letter = enigma.Decodagelettre(letter)

    return jsonify({"decrypted": decrypted_letter})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
