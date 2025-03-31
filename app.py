from flask import Flask, request, url_for, redirect

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Colorful App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #333333, #fad0c4);
                text-align: center;
                color: white;
                padding: 50px;
            }}
            .container {{
                max-width: 600px;
                margin: auto;
                background: rgba(255, 255, 255, 0.2);
                padding: 20px;
                border-radius: 10px;
            }}
            a {{
                display: block;
                text-decoration: none;
                color: white;
                font-size: 20px;
                background: #333333;
                padding: 10px;
                margin: 10px;
                border-radius: 5px;
            }}
            a:hover {{
                background: #A67B5B;
            }}
            .animated-img {{
                width: 500px;
                height: auto;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎨 Welcome Buddies!! 🎨</h1>
            <p><a href="{url_for('profile', username='Sonam',age=25)}">👤 View Profile</a></p>
            <p><a href="{url_for('submit')}">✉ Submit Your Details</a></p>
        </div>
        <img class="animated-img" src="https://media4.giphy.com/media/Uds3XFFV8Z5gOyrSsP/giphy.webp" alt="Animated GIF">
    </body>
    </html>
    """
    
@app.route('/profile')
def profile():
    name = request.args.get('name')
    age = request.args.get('age')

    if not name or not age:  # If accessed manually without parameters
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Profile Not Found</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #333333, #fad0c4);
                    text-align: center;
                    color: white;
                    padding: 50px;
                }}
                .container {{
                    max-width: 600px;
                    margin: auto;
                    background: rgba(255, 255, 255, 0.2);
                    padding: 20px;
                    border-radius: 10px;
                }}
                a {{
                    display: block;
                    text-decoration: none;
                    color: white;
                    font-size: 20px;
                    background: #333333;
                    padding: 10px;
                    margin: 10px;
                    border-radius: 5px;
                }}
                a:hover {{
                    background: #A67B5B;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>⚠ Profile Not Found!</h1>
                <p>Please submit your details first.</p>
                <a href="{url_for('home')}">🏠 Back to Home</a>
                <a href="{url_for('submit')}">📩 Submit Your Details</a>
            </div>
        </body>
        </html>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Profile - {name}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #333333, #fad0c4);
                text-align: center;
                color: white;
                padding: 50px;
            }}
            .container {{
                max-width: 600px;
                margin: auto;
                background: rgba(255, 255, 255, 0.2);
                padding: 20px;
                border-radius: 10px;
            }}
            a {{
                display: block;
                text-decoration: none;
                color: white;
                font-size: 20px;
                background: #333333;
                padding: 10px;
                margin: 10px;
                border-radius: 5px;
            }}
            a:hover {{
                background: #A67B5B;
            }}
            .animated-img {{
                width: 500px;
                height: auto;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome, {name}! 🎉</h1>
            <p>🗓 Age: {age}</p>
            <a href="{url_for('home')}">🏠 Back to Home</a>
        </div>
        <img class="animated-img" src="https://media0.giphy.com/media/Vn3lKM3qftnomk1YCr/giphy.webp" alt="Profile Animation">
    </body>
    </html>
    """




# Form Page - Redirect to Profile Page after Submission
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        age = request.form.get('age', 'Unknown')
        
        # Redirect to profile page with name & age as URL parameters
        return redirect(url_for('profile', name=name, age=age))
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Submit Form</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #333333, #fad0c4);
                text-align: center;
                color: white;
                padding: 50px;
            }}
            .container {{
                max-width: 500px;
                margin: auto;
                background: rgba(255, 255, 255, 0.2);
                padding: 20px;
                border-radius: 10px;
            }}
            input, button {{
                display: block;
                width: 80%;
                margin: 10px auto;
                padding: 10px;
                border-radius: 5px;
                border: none;
            }}
            button {{
                background: #333333;
                color: white;
                font-size: 1rem;
                cursor: pointer;
            }}
            button:hover {{
                background:  #A67B5B;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📩 Submit Your Details</h1>
            <form action="{url_for('submit')}" method="post">
                <label for="name">👤 Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="age">🎂 Age:</label>
                <input type="number" id="age" name="age" required>
                <button type="submit">🚀 Submit</button>
            </form>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
