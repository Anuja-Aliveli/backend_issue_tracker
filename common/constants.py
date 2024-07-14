# Database field limits
CHAR_SHORT_LIMIT = 10
CHAR_MEDIUM_LIMIT = 25
CHAR_LONG_LIMIT = 50
CHAR_VERY_LONG_LIMIT = 255
# user mail domain allowed
user_mail_domains_allowed = ['mailinator', 'gmail', 'outlook', 'hotmail']
# Email validation Error Statements
EMAIL_INVALID_ERROR = 'Invalid Email'
EMAIL_INVALID_DOMAIN_ERROR = 'Invalid Email Domain'
EMAIL_USER_ALREADY_EXITS_ERROR = 'User with email already exists'
# Password validation Error Statments
PASSWORD_LENGTH_ERROR = 'Password should be more than 6 characters'
PASSWORD_TYPES_ERROR = 'Use Atleast 1 capital letter, symbol, number'
PASSWORD_CAPITAL_ERROR = 'Use Atleast 1 capital letter'
PASSWORD_SYMBOL_ERROR = 'Use Atleast 1 symbol'
PASSWORD_NUMBER_ERROR = 'Use Atleast 1 Number'
# Login Validation Error Statments
LOGIN_INVALID_DATA_ERROR = 'Invalid Email or Password'
LOGIN_USER_DOES_NOT_EXISTS = 'User Does Not Exists'
# JWT Token Errors
JWT_INVALID_TOKEN = 'Invalid Token'
JWT_TOKEN_EXPIRED = 'Token Expired'
JWT_TOKEN_REQUIRED = 'Token Required'
# Urls without token
TOKEN_NOT_REQUIRED_FOR_URLS = ['/register/', '/login/', '/forgot_password_check_email/', '/reset_user_password/', '/admin/']
# ID CONSTANTS
USER_ID = 'USR'
PROFILE_ID = "PRF"
USER_EXAM_ID = "UEX"
# Profile Validations
PROFILE_CREATION_SUCCESSFUL = 'Profile Created Successfully'
PROFILE_CREATION_FAILED = 'Profile Creation Failed'
PROFILE_UPDATED_SUCCESSFUL = 'Profile Updated Successfully'
# User Statements
USER_LOGIN_SUCCESSFUL = 'User Login successful'
USER_NOT_FOUND = 'User not found'
USER_REGISTER_SUCCESSFUL = 'User registered successfully'
# param variables
EMAIL = 'email'
PASSWORD = 'password'
USER_NAME = 'user_name'