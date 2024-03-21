import warehouse
from flask import Flask, render_template
    
app = Flask(__name__)


ITEMS = warehouse.load_products_from_csv('dane/magazyn.csv')

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/list_products')
def list_products():
    return  render_template('list_product.html', list=ITEMS) 
    

if __name__ == '__main__':
    app.run(debug=True)
