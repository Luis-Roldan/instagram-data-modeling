import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

# Insta data bas modeling
class Follower(Base): #child   
    __tablename__ = 'follower'
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable= False)
    user = relationship("User", back_populates="follower")
    

class User(Base): #parent
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String(12), nullable= False, unique=True)
    firstname = Column(String(12), nullable= False, unique=False)
    lastname = Column(String(12), nullable= False, unique=False)
    email = Column(String(12), nullable= False, unique=True)
    follower = relationship("Follower", back_populates="user")
    comment = relationship("Comment", back_populates="user")
    post = relationship("Post", back_populates="user")

class Comment(Base): #child   
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, primary_key=True)
    comment_text = Column(String(100), nullable= False, unique=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable= False)
    user = relationship("User", back_populates="comment")
    

class Post(Base): #child   
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable= False)
    user = relationship("User", back_populates="post")
    media = relationship("Media", back_populates="post")



class Media(Base): #grandchild   (related to Post)
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"), nullable= False)
    post = relationship("Post", back_populates="media")


    




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
