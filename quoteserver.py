from flask import Flask, jsonify, request, abort, render_template
# Import library for authentication
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
# Import Database Access Objec and rowCounter for random number generation
from quoteDAO import quoteDAO
import rowCounter as rc

app = Flask(__name__, static_url_path='/quoteViewer.html', static_folder='.')


### Testing Authentication
basicAuth = HTTPBasicAuth()
users = {
"user1": generate_password_hash("pass1"),
"andy1": generate_password_hash("pass2")
}
@basicAuth.verify_password
def verify_password(username, password):
    if username in users and \
    check_password_hash(users.get(username), password):
        return username
@app.route('/')
@basicAuth.login_required
def index():
    return render_template('quoteViewer.html')
    return "Hello, %s!" % basicAuth.current_user()




## End Authentication testing

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

# Testing random quote

# 

# Gives all quotes
#curl "http://127.0.0.1:5000/quotes"
@app.route('/quotes')
def getAll():
    #print("in getall")
    results = quoteDAO.getAll()
    return jsonify(results)

# Gives a random quote by id
@app.route('/quotes/<int:id>')
def getRandQuote(rc):
    randQuote = quoteDAO.getRandQuote(rc)
    return jsonify(randQuote)

# Gives quote with id of 1
#curl "http://127.0.0.1:5000/quotes/1"
@app.route('/quotes/<int:id>')
def findById(id):
    foundQuote = quoteDAO.findByID(id)

    return jsonify(foundQuote)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"quote\":\"Let it be\",\"author\":\"Paul McCartney\"}" http://127.0.0.1:5000/quotes
@app.route('/quotes', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    quote = {
        "quote": request.json['quote'],
        "author": request.json['author'],
    }
    values =(quote['quote'],quote['author'])
    newId = quoteDAO.create(values)
    quote['id'] = newId
    return jsonify(quote)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books/1
@app.route('/quotes/<int:id>', methods=['PUT'])
def update(id):
    foundQuote = quoteDAO.findByID(id)
    if not foundQuote:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'quote' in reqJson:
        foundQuote['quote'] = reqJson['quote']
    if 'Author' in reqJson:
        foundQuote['author'] = reqJson['author']
    values = (foundQuote['quote'],foundQuote['author'],foundQuote['id'])
    quoteDAO.update(values)
    return jsonify(foundQuote)
        

    

@app.route('/quotes/<int:id>' , methods=['DELETE'])
def delete(id):
    quoteDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)