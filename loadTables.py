from app import db
from app.models import User, Category, Items, Cart

db.drop_all()

db.create_all()

# insert rows for User table
userTest = User(id=0, first_name='Testy',role="Admin" ,last_name='Test', username='testyTest', email='testy@gmail.com', password_hash='randomHash', securityQuestion='a', question_answer_hash= 'a')

guestUser = User(id =9999, first_name="Guest", role="Admin" ,last_name = None, username="Guest1", email=None)
userTest2 = User(id=1, first_name='Taeyong', role="Admin" ,last_name='Lee', username='ty_xoxo', email='lty1995@neotech.com', password_hash='randomHash2')
userTest3 = User(id=2, first_name='Johnny', role="Admin" ,last_name='Suh', username='johnnysuhlee', email='jjsuh@neotech.com', password_hash='randomHash3')
userTest4 = User(id=3, first_name='Yuta', role="Admin" ,last_name='Nakamoto', username='tako_ya', email='naYu06@neotech.com', password_hash='randomHash4')
userTest5 = User(id=4, first_name='Mark', role="Admin" ,last_name='Lee', username='onyour__mark', email='mmarkly99@neotech.com', password_hash='randomHash5')
userTest6 = User(id=5, first_name='Sungchan', role="Admin" ,last_name='Jung', username='jschannie27', email='singsangsung_chan@neotech.com', password_hash='randomHash6')
userTest7 = User(id=6, first_name='Doyoung', role="Admin" ,last_name='Kim', username='do0_ie', email='doyo982@neotech.com', password_hash='randomHash7')
userTest8 = User(id=7, first_name='Yangyang', role="Admin" ,last_name='Liu', username='wooly_yang', email='blacksheep9023@neotech.com', password_hash='randomHash8')
userTest9 = User(id=8, first_name='Kun', role="Admin" ,last_name='Qian', username='kuncloud1010', email='cloudy1011@neotech.com', password_hash='randomHash9')
userTest10 = User(id=9, first_name='Oliver', role="Admin" ,last_name='Stuart', username='oliveStu389', email='oliver_stuart5843@info44.tech', password_hash='randomHash10')
userTest11 = User(id=10, first_name='Roger', role="Admin" ,last_name='Hunt', username='rrrogerd', email='Roger_Hunt6249@gmal.com', password_hash='randomHash11')
userTest12 = User(id=11, first_name='Gil', role="Admin" ,last_name='Brooks', username='gills17Fsh', email='Gil_Brooks5827@atink.com', password_hash='randomHash12')
userTest13 = User(id=12, first_name='Holly', role="Admin" ,last_name='Poulton', username='mistletoad12', email='Holly_poulton532@nickia.com', password_hash='randomHash13')
userTest14 = User(id=13, first_name='Alessia', role="Admin" ,last_name='Middleton', username='alleycaat0', email='alessia_Middleton1512@gmail.com', password_hash='randomHash14')

db.session.add(userTest)
db.session.add(guestUser) 
db.session.add(userTest2)
db.session.add(userTest3) 
db.session.add(userTest4)
db.session.add(userTest5) 
db.session.add(userTest6)
db.session.add(userTest7) 
db.session.add(userTest8)
db.session.add(userTest9) 
db.session.add(userTest10)
db.session.add(userTest11) 
db.session.add(userTest12)
db.session.add(userTest13) 
db.session.add(userTest14)
db.session.commit()


# inserting rows for Category table
categoryTest = Category(categoryID = 0, category_name="horror")

categoryTest2 = Category(categoryID = 1, category_name="comedy")
categoryTest3 = Category(categoryID = 2, category_name="fiction")
categoryTest4 = Category(categoryID = 3, category_name="non-fiction")
categoryTest5 = Category(categoryID = 4, category_name="children's")
categoryTest6 = Category(categoryID = 5, category_name="adult's")
categoryTest7 = Category(categoryID = 6, category_name="hobby")
categoryTest8 = Category(categoryID = 7, category_name="kids")
categoryTest9 = Category(categoryID = 8, category_name="toys")
categoryTest10 = Category(categoryID = 9, category_name="beauty")
categoryTest11 = Category(categoryID = 10, category_name="outdoors")
categoryTest12 = Category(categoryID = 11, category_name="shoes")
categoryTest13 = Category(categoryID = 12, category_name="storage")
categoryTest14 = Category(categoryID = 13, category_name="kitchen")
categoryTest15 = Category(categoryID = 14, category_name="school & office")
categoryTest16 = Category(categoryID = 15, category_name="health")
categoryTest17 = Category(categoryID = 16, category_name="household needs")
categoryTest18 = Category(categoryID = 17, category_name="misc & others")

db.session.add(categoryTest) 
db.session.add(categoryTest2)
db.session.add(categoryTest3) 
db.session.add(categoryTest4)
db.session.add(categoryTest5) 
db.session.add(categoryTest6)
db.session.add(categoryTest7) 
db.session.add(categoryTest8)
db.session.add(categoryTest9) 
db.session.add(categoryTest10)
db.session.add(categoryTest11) 
db.session.add(categoryTest12)
db.session.add(categoryTest13) 
db.session.add(categoryTest14)
db.session.add(categoryTest15) 
db.session.add(categoryTest16)
db.session.add(categoryTest17) 
db.session.add(categoryTest18)
db.session.commit()


# inserting rows for Items table
# inserting rows for Items table
itemsTest = Items(itemID=0, product_name='The Shining', condition='New', description='A novel by Stephen King',
                  price=4, quantity=20, sellerID=0, categoryID=0)

itemsTest2 = Items(itemID=1, product_name='To Kill a Mockingbird', condition='Used - Good', description='A novel by Harper Lee',
                  price=12, quantity=17, sellerID=0, categoryID=1)
