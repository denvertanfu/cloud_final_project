from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('webpage.html')
welcome = "<h1>Welcome to Big Data Processing Application</h1>"
hint = "<p>Please type the number that correspons to which application you would like to run</p>"
option1 = "<a href='http://34.133.165.5:9870' target='_blank'>1. Apache Hadoop</a><br>"
option2 = "<a href='http://34.132.12.151:80' target='_blank'>2. Apache Spark</a><br>"
option3 = "<a href='http://34.133.229.56:80' target='_blank'>3. Jupyter Notebook</a><br>"
option4 = "<a href='http://34.121.57.127:80' target='_blank'>4. SonarQube and SonarScanner</a><br>"


@app.route("/")
def home_page():
    return f"{welcome}{hint}{option1}{option2}{option3}{option4}"


if __name__ == '__main__':
   # app.run(debug = True)
   app.run(host='0.0.0.0')