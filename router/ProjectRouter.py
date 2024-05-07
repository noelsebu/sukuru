from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db


from dto.ProjectSchema import Project as ProjectDto
from models.ProjectModel import Project as Project


from service.ProjectService import ProjectService as projectService

router = APIRouter(prefix="/project", tags=["Project"])

@router.post("/create", response_model=ProjectDto)
async def createProject(project: ProjectDto):
    return projectService.createProject(project)

@router.get("/{projectId}", response_model=ProjectDto)
async def getProject(projectId: int):
    return projectService.getProject(projectId)