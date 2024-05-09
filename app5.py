from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/get', methods=['GET'])
def get_data():
    # สร้างข้อมูล JSON
    data = {
        "Name": "The RaMe",
        "Age": "523"
    }

    # ส่ง JSON กลับไปใน response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=523)
