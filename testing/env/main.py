from fastapi import FastAPI
from config import setting

description = """
myApp API helps you do awesome stuff. 🚀
## Items

You can **read items**.

"""


tags_metadata = [
    {
        "name": "user",
        "description": "there are my user related router",
    },
    {
        "name": "product",
        "description": "there are my product related router",
    }
]

APP = FastAPI(title=setting.TITLE,
    description=setting.DESCRIPTION,
    version=setting.VERSION,
    contact={"name": setting.NAME,
    "email": setting.Email},
    openapi_tags=tags_metadata,
    redoc_url=None)


    


@APP.get('/users',tags=["user"])
def get_user():
    return{"message":"hello user"}

@APP.get('/items',tags=["product"])
def get_items():
    return{"message":"hello items"}
