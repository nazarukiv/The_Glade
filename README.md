
# The Glade - E-commerce Platform

Welcome to **The Glade**, an e-commerce platform built with Django. This project is designed to showcase a modern and sleek online shopping experience, featuring a collection of stylish and high-end merchandise.

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


## About the Project
The Glade is a demonstration of a modern e-commerce platform built using Django. It features a sleek design and provides a user-friendly shopping experience. This project can serve as a starting point for developing a full-fledged e-commerce application.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Credits
Author: Nazaruk Ivan  
Year: 2024

