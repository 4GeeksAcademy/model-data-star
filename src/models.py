from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    favorites: Mapped[list["Favorite"]] = relationship(back_populates="user")


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "firstname": self.first_name,
            "lastname": self.last_name,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__="people"
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(120), nullable= False)
    Favorite: Mapped[list["Favorite"]]= relationship(back_populates="people")

def serialize(self):
    return {
        "id": self.id,
        "name": self.name
    }

class Vehicles(db.Model):
    __tablename__="vehicles"
    id: Mapped[int]= mapped_column(primary_key = True)
    name: Mapped[str]=mapped_column(String(120), nullable=False)
def serialize(self):
    return {
        "id": self.id,
        "name": self.name
    }
class Species(db.Model):
    __tablename__="species"
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(120),nullable= False)

def serialize(self):
    return {
        "id": self.id,
        "name": self.name

    }

class Planet(db.Model):
    __tablename__="planet"
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(120), nullable= False)
    Favorite: Mapped[list["Favorite"]]= relationship(back_populates="planet")

def serialize(self):
    return {
        "id": self.id,
        "name":self.name

    }

class Favorite(db.Model):
    __tablename__ = "favorite"
    id: Mapped[int] = mapped_column(primary_key = True)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"),nullable=True)
    planet: Mapped[Planet] = relationship(back_populates= "favorites")
    people_id: Mapped[int] = mapped_column(ForeignKey("people.id"),nullable=True)
    people: Mapped[People] = relationship(back_populates= "favorites")
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped[User] = relationship(back_populates= "favorites")

def serialize(self):
    return {
        "id": self.id,
        "planet_id": self.planet_id,
        "people_id": self.people_id,
        "user_id": self.user_id
    }