from flask import Flask, jsonify, abort, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='server.log', level=logging.INFO)

# Define the endpoints
@app.route('/people/<int:id>/', methods=['GET'])
def get_person(id):
    # Log the requested URL
    logging.info(f"Received request: {request.url}")

    if id > 100:
        # Return 404 Not Found with a JSON body
        response = jsonify({'error': 'Person not found'})
        return response, 404

    # Return a JSON response for the person
    response = jsonify({
        'id': id,
        'name': 'John Doe',
        'age': 30
    })
    return response

@app.route('/planets/<int:id>/', methods=['GET'])
def get_planet(id):
    # Log the requested URL
    logging.info(f"Received request: {request.url}")

    if id > 100:
        # Return 404 Not Found with a JSON body
        response = jsonify({'error': 'Planet not found'})
        return response, 404

    # Return a JSON response for the planet
    response = jsonify({
        'id': id,
        'name': 'Earth',
        'population': '7.9 billion'
    })
    return response

@app.route('/starships/<int:id>/', methods=['GET'])
def get_starship(id):
    # Log the requested URL
    logging.info(f"Received request: {request.url}")

    if id > 100:
        # Return 404 Not Found with a JSON body
        response = jsonify({'error': 'Starship not found'})
        return response, 404

    # Return a JSON response for the starship
    response = jsonify({
        'id': id,
        'name': 'Millennium Falcon',
        'pilots': ['Han Solo', 'Chewbacca']
    })
    return response

if __name__ == '__main__':
    app.run()

