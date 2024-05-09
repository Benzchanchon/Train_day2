from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/post', methods=['POST', 'GET'])
def receive_json():
    # รับ JSON body จาก request
    json_data = request.json

    # เก็บค่าตัวแปร age
    age = json_data.get('age')

    # พิมพ์ค่าของตัวแปร age ออกมา
    print('Age:', age)

    # return ข้อมูลในรูปแบบ JSON
    return jsonify({'age': age}), 200

if __name__ == '__main__':
    app.run(debug=True, port=523)
