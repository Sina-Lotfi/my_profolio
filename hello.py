from flask import Flask
from flask import render_template, redirect
from flask import request
from flask import url_for
import csv
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


#def write_to_file(data):
    #with open('database.txt', mode="a") as databse:
        #email = data["email"]
        #message = data["message"]
        #subjet = data["subject"]
        #file = databse.write(f'email: {email}, subject: {subjet}, message:{message} \n')
def write_csv(data):
    with open("D:\Codes\Web\database.csv", mode="a", newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
@app.route("/submit_form", methods=["GET", "POST"])
def summit():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_csv(data)
            return redirect("/thankyou.html")
        except:
            return "somthing went wrong"
    else:
        return "somthing went wrong please check!"
