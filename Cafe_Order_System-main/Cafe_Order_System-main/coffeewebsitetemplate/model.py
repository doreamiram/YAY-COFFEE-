import os
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

# יצירת אובייקט SQLAlchemy
db = SQLAlchemy()

# הגדרת תיקיית העלאת קבצים
UPLOAD_FOLDER = 'static/uploads/'

# יצירת התיקייה במידת הצורך
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# מודל משתמשים
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=False)

# הוספת משתמשים
def add_user(username, password, role):
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        print(f"User '{username}' already exists.")
    else:
        new_user = User(username=username, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()

# אימות משתמשים
def authenticate_user(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return user.role  # מחזיר את התפקיד של המשתמש (role)
    else:
        return None

# מתפעל
# model.py

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(80), nullable=False)
    items = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Open')

# פונקציה לקבלת הזמנות פתוחות
def get_open_orders():
    return Order.query.filter_by(status='Open').all()

# פונקציה לסגירת הזמנה
def close_order(order_id):
    order = Order.query.get(order_id)
    if order:
        order.status = 'Closed'
        db.session.commit()

# פתיחת הזמנה חדשה
def new_order(customer_name, items):
    new_order = Order(customer_name=customer_name, items=items, status="Open")
    db.session.add(new_order)
    db.session.commit()

class Items(db.Model):
    __tablename__ = 'Items'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)


def add_new_item(item_name, description, price):
    new_item = Items(item_name=item_name, description=description, price=price)
    db.session.add(new_item)
    db.session.commit()


class Review(db.Model):
    __tablename__ = 'Review'
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(255), nullable=True)  # עדכון העמודה לסוג String כדי לשמור נתיב


# הגדרת תיקיית העלאת קבצים
UPLOAD_FOLDER = 'static/uploads/'  # המיקום שבו הקבצים יישמרו
UPLOAD_FOLDER = 'static/uploads/'

# בדיקת הרשאת כתיבה לתיקייה
if os.access(UPLOAD_FOLDER, os.W_OK):
    print("התיקייה ניתנת לכתיבה.")
else:
    print("התיקייה לא ניתנת לכתיבה.")

# פונקציה לבדוק אם הסיומת מותרת
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# פונקציה לשמירת ביקורת עם תמונה
def add_review(review, rating, photo):
    # שמירת נתיב הקובץ
    photo_path = None
    if photo and photo.filename != '' and allowed_file(photo.filename):
        # יצירת שם קובץ בטוח לשמירה
        filename = secure_filename(photo.filename)
        # יצירת נתיב לשמירת הקובץ
        photo_path = os.path.join(UPLOAD_FOLDER, filename)
        # שמירת הקובץ בתיקיית ה-uploads
        photo.save(photo_path)
        print(f"File saved at: {photo_path}")  # יראה את הנתיב המלא של הקובץ

    # יצירת אובייקט הביקורת ושמירתו עם הנתיב לתמונה
    new_review = Review(review=review, rating=rating, photo=photo_path)
    db.session.add(new_review)
    db.session.commit()