from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

availableToppings = ["Tomato Sauce", "Mozzarella", "Pepperoni", "Jalapeños"]
pizzas = {}

# Home
@app.route("/")
def homePage():
    return render_template('index.html')

# Pizza
@app.route("/pizza", methods=["GET", "POST"])
def managePizza():
    if request.method == "POST":
        pizzaName = request.form.get("pizzaName")
        toppings = request.form.getlist("toppings")

        if pizzaName and toppings:
            pizzas[pizzaName] = toppings
        
        return redirect(url_for("managePizza"))

    return render_template("pizza.html", pizzas=pizzas, availableToppings=availableToppings)

@app.route("/deletePizza/<pizzaName>")
def deletePizza(pizzaName):
    pizzas.pop(pizzaName, None)
    return redirect(url_for("managePizza"))

# Toppings
@app.route("/toppings", methods=["GET", "POST"])
def manageToppings():
    if request.method == "POST":
        newTopping = request.form.get("toppingName")
        if newTopping and newTopping not in availableToppings:
            availableToppings.append(newTopping)
            return redirect(url_for("manageToppings"))

    return render_template("toppings.html", availableToppings=availableToppings)

@app.route("/deleteTopping/<topping>")
def delete_topping(topping):
    if topping in availableToppings:
        availableToppings.remove(topping)
    return redirect(url_for("manageToppings"))

# Error Handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500
