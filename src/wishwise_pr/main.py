from fastapi import Depends, FastAPI

from wishwise_pr.configs.env import get_environment_variables
from wishwise_pr.configs.database.init_models import init_models

from wishwise_pr.routers.user_router import UserRouter
from wishwise_pr.routers.gift_router import GiftRouter
from wishwise_pr.routers.wishlist_router import WishlistRouter
from wishwise_pr.routers.reservation_router import ReservationRouter



env = get_environment_variables()

app = FastAPI(
    title="WishWise Backend API",
    version="1.0.0",
)

app.include_router(UserRouter)
app.include_router(GiftRouter)
app.include_router(WishlistRouter)
app.include_router(ReservationRouter)

@app.on_event("startup")
async def on_startup():
    await init_models()
# init()
