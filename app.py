
from flask import Flask
import os
import datetime
import subprocess
app = Flask(__name__)
@app.route('/htop')
def htop():
    # Your full name
    name = "Ayush Singh Rathore"
    
    # System username
    username = os.getlogin()
    
    # Server time in IST
    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime('%Y-%m-%d %H:%M:%S')
    # System 'top' output (first 10 lines for brevity)
    top_output = subprocess.getoutput("top -bn1 | head -10")
    # HTML output
    html = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <pre><strong>Top Output:</strong><br>{top_output}</pre>
    """
    return html
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)