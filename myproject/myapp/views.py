from django.shortcuts import render

# Create your views here.
import os
import datetime
import subprocess
from django.http import HttpResponse

def htop(request):
    # Your full name
    name = "Ayush Singh Rathore"  # Replace with your actual name

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
    return HttpResponse(html)
