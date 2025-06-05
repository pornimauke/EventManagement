from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes.event_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)


import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
