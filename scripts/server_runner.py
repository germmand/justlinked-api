import uvicorn as asgi


def run_app(app, port=8000, host='0.0.0.0'):
    asgi.run(app, port=port, host=host)
