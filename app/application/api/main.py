from fastapi import FastAPI


def create_app() -> FastAPI:
    return FastAPI(
        title='Simple Kafka Chat',
        
        description='A simple kafka + ddd example.',
        debug=True,
    )
