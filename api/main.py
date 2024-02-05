from flask import Flask, render_template, jsonify
# from flask_bootstrap import Bootstrap5
app= Flask(__name__)


# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Bootstrap5(app)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404

@app.after_request
def add_security_headers(response):
    # Content-Security-Policy
    
    
    # X-Frame-Options
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    
    # X-Content-Type-Options
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    # Referrer-Policy
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    
    # Permissions-Policy
    response.headers['Permissions-Policy'] = 'geolocation=(self "https://yourdomain.com"), microphone=()'

    return response

if __name__ == "__main__":
    app.run(debug=False)