from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloworld():

    students = [
        {"id": "c0894214", "name": "ashu sharma"},
        {"id": "c0894124", "name": "sarpreet"},
        {"id": "c0897852", "name": "harkirat singh"},
        {"id": "c0893576", "name": "jasleen kaur chopra"}
    ]
    
    html_content = "<h1>Student IDs and Names</h1>"
    html_content += "<ul>"
    for student in students:
        html_content += f"<li>{student['id']}: {student['name']}</li>"
    html_content += "</ul>"
    
    return html_content

app.run(host='0.0.0.0', port=80)

