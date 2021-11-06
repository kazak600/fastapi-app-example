from fastapi import APIRouter, Body, Depends
from app.models import Stream, User, connect_db
from app.forms import StreamForm, UserCreateForm, UserLoginForm
from app.utils import get_password_hash

router = APIRouter()


@router.post('/login')
def login(user: UserLoginForm = Body(..., embed=True), database=Depends(connect_db)):
    return {'user': None}


@router.get('/user', name='user:get')
def get_user():
    return {'user': None}


@router.post('/user', name='user:create')
def create_user(user: UserCreateForm = Body(..., embed=True), database=Depends(connect_db)):
    new_user = User(email=user.email, password=get_password_hash(user.password))
    database.add(new_user)
    database.commit()
    return {'user_id': new_user.id}


@router.get('/stream')
def get_stream(database=Depends(connect_db)):
    all_streams = database.query(Stream).all()
    return all_streams


@router.post('/stream')
def create_stream(item: StreamForm = Body(..., embed=True), database=Depends(connect_db)):
    stream = Stream(title=item.title, topic=item.topic)
    database.add(stream)
    database.commit()
    return {'stream': {'status': 'created'}}
