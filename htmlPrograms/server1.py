from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask import json

app = Flask(__name__, template_folder="./")
CORS(app)  # Enable CORS to allow cross-origin requests

class stu:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

student = [stu(i[0], i[1]) for i in [['ram', 123], ['sam', 232]]]

@app.route("/updatedata")
def update_data():
    return jsonify([{'name': s.name, 'roll' : s.roll} for s in student]), 200

@app.route("/delete/<int:roll>", methods=["DELETE"])
def delete_data(roll):
    print(roll)
    global student
    new_student = [i for i in student if i.roll != roll]
    student = new_student
    for i in new_student:
        print(i.name, i.roll)
    return jsonify({'message':'data row deleted'}), 200

@app.route('/', methods=['POST', 'GET'])
def index():
    server_url = url_for('index', _external=True)
    global student  # Declare 'student' as global
    try:
        if request.method == 'POST':
            data = request.json  # Access JSON data
            print("Received Data:", data)
            student.append(stu(data['name'], int(data['roll'])))
            for i in student:
                print(i.name,i.roll, type(i))
            return jsonify({"message": "Received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return render_template('rollData.html', student=student,server_url=server_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5060, debug=True)
