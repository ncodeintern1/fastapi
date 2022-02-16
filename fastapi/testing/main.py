from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.version1 import route_general_pages
from db.session import engine   #new
from db.base import Base  #new
from apis.base import api_router #n


def include_router(app):
	app.include_router(route_general_pages)



def include_router(app):   
	app.include_router(api_router) #modified

def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
	print("create_tables")
	Base.metadata.create_all(bind=engine)


	
def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	configure_static(app)
	create_tables()       #new
	return app

app = start_application()