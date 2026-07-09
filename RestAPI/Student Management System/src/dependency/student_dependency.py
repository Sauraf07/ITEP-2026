from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db_config import get_session
from src.repository.student_repository import StudentRepository
from src.services.student_service import StudentService


def get_student_repository(session:AsyncSession=Depends(get_session)):
    return StudentRepository(session)

def get_student_service(session:AsyncSession=Depends(get_session),student_repo:StudentRepository=Depends(get_student_repository)):
    return StudentService(session,student_repo)
