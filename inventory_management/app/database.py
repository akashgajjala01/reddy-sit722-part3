from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://reddy_sit722_part2_uc59_user:KNSBcPt8xOSQdGVGLtS1QlaKQBHlmRGe@dpg-crkbmvjv2p9s73b4pr1g-a.oregon-postgres.render.com/reddy_sit722_part2_uc59")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
