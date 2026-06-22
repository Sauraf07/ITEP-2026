import asyncio

from sqlalchemy.exc import SQLAlchemyError

from src.model.post import Post
from src.service.post_service import PostService
from src.resourcenotfound.resourcenotfound import ResourcenotFound
from src.model.user import User
from src.service.user_service import UserService
from src.db.db_config import SessionLocal


async def create_user():
    try:
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        async with SessionLocal.begin() as session:
            user_service = UserService(session)
            user = User(name=name, email=email, password=password)
            created_user = await user_service.create_user(user)
            print(f"User created with ID: {created_user.id}")
    except SQLAlchemyError as e:
        print(e)
            
async def get_all_users():
    try:
        async with SessionLocal() as session:
            user_service = UserService(session)
            users = await user_service.get_all_users()
            for user in users:
                print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    except SQLAlchemyError as e:
        print(e)
            

async def fetch_by_id():
    try:
        user_id = int(input("Enter user ID: "))
        async with SessionLocal() as session:
            user_service = UserService(session)
            user = await user_service.get_user_by_id(user_id)
            if not user:
                raise ResourcenotFound("Invalid Resource")
            else:
                for user in user:
                    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    except SQLAlchemyError as e:
        print(e)

        
async def update_user_by_id():
    try:
        user_id = int(input("Enter user ID to update: "))
        async with SessionLocal.begin() as session:
            user_service = UserService(session)
            user = await user_service.get_user_by_id(user_id)
            if not user:
                raise ResourcenotFound("Invalid Resource")
            else:
                for user in user:
                    user.name = input("Enter new name: ")
                    user.email = input("Enter new email: ")
                    user.password = input("Enter new password: ")
                    await session.commit()
                    print("User updated successfully.")
    except SQLAlchemyError as e:
        print(e)
   
   
async def delete_user():
    try:
        user_id = int(input("Enter user ID to delete: "))
        async with SessionLocal.begin() as session:
            user_service = UserService(session)
            user = await user_service.get_user_by_id(user_id)
            if not user:
                raise ResourcenotFound("Invalid Resource")
            else:
                await session.delete(user)
                await session.commit()
                print("User deleted successfully.")
    except SQLAlchemyError as e:
        print(e)
    

async def create_post():
    try:
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        user_id = int(input("Enter user ID for the post: "))
        async with SessionLocal.begin() as session:
            post_service = PostService(session)
            post = Post(title=title, content=content, user_id=user_id)
            created_post = await post_service.create_post(post)
            print(f"Post created with ID: {created_post.id}")
    except SQLAlchemyError as e:
        print(e)
        
async def fetch_all_post():
    try:
        async with SessionLocal() as session:
            post_service = PostService(session)
            posts = await post_service.get_all_posts()
            for post in posts:
                print(f"ID: {post.id}, Title: {post.title}, Content: {post.content}, User ID: {post.user_id}")
    except SQLAlchemyError as e:
        print(e)
        
async def fetch_post_by_id():
    try:
        post_id = int(input("Enter post ID: "))
        async with SessionLocal() as session:
            post_service = PostService(session)
            post = await post_service.fetch_post_by_id(post_id)
            if not post:
                raise ResourcenotFound("Invalid Resource")
            else:
                for post in post:
                    print(f"ID: {post.id}, Title: {post.title}, Content: {post.content}, User ID: {post.user_id}")

    except SQLAlchemyError as e:
        print(e)

async def update_post_by_id():
    try:
        post_id = int(input("Enter post ID to update: "))
        async with SessionLocal.begin() as session:
            post_service = PostService(session)
            post = await post_service.fetch_post_by_id(post_id)
            if not post:
                raise ResourcenotFound("Invalid Resource")
            else:
                for post in post:
                    post.title = input("Enter new title: ")
                    post.content = input("Enter new content: ")
                    await session.commit()
                    print("Post updated successfully.")
    except SQLAlchemyError as e:
        print(e)
   
async def delete_post_by_id():
    try:
        post_id = int(input("Enter post ID to delete: "))
        async with SessionLocal.begin() as session:
            post_service = PostService(session)
            post = await post_service.fetch_post_by_id(post_id)
            if not post:
                raise ResourcenotFound("Invalid Resource")
            else:
                await session.delete(post)
                await session.commit()
                print("Post deleted successfully.")
    except SQLAlchemyError as e:
        print(e)

async def main():
    while True:
        print("1 To create User")
        print("2 to get all users")
        print("3 To fetch user by id")
        print("4 To update user by id")
        print("5 To delete user by id")
        print("6 to create Post")
        print("7 to fetch all posts")
        print("8 to fetch post by id")
        print("9 to update post by id")
        print("10 to delete post by id")

        print("0 to exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            await create_user()
        elif choice == "2":
            await get_all_users()
        elif choice == "3":
            await fetch_by_id()
        elif choice == "4":
            await update_user_by_id()
        elif choice == "5":
            await delete_user()
        elif choice == "6":
            await create_post()
        elif choice == "7":
            await fetch_all_post()
        elif choice == "8":
            await fetch_post_by_id()
        elif choice == "9":
            await update_post_by_id() 
        elif choice == "10":
            await delete_post_by_id()
        elif choice == "0":
            break

asyncio.run(main())