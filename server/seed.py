from app import app
from models import db, Book

with app.app_context():
    Book.query.delete()

    fire_and_ice = Book(
        id=1,
        title="A Game of Thrones (A Song of Ice and Fire, Book 1)",
        author="George R. R. Martin",
        page_count=864,
        summary="Winter is coming. Such is the stern motto of House Stark, the northernmost of the fiefdoms that owe allegiance to King Robert Baratheon in far-off King’s Landing. There Eddard Stark of Winterfell rules in Robert’s name. There his family dwells in peace and comfort: his proud wife, Catelyn; his sons Robb, Brandon, and Rickon; his daughters Sansa and Arya; and his bastard son, Jon Snow. Far to the north, behind the towering Wall, lie savage Wildings and worse—unnatural things relegated to myth during the centuries-long summer, but proving all too real and all too deadly in the turning of the season.",
        category="Fiction"
    )

    pretties = Book(
        id=2,
        title="Pretties",
        author="Scott Westerfeld",
        page_count=368,
        summary="Tally has to choose between fighting to forget what she knows and fighting for her life—because the authorities don’t intend to let anyone with this information survive.",
        category="Fiction"
    )

    db.session.add_all([fire_and_ice, pretties])
    db.session.commit()