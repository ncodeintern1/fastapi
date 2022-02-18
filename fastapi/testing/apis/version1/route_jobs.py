from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from typing import List        
from db.session import get_db
from db.models.jobs import Job
from schemas.jobs import JobCreate,ShowJob
from db.repository.jobs import create_new_job,retreive_job
router = APIRouter()



@router.post("/create-job/",response_model=ShowJob)
def create_job(job: JobCreate,db: Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job=job,db=db,owner_id=current_user)
    return job


def read_job(id:int,db:Session = Depends(get_db)):
    job = retreive_job(id=id,db=db)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Job with this id {id} does not exist")
    return job

def read_jobs(db:Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return jobs




def retreive_job(id: int, db: Session):
    item = db.query(Job).filter(Job.id == id).first()
    return item


def list_jobs(db : Session):    #new
    jobs = db.query(Job).all().filter(Job.is_active == True)
    return jobs