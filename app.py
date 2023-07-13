from flask import Flask, redirect, render_template, flash, jsonify, request
from models import db, connect_db, Cupcake, serialized_cupcakes
from flask_debugtoolbar import DebugToolbarExtension
from forms import CupcakeFrom
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)

app.config['SECRET_KEY'] = 'Naruto7'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config["SECRET_KEY"] = 'NARUTO7'
debug = DebugToolbarExtension(app)

ctx = app.app_context()
ctx.push()




@app.route("/", methods =["GET", "POST"])
def home():
    form = CupcakeFrom()
    if form.validate_on_submit():
    #   flavor =  form.data.flavor
    #   size =  form.data.size
    #   rating =   form.data.rating
    #   image =  form.data.ima.get
    #   cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    #   db.session.add(cupcake)
    #   db.session.commit()
      return redirect('/')
    else:
      return render_template("home.html", form = form)

@app.route('/api/cupcakes')
def cupcake_list():
    cupcakes = Cupcake.query.all()
    serialized = [ serialized_cupcakes(c) for c in cupcakes]
    return jsonify(cupcakes=serialized)


@app.route('/api/cupcakes/<int:cupcake_id>')
def cupcake_detail(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized =  serialized_cupcakes(cupcake)
    return jsonify(cupcake=serialized)


@app.route('/api/cupcakes', methods = ["POST"])
def create_cupcake():
    # form = CupcakeFrom
    # if form.validate_on_submit():
    flavor = request.json["flavor"]   
    size = request.json["size"]   
    rating = request.json["rating"]   
    image = request.json["image"]   
    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(cupcake)
    db.session.commit()
    serialized = serialized_cupcakes(cupcake)
    (jsonify(cupcake=serialized), 201)
    redirect('/')

@app.route('/api/cupcakes/<int:cupcake_id>', methods = ["PATCH"])
def edit_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)  
    cupcake.size = request.json.get("size", cupcake.size)  
    cupcake.rating = request.json.get("rating", cupcake.rating)  
    cupcake.image = request.json.get("image", cupcake.image)    
    db.session.commit()
    serialized = serialized_cupcakes(cupcake)
    return (jsonify(cupcake=serialized), 200)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message = "Deleted")