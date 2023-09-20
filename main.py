from flask import Flask, render_template, request,jsonify
import mysql.connector
app=Flask(__name__,template_folder='Templates')

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test"
    )
#print(mydb)
cursor=mydb.cursor()



bus_route_data = [
    { "id": 1, "busNumber": "101", "route": "narhe to nanded city", "departureTime": "07:00 AM", "arrivalTime": "08:00 AM" },
    { "id": 2, "busNumber": "202", "route": "narhe to kothrude", "departureTime": "07:00 AM", "arrivalTime": "08:30 AM" },
    { "id": 3, "busNumber": "303", "route": "narhe to warje", "departureTime": "07:20 PM", "arrivalTime": "08:3S0 PM" }

]

@app.route('/api/routes',methods=['GET'])
def get_routes():
    return jsonify(bus_route_data)

@app.route('/api/routes/<int:route_id>', methods=['PUT'])
def update_route(route_id):
    for route in bus_route_data:
        if route['id'] == route_id:
            data = request.json
            route.update(data)
            return jsonify(route)
    return jsonify({"error": "Route not found"}), 404


@app.route('/student_route')
def student_route():
    return render_template('student_route.html', bus_route_data=bus_route_data)

@app.route('/admin_route',methods=['POST','GET'])
def admin_route():
    if request.method == 'POST':
        busNumber = request.form.get('busNumber')
        route = request.form.get('route')
        departureTime = request.form.get('departureTime')
        arrivalTime = request.form.get('arrivalTime')
        cursor.execute(
            """ INSERT INTO `routs`(`busNumber`,`route`,`departureTime`,`arrivalTime`) VALUES('{}','{}','{}','{}')""".format(
                busNumber, route, departureTime, arrivalTime))
        mydb.commit()
    return render_template('admin_route.html')


@app.route('/register',methods=['POST','GET'])
def reg():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        department = request.form.get('department')
        phone = request.form.get('phone')
        email = request.form.get('email')
        gender = request.form.get('gender')
        password = request.form.get('password')
        conpassword = request.form.get('conpassword')
        cursor.execute(
            """ INSERT INTO `students`(`firstname`,`lastname`,`phone`,`email`,`gender`,`department`,`password`,`conpassword`) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')""".format(
                firstname, lastname,phone,email,gender,department,password,conpassword))
        mydb.commit()

    return render_template('register.html')



@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
    return render_template('student_login.html')

@app.route('/card', methods=['GET', 'POST'])
def card():
    return render_template('card.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    return render_template('booking.html')

@app.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    return render_template('adminlogin.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('logout.html')

@app.route('/admin_bus', methods=['GET', 'POST'])
def admin_bus():
    if request.method == 'POST':
        busname = request.form.get('bn')
        busnumber = request.form.get('busn')
        cursor.execute(
            """ INSERT INTO `busdetail`(`bn`,`busn`) VALUES('{}','{}')""".format(busname, busnumber))
        mydb.commit()
    return render_template('admin_bus.html')

@app.route('/student', methods=['GET', 'POST'])
def student():
    return render_template('student.html')

'''cursor.execute("SELECT * FROM students")

myresult = cursor.fetchall()

for x in myresult:
  print(x)'''



@app.route('/fetchdata')
def fetch():
    cursor.execute("SELECT * FROM students")
    stud = cursor.fetchall()
    return render_template('fetchdata.html',stud=stud,x=len(stud))







app.run(debug=True,port=8080)

