from models import User, Post
from datetime import date
import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB"))

database = client.SocialMediaAPI

collection_users = database.Users
collection_posts = database.Posts


async def create_user(user):
    document = user
    result = await collection_users.insert_one(document)
    return document


async def get_user(username, password):
    document = await collection_users.find_one({"username": username, "password": password})
    return document


async def sign_out_user(username, password):
    last_seen = date.today()
    ls = str(last_seen)
    document = await collection_users.update_one({'username': username, "password": password}, {'$set': {'last_seen': ls}})
    new_document = await collection_users.find_one({"username": username, "password": password})
    return new_document


async def create_post(post):
    document = post
    result = await collection_posts.insert_one(document)
    return document
