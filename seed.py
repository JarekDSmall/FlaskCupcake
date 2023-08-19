from app import app
from models import db, Cupcake

# Establish an application context
with app.app_context():
    # Drop all tables
    db.drop_all()

    # Create all tables
    db.create_all()

    # Create and add sample cupcakes
    c1 = Cupcake(
        flavor="cherry",
        size="large",
        rating=5,
    )

    c2 = Cupcake(
        flavor="chocolate",
        size="small",
        rating=9,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )

    db.session.add_all([c1, c2])
    db.session.commit()
