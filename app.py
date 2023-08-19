from flask import Flask, jsonify, request, render_template
from models import db, Cupcake
from flask_cors import CORS  # Import the CORS class

app = Flask(__name__)
CORS(app)  # Enable CORS for your app

# Configure the database settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create the tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/cupcakes', methods=['GET'])
def get_cupcakes():
    cupcakes = Cupcake.query.all()
    cupcakes_data = [cupcake.to_dict() for cupcake in cupcakes]
    return jsonify(cupcakes=cupcakes_data)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    data = request.json
    new_cupcake = Cupcake(flavor=data['flavor'], size=data['size'], rating=data['rating'], image=data.get('image', Cupcake.DEFAULT_IMAGE))
    db.session.add(new_cupcake)
    db.session.commit()
    return jsonify(cupcake=new_cupcake.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)


