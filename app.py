from flask import Flask, render_template, request, jsonify
from bot.tiktok_bot import send_bulk_dms

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-dms', methods=['POST'])
def send_dms():

    usernames = request.form.get('usernames')
    message = request.form.get('message')

    user_list = usernames.split('\n')

    result = send_bulk_dms(user_list, message)

    return jsonify({
        'status': result
    })

if __name__ == '__main__':
    app.run(debug=True)