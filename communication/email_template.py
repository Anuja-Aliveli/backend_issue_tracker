from common.constants import ISSUE_TRACKER


def get_verification_code_message(user_name, verification_code):
    VERIFICATION_CODE_MESSAGE = f"""
    Dear {user_name},
    
    We received a request to reset the password for your account. Please use the following verification code to proceed with resetting your password:
    
    Your Verification Code: {verification_code}
    `
    Please enter this code on the password reset page to complete the process. If you did not request a password reset, please ignore this email.
    
    For your security, the code will expire in 30 minutes.
    
    Thank you,
    {ISSUE_TRACKER} Team
        
    Security Tips:
    
    1. Never share your verification code with anyone.
    2. Always keep your account information secure.
    3. If you suspect any unusual activity, please change your password immediately and notify our support team.
    
    Thank you for using {ISSUE_TRACKER}.
    """
    return VERIFICATION_CODE_MESSAGE