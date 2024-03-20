import warehouse
import data_transfer
import csv
from flask import Flask, render_template, redirect 
    
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/list_products')
def list_products():
    list = []
    data_transfer.load_items_from_csv(list)
    return  render_template('list_product.html', list=list) 
    
#load_items_from_csv()
#while True:
 #   question = input("What would u like to do? ")

 #   if question == "exit":
 #       print("Exiting... Bye!")
 #       break
 #   if question == "show":
 #       get_items()
 #   if question == "add":
 #       add_items()
 #   if question == "sell":
 #       sell_items()
 #   if question == "show_revenue":
 #       show_revenue()
 #   if question == "save":
 #       export_items_to_csv()
 #       export_sales_to_csv()
 #  if question == "load":
 #       load_items_from_csv()


if __name__ == '__main__':
    app.run(debug=True)