itemsTest3 = Items(itemID=2, product_name='Pride and Prejudice', condition='Used - Good', description='A novel by Jane Austen',
                  price=47, quantity=4, sellerID=0, categoryID=2)
itemsTest4 = Items(itemID=3, product_name='The Great Gatsby', condition='New', description='A novel by F. Scott Fitzgerald',
                  price=35, quantity=16, sellerID=0, categoryID=3)
itemsTest5 = Items(itemID=4, product_name='Harry Potter and the Sorcerer\'s Stone', condition='New', description='A novel by J.K. Rowling',
                  price=59, quantity=4, sellerID=0, categoryID=4)
itemsTest6 = Items(itemID=5, product_name='1984', condition='New', description='A novel by George Orwell',
                  price=60, quantity=7, sellerID=2, categoryID=5)
itemsTest7 = Items(itemID=6, product_name='Brave New World', condition='Used - Like New', description='A novel by Aldous Huxley',
                  price=180, quantity=26, sellerID=0, categoryID=6)
itemsTest8 = Items(itemID=7, product_name='The Catcher in the Rye', condition='New', description='A novel by J.D. Salinger',
                  price=10, quantity=38, sellerID=0, categoryID=7)
itemsTest9 = Items(itemID=8, product_name='The Hobbit', condition='New', description='A novel by J.R.R. Tolkien',
                  price=6, quantity=36, sellerID=0, categoryID=8)
itemsTest10 = Items(itemID=9, product_name='Moby-Dick', condition='New', description='A novel by Herman Melville',
                   price=14, quantity=50, sellerID=0, categoryID=9)
itemsTest11 = Items(itemID=10, product_name='Little Women', condition='Used - Good', description='A novel by Louisa May Alcott',
                   price=32, quantity=4, sellerID=0, categoryID=10)
itemsTest12 = Items(itemID=11, product_name='Frankenstein', condition='Used - Acceptable', description='A novel by Mary Shelley',
                   price=87, quantity=16, sellerID=0, categoryID=11)
itemsTest13 = Items(itemID=12, product_name='The Picture of Dorian Gray', condition='Used - Good', description='A novel by Oscar Wilde',
                   price=64, quantity=4, sellerID=0, categoryID=12)
itemsTest14 = Items(itemID=13, product_name='To the Lighthouse', condition='New', description='A novel by Virginia Woolf',
                   price=30, quantity=5, sellerID=0, categoryID=13)
itemsTest15 = Items(itemID=14, product_name='Crime and Punishment', condition='New', description='A novel by Fyodor Dostoevsky',
                   price=2, quantity=39, sellerID=0, categoryID=14)
itemsTest16 = Items(itemID=15, product_name='The Odyssey', condition='New', description='An epic poem by Homer',
                   price=35, quantity=21, sellerID=0, categoryID=15)
itemsTest17 = Items(itemID=16, product_name='The Adventures of Tom Sawyer', condition='Used - Good', description='A novel by Mark Twain',
                   price=100, quantity=4, sellerID=0, categoryID=16)
itemsTest18 = Items(itemID=17, product_name='Jane Eyre', condition='New', description='A novel by Charlotte Bronte',
                   price=5, quantity=27, sellerID=0, categoryID=16)

itemsTest19 = Items(itemID=18, product_name='Nineteen Eighty-Four', condition='New', description='A novel by George Orwell',
                   price=30, quantity=6, sellerID=1, categoryID=2)
itemsTest20 = Items(itemID=19, product_name='Animal Farm', condition='Used - Like New', description='A novella by George Orwell',
                   price=60, quantity=17, sellerID=3, categoryID=2)
itemsTest21 = Items(itemID=20, product_name='The Bell Jar', condition='New', description='A novel by Sylvia Plath',
                   price=60, quantity=30, sellerID=3, categoryID=2)
itemsTest22 = Items(itemID=21, product_name='The Lord of the Rings', condition='New', description='A novel by J.R.R. Tolkien',
                   price=3, quantity=25, sellerID=4, categoryID=3)


db.session.add(itemsTest) 
db.session.add(itemsTest2)
db.session.add(itemsTest3) 
db.session.add(itemsTest4)
db.session.add(itemsTest5) 
db.session.add(itemsTest6)
db.session.add(itemsTest7) 
db.session.add(itemsTest8)
db.session.add(itemsTest9) 
db.session.add(itemsTest10)
db.session.add(itemsTest11) 
db.session.add(itemsTest12)
db.session.add(itemsTest13) 
db.session.add(itemsTest14)
db.session.add(itemsTest15) 
db.session.add(itemsTest16)
db.session.add(itemsTest17) 
db.session.add(itemsTest18)
db.session.add(itemsTest19) 
db.session.add(itemsTest20)
db.session.add(itemsTest21) 
db.session.add(itemsTest22)
db.session.commit()


# create test Cart items
testCart = Cart(cartID = 0, userID = 1, itemID = 0, quantity = 1, createdAt=None, modifiedAt=None)
testCart2 = Cart(cartID = 1, userID= 2, itemID = 0, quantity = 1, createdAt=None, modifiedAt=None)
testCart3 = Cart(cartID=2, userID=2, itemID=1, quantity=1, createdAt=None, modifiedAt=None)

db.session.add(testCart)
db.session.add(testCart2)
db.session.add(testCart3)

db.session.commit()

# test output from database tables
users = User.query.all()
for u in users:
	print(u.id, u.username)

u = User.query.get(0)
print(u)
print()

categories = Category.query.all()
for c in categories:
	print(c.categoryID, c.category_name)
c = Category.query.get(0)
print(c)
print()

items = Items.query.all()
for i in items:
	print(i.product_name, i.price)
i = Items.query.get(0)
print(i)
print()

