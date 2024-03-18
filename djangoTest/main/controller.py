from .models import DB

db = DB('db\tours.db')

def createTown(name, id_country):
    db.cursor.execute(f'''INSERT INTO town id={NULL}, name={name}, id_country={id_country}''')
    db.connect.commit()
    db.connect.close()

def selectTown():
    data = db.cursor.execute('''SELECT * FROM Town''')
    db.cursor.fetchall(data)
    db.connect.close()
    return data

def updateTown(id, name, id_country):
    db.cursor.execute(f'''UPDATE town name={name}, id_country={id_country} WHERE id={id}''')
    db.connect.commit()
    db.connect.close()

def deleteTown(id):
    db.cursor.execute(f'''DELETE FROM town WHERE id={id}''')
    db.connect.commit()
    db.connect.close()