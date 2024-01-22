This is a Django project base onf Beginning Django E-Commerce Book for Software Architecture and Design class at PTIT year 4

Using conda environment to manage package

```shell
conda create -n <env_name> python=3.12
```

```shell
conda activate <env_name>
pip install requirements.txt
python manage.py runserver
```

# To runserver with your own database

  - Create an .env file which use by python-decouple package which in requirements.txt
  - Add your database information to .env file:
    - DEBUG=your-own-value(True or False)
    - ALLOW_HOSTS=your-own-value
    - SECRET_KEY=your-own-value(Use Django Secret Key Generator)
    - DB_HOST=your-own-value
    - DB_PORT=your-own-value
    - DB_NAME=your-own-value
    - DB_USER=your-own-value
    - DB_PASSWORD=your-own-value