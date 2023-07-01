import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    posts = relationship('Post', back_populates='user')
    comments = relationship('Comment', back_populates='user')
    followers = relationship('Follower', back_populates='following', foreign_keys='Follower.follower_id')
    following = relationship('Follower', back_populates='follower', foreign_keys='Follower.following_id')

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    image_url = Column(String(255), nullable=False)
    caption = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='comments')
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    post = relationship('Post', back_populates='comments')

class Follower(Base):
    __tablename__ = 'followers'
    follower_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    following_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    follower = relationship('User', foreign_keys=[follower_id], back_populates='followers')
    following = relationship('User', foreign_keys=[following_id], back_populates='following')
    created_at = Column(DateTime, nullable=False)

