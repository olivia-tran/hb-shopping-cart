"""Ubermelon shopping application Flask server.

Provides web interface for browsing melons, seeing detail about a melon, and
put melons in a shopping cart.

Authors: Joel Burton, Christian Fernandez, Meggie Mahnken, Katie Byers.
"""

from flask import Flask, render_template, redirect, flash, session, request
import jinja2

import melons

app = Flask(__name__)

# A secret key is needed to use Flask sessioning features
app.secret_key = 'hgksahgkhgiuaildflgnldjKLHHlnk80808hlshlh'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/melons")
def list_melons():
    """Return page showing all the melons ubermelon has to offer"""

    melon_list = melons.get_all()
    return render_template("all_melons.html",
                           melon_list=melon_list)


@app.route("/melon/<melon_id>")
def show_melon(melon_id):
    """Return page showing the details of a given melon.

    Show all info about a melon. Also, provide a button to buy that melon.
    """
    # melon_id = <melon_id >
    melon = melons.get_by_id(melon_id)
    # print(melon)
    return render_template("melon_details.html",
                           display_melon=melon)


@app.route("/cart")
def show_shopping_cart():
    """Display content of shopping cart."""

    # TODO: Display the contents of the shopping cart.

    # The logic here will be something like:
    #
    # - get the cart dictionary from the session

    # melon_id_list = request.args.getlist(session['cart'])  # added .args
    melons_in_cart = session['cart']

    # total_cost += request.args.get(session['cart'][3])
    total_cost = 0  # check out cost of all items
    cost_by_item = 0  # total cost of each item in the cart
# - create a list to hold melon objects and a variable to hold the total
#   cost of the order

# - loop over the cart dictionary, and for each melon id:
    for melon_id, quantity in melons_in_cart.items():
        #    - get the corresponding Melon object

        # melon = melons.get_by_id(melon_id)
        melon = melons.melon_types[melon_id]
        #    - compute the total cost for that type of melon

        #    - add this to the order total
        cost_by_item = (quantity * melon.price)
        total_cost += cost_by_item
        #    - add quantity and total cost as attributes on the Melon object

        melon.cost_by_item = cost_by_item
        melon.quantity = quantity

        #    - add the Melon object to the list created above
        # - pass the total order cost and the list of Melon objects to the template
#
# Make sure your function can also handle the case wherein no cart has
# been added to the session

    return render_template("cart.html", session=session, melons_in_cart=melons_in_cart, total_cost=total_cost)


@app.route("/add_to_cart/<melon_id>")
def add_to_cart(melon_id):
    """Add a melon to cart and redirect to shopping cart page.

    When a melon is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Melon successfully added to
    cart'."""

    # TODO: Finish shopping cart functionality

    session.modified = True

    # - check if a "cart" exists in the session, and create one (an empty
    #   dictionary keyed to the string "cart") if not

    # cart_content = [] #[{melon_id: qty}, {melon_id: qty}]
    # session['cart'] = {cart : {melon_id: qty}, cart: {melon_id: qty}}
    # session['cart'] is a key in the session dictionary

    # cart_content.append(melon_item)

    # adding dict {melon_id: qty} into list
    # melon_item = {}

    # check to see if the session already contains a cart

    # if session['cart'] is None:
    # if 'cart' not in session:
    #     session['cart'] = {}

   # if not session.get('cart') is None:

    # If not, add a new cart (an empty dictionary) to the session.

    # if not melon_item:
    #     melon_item('cart', {})

    # - check if the desired melon id is the cart, and if not, put it in
    # - increment the count for that melon id by 1

    melons_in_cart = session['cart']
    if melon_id not in melons_in_cart:
        melons_in_cart[melon_id] = 1
    else:
        # session['cart'] = {melon_id: qty, melon_id: qty, melon_id: qty}
        melons_in_cart[melon_id] += 1

    flash("Melon successfully added to cart.")

    # - flash a success message
    # - redirect the user to the cart page

    # return render_template("cart.html")
    return redirect("/cart")


"""  session.modified = True
    session['cart'] = {}
    if melon_id not in session['cart']:
        session['cart'] = melon_id
    else:
        session['cart'] += 1

    flash("Melon added to the card.")
"""


@ app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@ app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    # TODO: Need to implement this!

    # The logic here should be something like:
    #
    # - get user-provided name and password from request.form
    # - use customers.get_by_email() to retrieve corresponding Customer
    #   object (if any)
    # - if a Customer with that email was found, check the provided password
    #   against the stored one
    # - if they match, store the user's email in the session, flash a success
    #   message and redirect the user to the "/melons" route
    # - if they don't, flash a failure message and redirect back to "/login"
    # - do the same if a Customer with that email doesn't exist

    return "Oops! This needs to be implemented"


@ app.route("/checkout")
def checkout():
    """Checkout customer, process payment, and ship melons."""

    # For now, we'll just provide a warning. Completing this is beyond the
    # scope of this exercise.

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/melons")


if __name__ == "__main__":
    app.run(debug=True)
