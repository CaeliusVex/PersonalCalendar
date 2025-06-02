from flask import Flask, render_template, request, jsonify
import utils
import utils.utils
app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')  # Sends index.html to the client

# Route to handle the click coordinates
@app.route('/check_task', methods=['POST'])
def check_task():
    data = request.get_json()
    x = int(data['x'])
    y = int(data['y'])
    loc = (int(y/(100/6)))*5+int(x/20)+1
    task = utils.utils.get_task(loc)
    return jsonify({
        'status': 'success',
        'message': 'Click received',
        'loc': loc,
        'task':task
    })
@app.route('/edit', methods=['POST'])
def edit():
    data = request.get_json()
    loc = int(data['loc'])
    task = data['task']
    result = utils.utils.edit_task(loc,task)
    return jsonify({
        'status': result,
        'message': 'Click received'
    })
if __name__ == '__main__':
    app.run(host="0.0.0.0",port="9999")  # Run in development mode