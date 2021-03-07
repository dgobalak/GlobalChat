import argparse
from typing import Optional

from firebase_admin import auth
from firebase_admin.auth import UserRecord

from initialise_firebase_admin import app

def create_user(email,user_id,password):
    auth.create_user(email=email, uid=user_id) if user_id else auth.create_user(email=email)
    return set_password(user_id,password)

def set_password(user_id, password):
    return auth.update_user(user_id, password=password)

def delete_user(user_id):
    return auth.delete_user(user_id)

def update_email(user_id, email):
    return auth.update_user(user_id, email=email)


def update_mobile(user_id, mobile_no):
    return auth.update_user(user_id, phone_number=mobile_no)


def update_display_name(user_id, display_name) :
    return auth.update_user(user_id, display_name=display_name)


