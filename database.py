from models import User, Post
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


async def create_post(post):
    document = post
    result = await collection_posts.insert_one(document)
    return document
