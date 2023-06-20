# "Web-Travel"
## Webiste for holders

### Lounch instruction:
After cloning the repository open it as a work directory. Then do the following:

### 1. Create and activate virtual local-environment. Installing packages

###  for Windows:
```bash
python -m venv .venv
```
```bash
cd .venv/Scripts
```
```bash
.\activate
```
```bash
cd ../..
```
```bash
pip install -r requirements.txt
```

###  for Linux:
```bash
python3 -m venv .venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```

<hr>

### 2. Set global environment variables
```bash
cp .env-example .env
```
After it ask the SECRET_KEY from developer and paste it into .env instead of what is there.

### 3. Start applications
```bash
cd backend
```
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
python manage.py createsuperuser
```

After it type admin login, email and password. Then run server by:

```bash
python manage.py runserver
```

#### After everything above type http://127.0.0.1:8000/swagger-ui/ in your browser. Click Authoize in the top right corner and log in using your login and password. After it you can use endpoints that described in the documentation.