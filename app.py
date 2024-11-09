from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rating')
def rating():
    return render_template('rating.html')

@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')

# Add routes for other pages as needed

if __name__ == '__main__':
    app.run(debug=True)
