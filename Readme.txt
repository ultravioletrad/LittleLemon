To run a Django project locally after downloading it, you'll need to follow these steps:

    Set up a Virtual Environment (optional but recommended):
        Create a new virtual environment: python3 -m venv myenv
        Activate the virtual environment:
            For Windows: myenv\Scripts\activate
            For macOS/Linux: source myenv/bin/activate
        Note: Replace myenv with the desired name for your virtual environment.

    Install project dependencies:
        Navigate to the project's root directory (where the manage.py file is located).
        Install the required packages listed in the project's requirements.txt file: 
        pip install -r requirements.txt
        This will ensure that all necessary dependencies are installed in your virtual environment.

    Set up the MySQL database (if you want to,name and password given in settings.py file):
    If you are using your own database,update the database configuration in the project's settings file (settings.py).
    Run database migrations: python manage.py migrate

    Run the development server:

    Start the Django development server: python manage.py runserver
    By default, the server will run on http://127.0.0.1:8000/
    This shows the static HTML homepage of the Little Lemon Restaurant.

    You can check the following end points.
    Api Root
    The default basic root view for DefaultRouter
    http://127.0.0.1:8000/api/ 

    This contains the clickable link to 
     "menu-items": "http://127.0.0.1:8000/menu-items/"
    This requires authentication.
      "detail": "Authentication credentials were not provided."
    Go to django admin to login(username and password given in passwords.txt file)
    127.0.0.1:8000/admin/

    http://127.0.0.1:8000/admin/restaurant/menu/
    http://127.0.0.1:8000/admin/restaurant/booking/

    Visit http://localhost:8000/api/menu-items to test the POST and GET operations.
    http://127.0.0.1:8000/api/menu-items/
    http://127.0.0.1:8000/api/menu-items/1/
    http://127.0.0.1:8000/api/message/

    To check user authentication and get token.
    http://127.0.0.1:8000/auth/token/login/
    http://127.0.0.1:8000/auth/token/logout/
