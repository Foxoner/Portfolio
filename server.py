from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import os
import csv


import smtplib



app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)



def write_to_csv(data):
    with open('../database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #Start Email
            msg = 'Email - {}; Subject - {}; Message - {}'.format(data['email'],data['subject'],data['message'])
            with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login('vtestingroom@gmail.com', 'Testing888password')
                smtp.sendmail('vtestingroom@gmail.com','vadim.avercon@gmail.com', msg)
                smtp.quit()
            # End Email
            print(data)
            write_to_csv(data)
            return 'Thank you!' #redirect('/thankyou.html')

        except:
            return 'Didi not save to database!'
    else:
        return 'Something went wrong. Try again!'



