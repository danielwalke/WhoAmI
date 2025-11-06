from fastapi import APIRouter, UploadFile, File, HTTPException, Request, Form
from typing import List
from pathlib import Path
import shutil
import uuid
from datetime import datetime
from utils.DocumentValidator import DocumentValidator
from constants.Router import SERVER_PREFIX, UPLOAD_MULTIPLE_ROUTE
from constants.Upload import UPLOAD_DIR
from utils.DatabaseUtils import SessionDep
from database.database_classes.Room import Room
from database.database_classes.Image import Image
from utils.RoomCheck import verify_room_auth

doc_validator = DocumentValidator(max_size=10 * 1024 * 1024) # 10MB limit
router = APIRouter(
    tags=[SERVER_PREFIX],
    redirect_slashes=False
)


@router.post(UPLOAD_MULTIPLE_ROUTE)
async def upload_multiple_files(request: Request, files: List[UploadFile], session: SessionDep):
    """Upload multiple files with validation"""
    room = session.get(Room, "d34358c9-37e4-4026-a6c7-f103f16848d1")
    verify_room_auth("test", room)
    
    if len(files) > 24:  # Limit number of files
        raise HTTPException(
            status_code=400,
            detail="Too many files. Maximum 24 files allowed."
        )

    results = []

    for file in files:
        validation = await doc_validator.validate_file(file)

        if not validation["valid"]:
            results.append({
                "filename": file.filename,
                "success": False,
                "errors": validation["errors"]
            })
            continue

        file_ext = Path(file.filename).suffix
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        file_path = UPLOAD_DIR / unique_filename

        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            file_url = request.url_for("static", path=unique_filename)
            name = file.filename
            if "." in name:
                name = name.split(".")[0]
            image = Image(
                id=unique_filename,
                name=name,
                url=str(file_url),
                room_id=room.id
            )
            session.add(image)
            
            results.append({
                "filename": file.filename,
                "stored_filename": unique_filename,
                "success": True,
                "location": str(file_path),
                "url": file_url
            })
        except Exception as e:
            results.append({
                "filename": file.filename,
                "success": False,
                "errors": [f"Failed to save: {str(e)}"]
            })
        

    successful = [r for r in results if r["success"]]
    failed = [r for r in results if not r["success"]]
    session.commit()
    return {
        "total_files": len(files),
        "successful": len(successful),
        "failed": len(failed),
        "upload_time": datetime.utcnow().isoformat(),
        "results": results
    }