db:
	docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres


run:
	export FLASK_ENV=development
	poetry run flask --app python_playground.main:app run