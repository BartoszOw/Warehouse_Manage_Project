import warehouse
import forms
from flask import Flask, render_template, redirect, request, url_for
    
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SECRET_KEY'] = 'dwadadsadwadawdasdawd'


filename = 'dane/magazyn.csv'
ITEMS = warehouse.load_products_from_csv(filename)

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

@app.route('/sell/<product_name>', methods=["GET", "POST"])
def sell_product(product_name):
    product = next((item for item in ITEMS if item.name == product_name), None)
    form_sell = forms.ProductSaleForm()

    if request.method == "POST":

        if form_sell.validate_on_submit():
            quantity_to_sell = int(form_sell.quantity_sell.data)
            if int(product.quantity) < int(quantity_to_sell):
                return redirect('sell_product')
            
            product.quantity = int(product.quantity) - quantity_to_sell

            if product.quantity == 0:
                ITEMS.remove(product)

            warehouse.export_product_to_csv(ITEMS)
            return redirect(url_for('list_products'))
    
    return render_template('sell_product.html', form_sell=form_sell, product_name=product_name)





if __name__ == '__main__':
    app.run(debug=True)
