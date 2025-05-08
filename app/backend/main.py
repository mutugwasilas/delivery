from fastapi import FastAPI
from routes import auth_routes, order_routes



app = FastAPI()

"""
register routers to the main file
"""
app.include_router(auth_routes.router, prefix="/api")
app.include_router(order_routes.router, prefix="/api")