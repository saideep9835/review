from datetime import timedelta,date
from flask import Flask, render_template, request, session, url_for, redirect, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_

from model import *
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:reddy123@localhost:5432/book'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "1c488f4b4a21cd7fbc5007664656985c2459b2362cf1f88d44b97e750b0c14b2cf7bc7b792d3f45db"

db.init_app(app)
def main():
    db.create_all()
   
    
    
if __name__ == "__main__":
    with app.app_context():
        main()
        
        
# @app.route("/")
# def index():
#     return render_template("search1.html")

@app.route("/api/search/<string:word>",methods=["GET","POST"])
def search(word):
    
    s = Test.query.filter(or_(Test.isbn==word,Test.author==word,Test.title==word,Test.year==word))
    a = []
    flag=0
    for i in s:
        d = {}
        d["isbn"]=i.isbn
        d["author"]=i.author
        d["title"]=i.title
        d["year"]=i.year
        
        a.append(d)
        flag=1
    if flag == 0:
        return jsonify({"Error":"Books not found"}), 404
    return jsonify({"Test":a}), 200
@app.route("/api/review",methods=["GET","POST"])
def review():
    a = Review.query.all()
    #a = Review.query.filter(or_(Review.isbn==w,Review.user==w))
    b = []
    flag = 0
    for i in a:
        d = {}
        d["user"]=i.user
        d["isbn"]=i.isbn
        d["rating"]=i.rating
        d["review"]=i.review
        b.append(d)
        flag=1
    if flag == 0:
        return jsonify({"Error":"Reviews not found"}), 404
    return jsonify({"Review":b}), 200

        