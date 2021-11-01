from fastapi import APIRouter, Body, Depends
from app.models import Stream, connect_db
from app.forms import StreamForm

router = APIRouter()


@router.get('/user', name='user:get')
async def get_user():
    return {'user': None}


@router.post('/user', name='user:create')
async def create_user(body=Body(..., embed=True)):
    return {'user': None}


@router.get('/stream')
def get_stream(session=Depends(connect_db)):
    all_streams = session.query(Stream).all()
    return all_streams


@router.post('/stream')
def create_stream(item: StreamForm = Body(..., embed=True), session=Depends(connect_db)):
    stream = Stream(title=item.title, topic=item.topic)
    session.add(stream)
    session.commit()
    return {'stream': {'status': 'created'}}
