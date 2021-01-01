from flask import Flask, render_template,url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)





@app.route('/')
def my_world():
    return render_template('index.html')


@app.route('/<string:Post_id>')
def html_pages(Post_id):
    return render_template(Post_id)


# @app.route('/', methods=['POST'])
# def getvalue():
#     email=request.form['email']
#     subject=request.form['subject']
#     message=request.form['message']
#     return render_template('pass.html', e=email , sub=subject , mess=message)
def write_to_file(data):
    with open('database.txt',mode='a') as database:
           email=data["email"]
           subject=data["subject"]
           msg=data["message"]
           file=database.write(f'\n{email}, {subject}, {msg}')

def write_to_csv(data):
    with open('database3.csv',mode='a',newline='') as database2:
           email=data["email"]
           subject=data["subject"]
           message=data["message"]
           csv_writer=csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
           csv_writer.writerow([email, subject, message]) 
        
            
		
@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong,try again!!!'

# @app.route('/works.html')
# def works():
#     return render_template('works.html')



# @app.route('/contact.html')
# def blog():
#     return render_template('contact.html')

# @app.route('/components.html')
# def comp():
#     return render_template('components.html')

# @app.route('/about.html')
# def my_about():
#     return render_template('about.html')

# @app.route('/work.html')
# def my_world2():
#     return render_template('work.html')
