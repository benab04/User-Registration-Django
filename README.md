# User Registration using Django and MongoDB

### Hosted webiste link: https://user-registration-django.onrender.com/

This website allows users to register themselves and submit the link of their project. Each user gets a unique user id, which is stored as a cookie for faster logging in the future.
The data is stored in MongoDB using djongo engine.

## Installation instructions:

1. Open a new terminal in a new folder and run the following command:
 ```git
   git clone https://github.com/benab04/User-Registration-Django.git
```
3. Make sure than pip is installed on your device and the environment is set up.
   If not, follow this [link](https://pip.pypa.io/en/stable/installation/) to install it.
4. After pip is installed, run:
   ```python
   pip install virtualenv
   ```
   ```python
   virtualenv env
   ```
5. An additional folder called env would have been created. Navigate inside it and run the following command to activate the virtual evironment
   ```bash
   cd env\Scripts\
   ./activate
   cd ../../
   ```
6. Now, navigate to User-Registration-Django by running:
   ```bash
   cd User-Registration-Django
   ```
7. Install the dependencies using:
   ```python
   pip install -r requirements.txt
   ```
8. Create a new file to store the enviroment variables of the project:
   ```python
   touch .env
   ```
9. Manually enter the variables in the .env file using any code editor or run:
    ```python
   echo "VARIABLE_NAME=value" > .env
    ```
    The required variables for this project are :
   DATABASE_URL
   SECRET_KEY
   DEBUG
11. Now, you are officially ready to start the server. For that, run:
    ```python
    python manage.py runserver
    ```
    Copy the link show in the terminal and paste it in you browser. The django app should be running, displaying the home page.
