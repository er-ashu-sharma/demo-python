from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloworld():
<<<<<<< HEAD

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
=======
    return "Hello From Azure!"
if __name__ == "__main__":
    app.run()
>>>>>>> da8c3580679eef7e5f90e6be574aa6d37423cc42
