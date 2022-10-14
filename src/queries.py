from werkzeug.security import generate_password_hash

def db_register(username, password, db):

    pass_hash = generate_password_hash(password)

    sql = "INSERT INTO users (username, password) VALUES (:username, :password)"

    db.session.execute(sql, {"username" :username, "password" :pass_hash})
    db.session.commit()

def db_login(username, password, db):
        query = "SELECT id,password FROM users WHERE username=:username"
        result = db.session.execute(query, {"username": username})
        
        user = result.fetchone()

        return user
        
def db_add_expense(name, category, date, amount, info, db, user_id):
    sql = "INSERT INTO expenses (name,amount,category,date,added,comment,user_owner) VALUES (:name,:amount,:category,:date,NOW(),:comment,:user_owner)"

    db.session.execute(sql, {"name" :name, "amount" :amount, "category" :category, "date" :date, "comment" :info,"user_owner" :user_id})
    db.session.commit()