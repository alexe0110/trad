from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from src.database import get_async_session
from src.operations.models import operation
from src.operations.schemas import OperationCreate

router = APIRouter(
    tags=["Operation"]
)



@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    print('😌 query = ',query)
    result = await session.execute(query)
    print('😌 result = ',result)
    res = result.all()
    print('😌 result.all() = ', res)
    print('😌 result.all() = ', type(res))

    return JSONResponse(
        status_code=200,
        content=str(res)
    )


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
