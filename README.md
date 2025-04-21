Choco-Store
-----------
🛒 Django E-commerce Website
A full-featured e-commerce web application built with Django and Razorpay payment integration.

📌 Features
User Authentication (Login, Registration)

Product listing by category and title

Add to Cart, Wishlist, and Checkout

Address management and profile update

Razorpay payment gateway integration

Order placement and order history

AJAX-based cart update (plus, minus, remove)

Search functionality

🧰 Tech Stack
Backend: Django

Frontend: HTML, CSS, Bootstrap/Tailwind (as per your design)

Database: SQLite (default)

Payment Gateway: Razorpay

Other Tools: Git, GitHub

🚀 Setup Instructions
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Create and activate virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables

Create a .env file or update settings.py with your Razorpay credentials:

python
Copy
Edit
RAZOR_KEY_ID = 'your_razorpay_key'
RAZOR_KEY_SECRET = 'your_razorpay_secret'
Apply migrations

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Create superuser (for admin panel)

bash
Copy
Edit
python manage.py createsuperuser
Run the server

bash
Copy
Edit
python manage.py runserver
Open in browser

cpp
Copy
Edit
http://127.0.0.1:8000/
📁 Project Structure
swift
Copy
Edit
project/
│
├── app/
│   ├── migrations/
│   ├── templates/app/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
📸 Screenshots
Add screenshots of the home page, cart, checkout, order, etc. if needed.

✅ To Do
Add unit tests

Add product review/ratings

Improve UI with TailwindCSS

Email notifications

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

📄 License
This project is licensed under the MIT License.

