from flask import render_template, request, Blueprint
from flaskpitch.models import Post
import requests

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():

    random_quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'
    quote_response = requests.get(random_quote_url) 
    quote_data = quote_response.json()

    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, quote_data=quote_data)


@main.route("/about")
def about():
    return render_template('about.html', title='About')