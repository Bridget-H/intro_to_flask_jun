from app import app, db
from flask import jsonify, request
from app.models import User, Post
@app.route('/api/users')
def users():
     """
     [GET] /API/USERS
     """
     users = [u.to_dict() for u in User.query.all()]
     return jsonify(users=users) #bc it's a list in python, so we turn a list into and object here
   # returning a json response
@app.route('/api/create-user', methods=['POST'])  #post request ENDING tag for this route
# we want to get data from request to build/adduser
def create_user():
    """
    [POST]
    """
    data = request.get_json()
    print(data) #check parse data as JSON(as a dict)
    # print(type(data)) #dict
    # print(data["test1"]) #dict prints
    # print(type(data["test1"])) #returns an int
    username = data.get('username')
    email = data.get("email")
    password = data.get("password")
    if not username or not email or not password:
        return jsonify({"error": "incorrect username/email/password"}), 400
    #add new user
    new_user = User(username, email, password) #new instance of user object
    db.session.add(new_user)
    db.session.commit()
    # return "Hello World!"
    return jsonify(new_user.to_dict())
    #ADDED TO DB VIA POST REQUEST
@app.route('/api/posts') #return json object of posts
def posts():
    posts = [i.dict2()] for i in Post.query.all()]
    return jsonify(posts=posts)


@app.route('/api/create-post', methods=['POST'])
def create_post():
    data = request.get_json()
    print(data)
    title = data.get("title")
    body = data.get("body")
    user_id = data.get("user_id")
    new_post = Post(title, body, user_id)
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.dict2())


