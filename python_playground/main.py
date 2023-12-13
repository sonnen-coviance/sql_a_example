from flask import Flask, request

from python_playground.models import A, B, db

app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:postgres@localhost:5432/postgres"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def root():
    return "ok"


@app.route("/a", methods=["GET"])
def get_as():
    return [a.to_dict() for a in db.session.query(A).all()]


@app.route("/b", methods=["GET"])
def get_bs():
    return [b.to_dict() for b in db.session.query(B).all()]


@app.route("/a", methods=["POST"])
def create_a():
    name = request.json.get("name")
    a = A(name=name)
    db.session.add(a)
    db.session.commit()
    return "success"


@app.route("/a/<id>", methods=["DELETE"])
def delete_a(id):
    a = db.session.query(A).filter(A.id == id).first()
    if a:
        db.session.delete(a)
        db.session.commit()
        return "success", 200
    else:
        return "Entity not found", 404


@app.route("/a/<id>", methods=["PATCH"])
def patch_a(id):
    body = request.json
    a = db.session.query(A).filter(A.id == id).first()
    if a:
        for key, value in body.items():
            if key == "bs":
                a.update_bs(value)
            elif hasattr(a, key):
                setattr(a, key, value)
        db.session.commit()
        return "success", 200
    else:
        return "Entity not found", 404


@app.route("/a/<id>", methods=["GET"])
def get_a_by_id(id):
    a = db.session.query(A).filter(A.id == id).first()
    if a:
        return a.to_dict(), 200
    else:
        return "Entity not found", 404
