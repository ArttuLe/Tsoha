import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from os import getenv
from io import BytesIO

from db import db

def db_conn():
    db_uri = getenv("DATABASE_URL")

    if db_uri.startswith("postgres://"):
        db_uri = db_uri.replace("postgres://", "postgresql://", 1)
    return create_engine(db_uri, echo=False)

def get_expenses(user_id):
    conn = db_conn()
    result = pd.read_sql_query(('''SELECT * FROM expenses WHERE user_owner={}''').format(user_id), conn)

    data = pd.DataFrame(result, columns = ['name', 'amount', 'category', 'date', 'added', 'comment'])
    
    return data

def get_monthly(user_id):

    conn = db_conn()

    result = pd.read_sql_query(('''SELECT SUM(amount) as Total, EXTRACT(month from date) AS Month FROM expenses  WHERE user_owner={} GROUP BY month''').format(user_id), conn)
    data = pd.DataFrame(result)
    return data

def generate_pie(user_id):

    data = get_expenses(user_id)

    df = data.groupby("category").sum()
    plt.pie(df["amount"], labels=df.index, autopct='%1.1f%%')

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)

    return img
    

    
    