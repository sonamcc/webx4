from flask import Flask, request, url_for

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
                width: 500px;  /* Increased size */
                height: auto;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎨 Welcome Buddies!! 🎨</h1>
            <p><a href="{url_for('profile', username='Sonam')}">👤 View Profile</a></p>
            <p><a href="{url_for('submit')}">✉ Submit Your Details</a></p>
        </div>
        <img class="animated-img" src="https://media4.giphy.com/media/Uds3XFFV8Z5gOyrSsP/giphy.webp" alt="Animated GIF">
    </body>
    </html>
    """

# Dynamic Profile Page
@app.route('/profile/<username>')
def profile(username):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Profile - {username}</title>
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
                width: 500px;  /* Increased size */
                height: auto;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome, {username}! 🎉</h1>
            <p>This is your profile page.</p>
            <a href="{url_for('home')}">🏠 Back to Home</a>
        </div>
        <img class="animated-img" src="https://media0.giphy.com/media/Vn3lKM3qftnomk1YCr/giphy.webp?cid=ecf05e47rjph6zslppq4ix2z5kq7fvbm7ir9pybkeunvjdfv&ep=v1_gifs_search&rid=giphy.webp&ct=g.gif" alt="Profile Animation">
    </body>
    </html>
    """

# Form Page - GET & POST
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        age = request.form.get('age', 'Unknown')
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Thank You</title>
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
                    background:  #A67B5B;
                }}
                .animated-img {{
                    width: 500px;  /* Increased size */
                    height: auto;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎉 Thank You, {name}! 🎉</h1>
                <p>Your details have been submitted successfully.</p>
                <p>🗓 Age: {age}</p>
                <a href="{url_for('home')}">🏠 Back to Home</a>
            </div>
            <img class="animated-img" src="https://media2.giphy.com/media/LZ2ZiuR6mgMnvs55wH/giphy.webp?cid=790b7611lim5wcul6n8a7gw8r8jgb7fr5vclbwhmvdd8iusf&ep=v1_stickers_search&rid=giphy.webp&ct=s.gif" alt="Thank You Animation">
        </body>
        </html>
        """
    
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
            .animated-img {{
                width: 400px;  /* Increased size */
                height: auto;
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
        <img class="animated-img" src="https://media0.giphy.com/media/GwJQEbOWmi0inXx9bu/giphy.webp?cid=790b7611ejqoxmi4r021j5r2bl3rjxiq94xb33ikbefeg0cs&ep=v1_gifs_search&rid=giphy.webp&ct=g.gif" alt="Form Animation">
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
