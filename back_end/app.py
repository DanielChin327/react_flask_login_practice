# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy

import sqlalchemy

db = sqlalchemy.create_engine("mariadb+pymysql://root:@localhost:3306/northwinddb", echo = True)

def get_customers():
    with db.connect() as conn:
        result = conn.execute(sqlalchemy.text("SELECT * FROM moviedb"))
        print(result.all())

def main():
    get_customers()
if __name__ == '__main__':
    main()
