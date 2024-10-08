from flask import Flask, request, jsonify

app = Flask(__name__)


def function_one(data):
    return {"message": "Function one executed", "data": data}


def function_two(data):
    return {"message": "Function two executed", "data": data}


@app.route('/datalore', methods=['POST'])
def handle_webhook():
    payload = request.json  # Получаем JSON-данные из запроса
    function_name = payload.get('function')  # Извлекаем значение поля 'function'

    if function_name == 'function_one':
        result = function_one(payload)
    elif function_name == 'function_two':
        result = function_two(payload)
    else:
        return jsonify({"error": "Function not found"}), 404

    return jsonify(result), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
