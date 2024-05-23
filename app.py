import flask; 
from selenium import webdriver;  # This will raise an ImportError if selenium is not installed
from urllib.parse import urlparse
import sqlite3
from flask import jsonify
import uniqlo

app = flask.Flask(__name__)

#initialize stores
uniqlo_store = uniqlo.Uniqlo()


#end points
@app.route('/get_products', methods=['GET'])
def get_products():
    store = flask.request.args.get('store',default=None)
    price_range = flask.request.args.get('price_range',default=None)

    try:
        # check filtering arguments 
        if store is None and price_range is None:
            query = 'SELECT * FROM products'
            results = execute_query_to_db(query=query, values=())
        elif price_range is None: 
            query = 'SELECT * FROM products WHERE store = ?'
            results = execute_query_to_db(query=query, values=(store,))
        elif store is None:
            query = 'SELECT * FROM products WHERE price <= ?'
            results = execute_query_to_db(query=query, values=(price_range,))
        else:
            query = 'SELECT * FROM products WHERE store = ? AND price <= ?'
            results = execute_query_to_db(query=query, values=(store, price_range))
    except sqlite3.Error as e:
        return str(e), 500

    print(results)
    results_json = jsonify(results)

    return results_json, 200

@app.route('/update_information', methods=['PUT'])
def update_products():

    product_ids = flask.request.args.get('product_ids')
    if product_ids is not None:
        product_ids = product_ids.split(',')

#grab product URL
    try:
        conn = sqlite3.connect('project_db')
        c = conn.cursor()

        query = 'SELECT URL FROM products WHERE id IN ({})'.format(','.join('?' for _ in product_ids))
        c.execute(query, product_ids)

        urls = c.fetchall()

        #close resources
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        return str(e), 500

    #check which store the URL is from and scrape using the associated methods

    for url in urls:
        URL_root = get_URL_root(url)

        #select which store to scrape from TODO: add more cases when more stores get implemented
        if URL_root == 'uniqlo.com':
            uniqlo_store.update_information(url)
        else:
            return URL_root, 400
        
    return "Product upated successfully", 200
        


@app.route('/delete_product/<product_ids>', methods=['DELETE'])
def delete_product(product_ids):
    """
    Deletes one or more products from the database.

    Args:
        product_ids (str): Comma-separated string of product IDs to be deleted.

    Returns:
        str: A success message indicating that the product(s) have been deleted successfully, or an error message if an exception occurs.
    """
    product_ids = product_ids.split(',')

    try:
        conn = sqlite3.connect('project_db')
        c = conn.cursor()

        query = 'DELETE FROM products WHERE id IN ({})'.format(','.join('?' for _ in product_ids))
        c.execute(query, product_ids)

        conn.commit()
    except sqlite3.Error as e:
        return str(e), 500   
    
    return 'Product deleted successfully', 200


@app.route('/add_product', methods=['POST'])
def add_product():
    product_url = flask.request.args.get('product_url', default=None)

    URL_root = get_URL_root(product_url)
    print(URL_root)

    #select which store to scrape from TODO: add more cases when more stores get implemented
    if URL_root == 'www.uniqlo.com':
        scrape = uniqlo_store.scrape_product(product_url)
        print(scrape)
    else:
        return "URL not found", 400
    
    return 'Product added successfully', 200
    

#helper functions
def get_URL_root(URL): 
    #valid domains this app recognizes --> can be expanded
    valid_domains = execute_query_to_db('SELECT domain FROM stores', ())

    #parse the URL
    domain = urlparse(URL).netloc

    #check if the domain is valid
    if domain in valid_domains:
        print(domain)
        return domain
    else:
        return None
    
def execute_query_to_db(query, values):
    try:
        conn = sqlite3.connect('project_db')
        c = conn.cursor()

        c.execute(query, values)
        results = c.fetchall()

        conn.commit()
    except sqlite3.Error as e:
        return str(e), 500
    finally:
        c.close()
        conn.close()

    return results


app.run(port=5000, debug=True)