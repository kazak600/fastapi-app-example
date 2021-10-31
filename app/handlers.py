from fastapi import APIRouter, Body

router = APIRouter()


@router.get('/user', name='user:get')
async def get_user():
    return {'user': None}


@router.post('/user', name='user:create')
async def create_user(body=Body(..., embed=True)):
    return {'user': None}
