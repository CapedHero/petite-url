# Petite URL

+ Petite URL is a URL shortener service.

+ For fun and demonstration purposes, I implemented some clean architecture 
  principles in this project. If this were a production project, I would have
  very carefully considered the trade-offs of following this architecture. 
  Especially given that Django is extremely coupled with its ORM and models.

+ I got some development speed-ups by copying code from my previous projects,
  so it wasn't as time-consuming as it seems.

## Project Configuration

```shell
# Create a virtual environment.
python -m venv venv
source venv/bin/activate

# Install the project dependencies.
pip install --upgrade pip
pip install -r requirements.txt

# Run the database migrations.
./manage.py migrate
```

## Running the Project

```shell
./manage.py runserver
```

You can verify that the project is working as intended with the following commands:

```shell
# In a separate terminal window:
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"target_url":"https://example.com"}' \
  http://localhost:8000/api/petitify

# Then, you can follow the link returned by the previous command and check if it
# redirects you to the target URL.
```

## Ad-hoc TODO List

+ Analyze factual business requirements, especially regarding project's purpose,
  users, scale, and security.

+ Add extensive test suite.

+ Implement petite code collision handling.

+ Improve handling web exceptions.

+ Integrate Postgres.

+ Dockerize the project.

+ Update & refactor Django settings.

+ Add Linters.

+ Integrate CI/CD.
