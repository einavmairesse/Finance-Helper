from flaskext.mysql import MySQL

from FinanceTracker import app
from FinanceTracker.routes.expenses import expenses_blueprint

if __name__ == '__main__':
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
    app.config['MYSQL_DATABASE_DB'] = 'tracker'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

    conn = mysql.connect()
    cursor = conn.cursor()

    app.register_blueprint(expenses_blueprint)

    app.run()
