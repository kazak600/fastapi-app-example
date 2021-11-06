import uuid
from datetime import datetime

from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status

from app.models import Stream, User, AuthToken, connect_db
from app.forms import StreamForm, UserCreateForm, UserLoginForm, UserGetForm
from app.authentication import check_auth_token
from app.utils import get_password_hash

router = APIRouter()


@router.post('/login')
def login(user_form: UserLoginForm = Body(..., embed=True), database=Depends(connect_db)):
    user = database.query(User).filter(User.email == user_form.email).one_or_none()
    if not user or get_password_hash(user_form.password) != user.password:
        return {'error': 'Email/password doesnt match'}

    auth_model = AuthToken(token=str(uuid.uuid4()), user_id=user.id, created_at=datetime.now())
    database.add(auth_model)
    database.commit()
    return {'auth_token': auth_model.token}


@router.get('/user', name='user:get')
def get_user(token: AuthToken = Depends(check_auth_token), database=Depends(connect_db)):
    user = database.query(User).filter(User.id == token.user_id).one_or_none()
    return {'user': user.get_filtered_data()}


@router.post('/user', name='user:create')
def create_user(user: UserCreateForm = Body(..., embed=True), database=Depends(connect_db)):
    exists_user = database.query(User.id).filter(User.email == user.email).one_or_none()
    if exists_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email already taken',
        )

    new_user = User(
        email=user.email,
        password=get_password_hash(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
        nickname=user.nickname
    )
    database.add(new_user)
    database.commit()
    return {'user_id': new_user.id}


@router.get('/stream', name='stream:get')
def get_stream(token: AuthToken = Depends(check_auth_token), database=Depends(connect_db)):
    streams_list = database.query(Stream).filter(Stream.user_id == token.user_id).all()
    return streams_list


@router.post('/stream', name='stream:create')
def create_stream(
        token: AuthToken = Depends(check_auth_token),
        stream_form: StreamForm = Body(..., embed=True),
        database=Depends(connect_db)
):
    stream = Stream(user_id=token.user_id, title=stream_form.title, topic=stream_form.topic, description=stream_form.description)
    database.add(stream)
    database.commit()
    return {'status': 'created'}
