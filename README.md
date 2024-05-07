This is a sample project using fastapi,SqlAlchemy, postgres.This project uses alembic.

Run the following code to enable migration.

alembic revision --autogenerate -m "New Migration"
alembic upgrade head
