from flask import Blueprint, request
import requests
from ..models import User, Product

api=Blueprint('api', __name__)

@api.route('/addtodb')
def add_products():
    url = "https://fakestoreapi.com/products"

    response = requests.get(url)
    print(response.json())
    prod_dicts = response.json()
    for p in prod_dicts:
        prod = Product(title = p['title'], description = p['description'], category=p['category'], 
                       image = p['image'], price = p['price'], rating = p['rating']['rate'], rating_count = p['rating']['count'])
        prod.saveProduct()
    return "products saved to db"

@api.route('/products')
def allproducts():
    prods = Product.query.all()
    prod_list=[]
    for p in prods:
       prod_list.append({'id': p.id, 'title': p.title, 'price': p.price, 'description': p.description, 'image': p.image, 'category': p.category, 'rating': p.rating, 'rating_count': p.rating_count})
    return {'status': 'ok', 'data': prod_list, 'item_count': len(prod_list)}

@api.post('/product')
def product():
    productId= request.json.get('ProductId')

    prod = Product.query.filter_by(id=productId).first()
    return({"id":prod.id, "title": prod.title, "image": prod.image, "description":prod.description, "price": prod.price, 'category': prod.category, "rating": prod.rating, "rating_count": prod.rating_count})