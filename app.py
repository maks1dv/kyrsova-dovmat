from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('sto.db')
    conn.row_factory = sqlite3.Row  
    return conn

# Головна сторінка для клієнта
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    
    if request.method == 'POST':
        client_name = request.form['client_name']
        phone = request.form['phone']
        service_id = request.form['service_id']
        
        conn.execute('INSERT INTO orders (client_name, phone, service_id) VALUES (?, ?, ?)',
                     (client_name, phone, service_id))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))

    services = conn.execute('SELECT * FROM services').fetchall()
    conn.close()
    return render_template('index.html', services=services)

# Сторінка панелі адміністратора
@app.route('/admin')
def admin():
    conn = get_db_connection()
    # Об'єднуємо таблиці, щоб вивести назву послуги замість її ID
    orders = conn.execute('''
        SELECT orders.id, orders.client_name, orders.phone, services.name AS service_name, services.price
        FROM orders
        JOIN services ON orders.service_id = services.id
    ''').fetchall()
    conn.close()
    return render_template('admin.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)