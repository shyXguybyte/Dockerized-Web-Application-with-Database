# render the template of the page.
from flask import Flask, render_template, request
#connect to the database.
import mysql.connector

#function to fetch data from the database
def get_connection():
    return  mysql.connector.connect(
    host = "mysql",
    user = "root" ,
    password = "1234",
    database = "student"
    )


app = Flask(__name__)

@app.route('/')
def form():

    return render_template('form.html')

@app.route('/submit_form' , methods=['POST'] )
def submit_form():
    if request.method == 'POST' :
        first_name= request.form['first_name']
        second_name= request.form['second_name']
        st_id= request.form['id']
        cgpa = request.form['cgpa']

    
    try : 
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO student(std_f_name , std_s_name , std_id , std_cgpa) VALUES(%s ,%s ,%s  ,%s )" ,(first_name,second_name,st_id ,cgpa) )
        conn.commit()
        cursor.close()
        conn.close()

        return index()
        
    except Exception as e :
        return str(e)
    

def get_data():
    conn = mysql.connector.connect(
    host = "mysql",
    user = "root" ,
    password = "1234",
    database = "student"

    )
    cursor = conn.cursor()

    #execute the query that will return all the data.
    cursor.execute("select * from student")
    data = cursor.fetchall()

    # close connection .
    cursor.close()
    conn.close()
    return data

#Route to display data 
@app.route('/index' )
def index():
    data = get_data()
    return render_template('index.html', data = data )


if __name__ == "__main__":
    app.run(debug=True , host="0.0.0.0" , port=5050)
else:
    print("no")