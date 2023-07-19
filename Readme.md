# "Web-Travel"
## Webiste for holders

### Lounch instruction:
After cloning the repository open it as a work directory. Then do the following:

```bash
cp backend/.env-example backend/.env
```
```bash
docker-compose up --build -d
```

#### After everything above type http://127.0.0.1:4000/swagger-ui in your browser.

#### Admin-panel http://127.0.0.1:4000/admin
- user: admin
- password: 123123

Notes:
- If django can't connect to database, just waite a minute: it means that the mysql hasn't create the neccessary db yet.
- If some of containters didn't up, just try up it again, it must works;
