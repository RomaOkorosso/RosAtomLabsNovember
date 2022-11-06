import fastapi
from db.db import Base, engine

Base.metadata.create_all(bind=engine)
app = fastapi.FastAPI()

