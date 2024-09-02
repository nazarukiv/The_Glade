
# The Glade - E-commerce Platform


Welcome to **The Glade**, an e-commerce platform built with Django. This project is designed to showcase a modern and sleek online shopping experience, featuring a collection of stylish and high-end merchandise.

## Table of Contents

- [Features](#features)
- [Project Setup](#project-setup)
- [Using Docker](#using-docker)
- [Project Structure](#project-structure)
- [License](#license)
- [Credits](#credits)

## Features

- **Responsive Design**: A fully responsive layout that adapts seamlessly to desktop and mobile devices.
- **User Authentication**: Secure user registration, login, and profile management.
- **Shopping Cart**: Add products to your cart and proceed to checkout.
- **Product Search**: Easily search for products by name or category.
- **Admin Dashboard**: Manage products, orders, and users through the Django admin interface.

## Project Setup

To set up this project locally, follow these steps:

### 1. Clone the Repository

\```bash
git clone https://github.com/your-username/glade-ecommerce.git
cd glade-ecommerce
\```

### 2. Set Up a Virtual Environment

Make sure you have Python 3.8+ installed on your system. Then, create and activate a virtual environment:

\```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
\```

### 3. Install Dependencies

Install the required packages using pip:

\```bash
pip install -r requirements.txt
\```

### 4. Set Up the Database

Run the following commands to create the database and apply migrations:

\```bash
python manage.py migrate
\```

### 5. Create a Superuser

To access the Django admin panel, you'll need to create a superuser:

\```bash
python manage.py createsuperuser
\```
Follow the prompts to create your admin account.

### 6. Run the Development Server

You can now run the development server:

\```bash
python manage.py runserver
\```
Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to view the site.

### 7. Access the Admin Panel

Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to access the Django admin panel and log in with the superuser credentials you created earlier.

## Using Docker

To set up and run this project using Docker, follow these steps:

### 1. Build the Docker Image

Navigate to the root directory of your project where the Dockerfile is located and run:

\```bash
docker build -t glade-ecommerce .
\```

### 2. Run the Docker Container

Once the image is built, you can run the container using:

\```bash
docker run -d -p 8000:8000 glade-ecommerce
\```

This command maps the container’s port 8000 to your machine’s port 8000, allowing you to access the application at `http://localhost:8000/`.

### 3. Stopping the Docker Container

To stop the container, first find the container ID using:

\```bash
docker ps
\```

Then stop it with:

\```bash
docker stop <container_id>
\```


## Credits

Author: Nazaruk Ivan  
Year: 2024
