from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Initialize the target number
TARGET = random.randint(1, 1000)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        try:
            user_guess = int(request.form.get("guess"))
            if user_guess == TARGET:
                message = "You Successfully Guessed!!!!!!! Game Over."
            elif user_guess < TARGET:
                message = "Your Guess is Less than Target....... Try again"
            else:
                message = "Your Guess is Greater than Target....... Try again"
        except ValueError:
            message = "Please enter a valid number."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
