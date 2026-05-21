from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():

    html_content = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ethar</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: #333;
            }
            .card {
                background-color: #ffffff;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 500px;
                width: 90%;
            }
            h1 {
                color: #2c3e50;
                font-size: 26px;
                margin-bottom: 20px;
            }
            p {
                color: #5a6c7d;
                font-size: 16px;
                line-height: 1.6;
            }
            .badge {
                display: inline-block;
                background-color: #d4edda;
                color: #155724;
                padding: 8px 16px;
                border-radius: 50px;
                font-weight: bold;
                font-size: 14px;
                margin-top: 20px;
                border: 1px solid #c3e6cb;
            }
            .footer {
                margin-top: 25px;
                font-size: 12px;
                color: #95a5a6;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1> Welcome to our website</h1>
            <p>this website for test pipline</p>
            <div class="badge">
                ● active and working
            </div>
            <div class="footer">
              bye bye
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)