from fastapi import FastAPI


def create_app():
    return FastAPI(docs_url="/api/docs", debug=True)
