from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    # Clear existing data
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create pizzas
    pizza1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    pizza3 = Pizza(name="Melanie", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")

    db.session.add_all([pizza1, pizza2, pizza3])
    db.session.commit()

    # Create restaurants
    r1 = Restaurant(name="Karen's Pizza Shack", address="address1")
    r2 = Restaurant(name="Sanjay's Pizza", address="address2")
    r3 = Restaurant(name="Kiki's Pizza", address="address3")

    db.session.add_all([r1, r2, r3])
    db.session.commit()

    # Create restaurant_pizzas
    rp1 = RestaurantPizza(price=5, pizza_id=pizza1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=10, pizza_id=pizza2.id, restaurant_id=r1.id)
    rp3 = RestaurantPizza(price=7, pizza_id=pizza1.id, restaurant_id=r3.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print(" Database seeded!")
