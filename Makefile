db:
	docker run --name sql_a_test -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres


run:
	export FLASK_ENV=development
	poetry run flask --app sql_a_example.main:app run