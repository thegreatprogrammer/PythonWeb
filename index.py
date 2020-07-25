from flask import flask
from flask import  render_template

# archivo principal
app = Flask(__name__)

# creamos las rutas usando la variable app
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# activamos el servidor
if __name__ == '__main__':
    # Para no tener que estar reiniciando el servidor
    app.run(debug=True)