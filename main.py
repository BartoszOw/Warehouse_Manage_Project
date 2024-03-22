import warehouse
import forms
from flask import Flask, render_template, redirect, request, url_for
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dwadadsadwadawdasdawd'

ITEMS = warehouse.load_products_from_csv('dane/magazyn.csv')

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/list_products', methods=["GET", "POST"])
def list_products():
    product_form = forms.ProductForm()
    if request.method == "POST":
        if product_form.validate_on_submit():
            name = request.form.get('name')
            quantity = int(request.form.get('quantity'))
            unit = request.form.get('unit')
            unit_price = float(request.form.get('unit_price'))
            
            new_product = warehouse.Product(name, quantity, unit, unit_price)
            ITEMS.append(new_product)

            warehouse.export_product_to_csv(ITEMS)
        return redirect(url_for('list_products'))
    return  render_template('list_product.html', list=ITEMS, product_form=product_form) 



if __name__ == '__main__':
    app.run(debug=True)
