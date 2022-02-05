# run this file

from market import db
from market.models import Item

db.create_all()

Item.__table__.drop(db.engine)
Item.__table__.create(db.engine)
# db.create_all()

items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 10000},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 70000},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 1250}
]

for i in items:
    item_temp = Item (
        name = i["name"],
        price = i["price"],
        barcode = i["barcode"],
        description = f"desc {i['id'] + 1}"
    )

    db.session.add(item_temp)

db.session.commit()

item4 = Item(
    name = "IPhone 13",
    price = 90000,
    barcode = "123456789012",
    description = "desc"
)

item5 = Item(
    name = "IPad",
    price = 30000,
    barcode = "678593002580",
    description = "desc2"
)

db.session.add(item4)
db.session.add(item5)

# u1 = User (
#     username = "suketu",
#     email_address = "suketu@suketu.com",
#     password_hash = "#123efdc23"
# )

# db.session.add(u1)
db.session.commit()

# phone = Item.query.filter_by(name = "Phone").first()
# phone.owner = User.query.filter_by(username = "suketu").first().id # .id as foreignkey only accepts user.id

# db.session.commit()

# print(Item.query.all())
# print(User.query.all())
# print(
#     phone.owner,
#     phone.owned_user
# )

# iterating through all items and printing their info
# for item in Item.query.all():
#     print(item.id)
#     print(item.name)
#     print(item.price)
#     print(item.barcode)
#     print(item.description)

# for filtering results, 
# for item in Item.query.filter_by(price=500):
#     print(item.name)