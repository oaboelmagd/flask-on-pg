from flask import Flask
import os
import psycopg2

DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBHOST = os.getenv("DBHOST")
DBNAME = os.getenv("DBNAME")

app = Flask(__name__)

@app.route('/')
def hello():

    try:
        conn = psycopg2.connect(f"dbname='{DBNAME}' user='{DBUSER}' host='{DBHOST}' password='{DBPASS}' connect_timeout=1 ")
        conn.close()
        return "<!DOCTYPEhtml><html><head><style>body{background-color:green;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;}h1{font-size:24px;color:white;}</style></head><body><h1>Working</h1></body></html>"
    except:
        return "<!DOCTYPEhtml><html><head><style>body{background-color:red;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;}h1{font-size:24px;color:white;}</style></head><body><h1>NOT Working</h1></body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)