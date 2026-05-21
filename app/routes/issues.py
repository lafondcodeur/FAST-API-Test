import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueOut, IssueUpdate

from app.storage import load_data, save_data

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get("/", response_model=list[IssueOut])
def get_issues():
    """Retrieve all issues"""
    issues = load_data()
    return []
