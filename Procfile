web: cd justlinked-api && alembic upgrade head && gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app