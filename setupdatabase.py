from basicmodel import app, db, Student

app.app_context().push()

db.create_all()

kamila = Student('Kamila', 6)
piotr = Student('Piotr', 5)

print (kamila.id)
print (piotr.id)

db.session.add_all(
[kamila,piotr]

)
db.session.commit()
print(kamila.id)
print(piotr.id)
print(kamila)
print(piotr)