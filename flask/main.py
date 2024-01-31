from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/sample-post')
def sample_post():
    return render_template('post.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact.html')

app.run(debug=True)