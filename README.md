Blog API

A RESTful Blog API built using FastAPI, SQLAlchemy, and SQLite.  
This project allows users to create, read, update, and delete blog posts through API endpoints.

Features

- Create blog posts
- View all blogs
- View single blog by ID
- Update blog posts
- Delete blog posts
- Interactive API documentation using Swagger UI
 
Technologies Used
  
Python
-FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
 
Project Structure
  
blog-api/
main.py
database.py
models.py
schemas.py
README.md

Installation
1. Clone the repository
2. git clone <repository-url>


Navigate to project folder
cd blog-api
Install dependencies
pip install fastapi uvicorn sqlalchemy pydantic

Run the Project
uvicorn main:app --reload
Server will run on:
http://127.0.0.1:8000

API Documentation
Swagger UI:
http://127.0.0.1:8000/docs

API Endpoints

Method                         Endpoint	                Description
POST	                         /blogs                 	Create blog
GET	                           /blogs	                  Get all blogs
GET	                           /blogs/{id}	            Get single blog
PUT	                           /blogs/{id}	            Update blog
DELETE                         /blogs/{id}              Delete blog


Author
Moulika Kompelly


















