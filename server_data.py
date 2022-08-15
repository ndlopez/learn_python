# Serving data with Flask
# $ pip install Flask
# server_data.py
from flask import Flask, render_template
app = Flask(__name__)

winners = [{'name':'Albert Einstein','category':'Physics'},
           {'name':'Mario Vargas Llosa','category':'Literature'},
           {'name':'Gabriela Mistral','category':'Literature'}]

@app.route("/demolist")
def demo_list():
    return render_template('server_data.html',heading="A lil' winners list",winners=winners)
#server_data.html is located at "templates" folder
#def hello():
#    return("Hello worjl")

if __name__ =="__main__":
    app.run(port=8000,debug=True) #http://localhost:8000
    
