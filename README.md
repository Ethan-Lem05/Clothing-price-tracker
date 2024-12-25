# Clothing price tracker

I developed this project mostly for personal use. I had always wanted a piece of software to track clothing sales for me but all the solutions I found were blocked by a pay wall. So I decided to create my own app to solve the issue. 

## Tech stack

For this project, I had decided to put to use the technologies like Flask for API development and SQLite for simple file storage since this was just going to be a locally hosted project. Additionally, I made use of ReactJS for simple dynamic page loading, that I can update what products are being displayed easily. 

So I can explain this easier I will include a screenshot of the user interface:
![image](https://github.com/user-attachments/assets/b31a55ad-fab5-4e1c-8840-e51a88d0f3b8)

As you can see there a few tabs that allow you to perform CRUD operations through sending GET POST PATCH and DELETE operations on the database. The React app uses the Fetch API to send requests to the API hosted on a separate port that has access to a database access layer which securely protects data going in and out of our database. 

There are also other tabs such as the add item tab:
![image](https://github.com/user-attachments/assets/c27ef6b6-cce9-4086-a9e3-942af7c76271)

This tab allows the user to upload a new URL which the API will classify and then invoke the scraper that scrapes that website for data. The data is then grabbed and uploaded into our DB, Upon updating the item, we check for a sale again and will display that a sale exists for the item if it does.

## Development process

I wrote the code for this project along time ago and find that is quite unpolished upon returning to write this readme. If I were to go back and improve upon the development process, I would make sure that the API is more secure by enabling CORS properly.

Additionlly, I am not a UI designer so the designed ended up coming out quite poor. Given my growing network, I would make use of my friends who like UI desing to help me improve upon how the website looks.
