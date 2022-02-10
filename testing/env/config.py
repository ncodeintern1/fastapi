from pydantic import BaseSettings



class Settings(BaseSettings):
    TITLE ="my fastapi application"
    VERSION="0.0.1"
    DESCRIPTION = """
     myApp API helps you do awesome stuff.
     dummay page
  """
    NAME="Nupur Koshti"
    Email="ncode.intern1@gmail.com"

     
class Config:
        env_file = ".env"       
setting=Settings()