from fastapi import Depends, FastAPI

from wishwise_pr.configs.env import get_environment_variables
from wishwise_pr.configs.database.init_models import init_models

from wishwise_pr.routers.user_router import UserRouter
from wishwise_pr.routers.gift_router import GiftRouter
from wishwise_pr.routers.wishlist_router import WishlistRouter
from wishwise_pr.routers.reservation_router import ReservationRouter
from fastapi.openapi.models import SecuritySchemeType
from fastapi.openapi.utils import get_openapi


env = get_environment_variables()

app = FastAPI(
    title="WishWise Backend API",
    version="1.0.0",
)

app.include_router(UserRouter)
app.include_router(GiftRouter)
app.include_router(WishlistRouter)
app.include_router(ReservationRouter)

@app.get("/openapi.json", include_in_schema=False)
async def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": SecuritySchemeType.http,
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", [{"BearerAuth": []}])
    app.openapi_schema = openapi_schema
    return app.openapi_schema

@app.on_event("startup")
async def on_startup():
    await init_models()
# init()
