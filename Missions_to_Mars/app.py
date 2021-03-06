# Dependencies and Setup
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

#create an instance of Flask
app = Flask(__name__,template_folder='template')
#app = Flask(__name__)
#mongodb connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#db = PyMongo.mars

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)

 
@app.route("/scrape")
def web_scrape():
    db = mongo.db.mars
    #db.collection.remove({})
    mars_data = scrape_mars.scrape()
    db.collection.insert_one(mars_data)
    #Update the Mongo database using update and upsert=True
    #mongo.db.collection.update({}, mars_data, upsert=True)
    #db.update({},mars_data, upsert=True)
    return "Scraping Sucessfull!"
     
if __name__ == "__main__":
    app.run(debug=True) 


