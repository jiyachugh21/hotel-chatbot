from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hotel_chatbot():
    if request.method == "POST":
        name = request.form["name"]
        city = request.form["city"]
        check_in = request.form["check_in"]
        nights = request.form["nights"]
        guests = request.form["guests"]
        confirm = request.form.get("confirm", "").lower()

        if confirm == "yes":
            result = f"🎉 Booking confirmed! Welcome {name}, your stay in {city} for {nights} night(s) is booked from {check_in} for {guests} guest(s)."
        else:
            result = "❌ Booking cancelled. Let us know if you change your mind!"

        return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
