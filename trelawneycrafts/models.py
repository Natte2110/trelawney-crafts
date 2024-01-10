from trelawneycrafts import db

class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(32), unique=True, nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Username: {1} | Password: {2} | Admin: {3}".format(
            self.id, self.username, self.password, self.admin
        )
        
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return "#{0} - Category: {1}".format(
            self.id, self.category_name
        )
    
class Post(db.Model):
    # schema for the Post model
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    image_url = db.Column(db.String(100), unique=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return "#{0} - Date: {1} | Posted By: {2} | Image: {3} | Category: {4}".format(
            self.id, self.date, self.user_id, self.image_url, self.category_id
        )
        
class Reaction(db.Model):
    # schema for the Reaction model
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return "#{0} - Date: {1} | Reacted By: {2} | On Post ID: {3}".format(
            self.id, self.date, self.user_id, self.post_id
        )
        
class Comment(db.Model):
    # schema for the Comment model
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return "#{0} - Date: {1} | Reacted By: {2} | On Post ID: {3} | Comment Content: {4}".format(
            self.id, self.date, self.user_id, self.post_id, self.content
        )