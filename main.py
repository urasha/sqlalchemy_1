from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")

    captain = User()
    captain.surname = "Scott"
    captain.name = "Ridley"
    captain.age = 21
    captain.position = "captain"
    captain.speciality = "research engineer"
    captain.address = "module_1"
    captain.email = "scott_chief@mars.org"

    nurse = User()
    nurse.surname = "Ilusa"
    nurse.name = "Mary"
    nurse.age = 24
    nurse.position = "colonist"
    nurse.speciality = "nurse"
    nurse.address = "module_4"
    nurse.email = "mary1997@mail.ru"

    engineer = User()
    engineer.surname = "Shelly"
    engineer.name = "Smith"
    engineer.age = 36
    engineer.position = "colonist"
    engineer.speciality = "engineer"
    engineer.address = "module_2"
    engineer.email = "superhero269@gmail.com"

    cooker = User()
    cooker.surname = "Hanks"
    cooker.name = "Tom"
    cooker.age = 30
    cooker.position = "colonist"
    cooker.speciality = "cooker"
    cooker.address = "module_8"
    cooker.email = "legendary_cooker@yandex.ru"

    db_sess = db_session.create_session()
    db_sess.add(captain)
    db_sess.add(nurse)
    db_sess.add(engineer)
    db_sess.add(cooker)
    db_sess.commit()

    app.run()


if __name__ == '__main__':
    main()
