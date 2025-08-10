from fastapi import FastAPI
from routers import users,products,orders,cart

app = FastAPI(title="eCommerce API")

app.include_router(users.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(orders.router)

@app.get("/")
def home():
    return {"message": "Hello World"}
