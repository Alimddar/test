from fastapi import  FastAPI
from models import Base,User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware

engine = create_engine(f"mysql+pymysql://root:test@db/user_db")
Session = sessionmaker(bind=engine)

def recreate_database():
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

recreate_database()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

