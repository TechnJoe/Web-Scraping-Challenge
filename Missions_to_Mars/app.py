
# Dependencies and Setup
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars
import os

#create an instance of Flask
app = Flask(__name__)

#mongodb connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)

 
@app.route("/scrape")
def web_scrape():
    db = mongo.db.mars
    #db.collection.remove({})
    mars_data = scrape.scrape()
    db.collection.insert_one(mars_data)
    return  render_template('scrape.html')  

    if __name__ == "__main__":
        app.run() 