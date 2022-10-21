from werkzeug.security import generate_password_hash

def db_register(username, password, db):

    pass_hash = generate_password_hash(password)

    sql = "INSERT INTO users (username, password) VALUES (:username, :password) RETURNING id"

    result = db.session.execute(sql, {"username" :username, "password" :pass_hash})
    id = result.fetchone()[0]

    sql = "INSERT INTO account (account_id, last_logged, create_date) VALUES (:account_id, NULL, CURRENT_DATE)"
    db.session.execute(sql, {"account_id":id})

    db.session.commit()

def db_login(username, db):
        query = "SELECT id,password FROM users WHERE username=:username"
        result = db.session.execute(query, {"username": username})
        
        user = result.fetchone()

        return user
        
def db_add_expense(name, category, date, amount, info, db, user_id):
    sql = "INSERT INTO expense (name,amount,category_id,date,added,comment) VALUES (:name,:amount,(SELECT category.id FROM category WHERE category.category=:category),:date,NOW(),:comment) RETURNING id"

    result = db.session.execute(sql, {"name" :name, "amount" :amount, "category" :category, "date" :date, "comment" :info,"user_owner" :user_id})
    expense_id = result.fetchone()[0]

    if expense_id:
        sql = "INSERT INTO expenses (user_owner, expense_id) VALUES (:user_owner, :expense_id)"
        db.session.execute(sql, {"user_owner":user_id, "expense_id": expense_id})

    db.session.commit()

def db_update_logged_in(user_id, db):

    sql = "UPDATE account SET last_logged=NOW() WHERE account_id=:user_id"
    db.session.execute(sql, {"user_id": user_id})
    db.session.commit()

def db_get_date(user_id, db):
    sql = "SELECT last_logged FROM account WHERE account_id=:user_id"
    result = db.session.execute(sql, {"user_id": user_id})
    date = result.fetchone()[0]
    
    return date
   