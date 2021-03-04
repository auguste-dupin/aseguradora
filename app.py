from flask import Flask, render_template, request

app = Flask(__name__)

distance = 0.1

@app.route("/")
def index():
    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    # Render HTML with count variable
    return render_template("index.html", count=count)

@app.route("/test")
def show_pag1():
    global distance
    return render_template("pag1.html", distance=distance)

@app.route("/main")
def main():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)