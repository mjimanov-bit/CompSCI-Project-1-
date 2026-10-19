
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

icons = [
    {"id": f"icon{i}", "x": random.randint(0, 800),
     "y": random.randint(0, 400), "color": "rgb(36, 87, 197)",
     "shape": "●"}
    for i in range(20)
]

shapes = ["●", "■", "▲", "★", "♥", "◆", "✚", "⬟"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/move", methods=["POST"])
def move_icons():
    for icon in icons:
        icon["x"] = random.randint(0, 800)
        icon["y"] = random.randint(0, 400)

    return jsonify(icons)


@app.route("/color", methods=["POST"])
def change_colors():
    for icon in icons:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        icon["color"] = f"rgb({red}, {green}, {blue})"

    return jsonify(icons)


@app.route("/shape", methods=["POST"])
def change_shapes():
    for icon in icons:
        icon["shape"] = random.choice(shapes)

    return jsonify(icons)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
