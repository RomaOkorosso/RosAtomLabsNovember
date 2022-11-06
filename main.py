import fastapi
from db.db import Base, engine
from routes.events import event_router

Base.metadata.create_all(bind=engine)
app = fastapi.FastAPI()

app.include_router(event_router)
