from fastapi_sqlalchemy import db
from fastapi import HTTPException

from models.ProjectModel import Project as Project
from dto.ProjectSchema import Project as ProjectDto



class ProjectService:

    def createProject(project: ProjectDto):
        db_project= Project(project_name=project.project_name, user_id=project.user_id)
        db.session.add(db_project)
        db.session.commit()
        return ProjectDto(
            id=db_project.id,
            project_name=db_project.project_name,
            user_id=db_project.user_id
        )
    
    def getProject(project_id: int):
        db_project = db.session.query(Project).filter(Project.id == project_id).first()
        if db_project is None:
            raise HTTPException(status_code=404, detail="project not found")
        return ProjectDto(
            id=db_project.id,
            project_name=db_project.project_name,
            user_id=db_project.user_id
        )
    
    