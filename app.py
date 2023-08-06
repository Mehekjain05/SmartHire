from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/job-detail')
def job_detail():
    return render_template('job-detail.html')

@app.route('/job-list')
def job_list():
    return render_template('job-list.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/404')
def error_404():
    return render_template('404.html')

@app.route('/register')
def register():
    return render_template('Registration.html')

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dash.html')

@app.route('/jobpost')
def jobpost():
    return render_template('jobpost.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)