from flask import Flask, render_template, request

app = Flask(__name__)

string_list = []
def read_strings():
    with open("strings.txt", "r") as file:
        strings = file.readlines()
    return [string.strip() for string in strings]

def append_string(new_string):
    with open("strings.txt", "a") as file:
        file.write(new_string + "\n")
        
@app.route("/", methods=["GET", "POST"])
def home():
    global string_list
    if request.method == "POST":
        new_string = request.form.get("string_input")
        string_list.append(new_string)
        write_strings(string_list)
    return render_template("index.html", string_list=string_list)

if __name__ == "__main__":
    app.run(debug=True)
