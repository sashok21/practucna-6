from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.settings.db import db

SessionDepend = Annotated[AsyncSession, Depends(db.get_session)]