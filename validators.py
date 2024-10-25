from marshmallow import Schema, fields, validate, ValidationError
import re
PASSWORD_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

# def validate_domain(email):
#     domain = email.split('@')[-1]
#     # Example: Validate that the domain is 'example.com'
#     if domain != '.com' or '.tech':
#         raise ValidationError('Email domain must be "example.com".')
class UserSchema(Schema):
    name=fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email=fields.Email(required=True, validate=[validate.Length(min=5,max=100),validate.Regexp(r'^[^@]+@[^@]+\.[^@]+$')])
    phone=fields.Int(required=True)
    age=fields.Int(required=True, validate=validate.Range(min=1,max=120))
    password=fields.Str(required=True, validate=[validate.Length(min=8),validate.Regexp(PASSWORD_REGEX, error="Password must be at least 8 characters long, contain an uppercase letter, a lowercase letter, a digit, and a special character.")])
    role=fields.Str(required=True,validate=validate.OneOf(["user", "admin", "moderator"]))
class UserUpdateSchema(Schema):
    name=fields.Str(required=False, validate=validate.Length(min=1, max=100))
    email=fields.Email(required=False, validate=[validate.Length(min=5,max=100),validate.Regexp(r'^[^@]+@[^@]+\.[^@]+$')])
    phone=fields.Int(required=False)
    age=fields.Int(required=False, validate=validate.Range(min=1,max=120))
    password=fields.Str(required=False, validate=[validate.Length(min=8),validate.Regexp(PASSWORD_REGEX, error="Password must be at least 8 characters long, contain an uppercase letter, a lowercase letter, a digit, and a special character.")])
    role=fields.Str(required=False,validate=validate.OneOf(["user", "admin", "moderator"]))

def validate_user(user_data):
    schema=UserSchema()
    return schema.load(user_data)

def validate_user_update(data):
    schema = UserUpdateSchema()
    return schema.load(data)