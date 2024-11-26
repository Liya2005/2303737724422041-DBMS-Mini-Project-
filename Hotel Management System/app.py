from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'hotel_secret_key'

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'hotel_management'
mysql = MySQL(app)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hotels')
def hotels():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM hotel_details")
    hotel_info = cur.fetchall()
    cur.close()
    return render_template('hotels.html', hotels=hotel_info)

@app.route('/search', methods=['POST', 'GET'])
def search():
    search_results = []
    if request.method == "POST":
        search_term = request.form['hotelid']
        cur = mysql.connection.cursor()
        query = "SELECT * FROM hotel_details WHERE id LIKE %s"
        cur.execute(query, ('%' + search_term + '%',))
        search_results = cur.fetchmany(size=1)
        cur.close()
    return render_template('hotels.html', hotels=search_results)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']
        rooms_available = request.form['rooms_available']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO hotel_details (name, location, description, rooms_available) VALUES (%s, %s, %s, %s)",
                    (name, location, description, rooms_available))
        mysql.connection.commit()
        return redirect(url_for('hotels'))

@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM hotel_details WHERE id = %s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('hotels'))

@app.route('/update', methods=['POST'])
def update():
    if request.method == "POST":
        id_data = request.form['hotelid']
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']
        rooms_available = request.form['rooms_available']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE hotel_details
            SET name = %s, location = %s, description = %s, rooms_available = %s
            WHERE id = %s
        """, (name, location, description, rooms_available, id_data))
        mysql.connection.commit()
        return redirect(url_for('hotels'))

if __name__ == "__main__":
    app.run(debug=True)
