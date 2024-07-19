from common.constants import ISSUE_TRACKER


def get_verification_code_message(user_name, verification_code):
        
    VERIFICATION_CODE_MESSAGE = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">
        <div style="width: 100%; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px;">
            <h2 style="color: #333;">Hello {user_name},</h2>
            <p>We received a request to reset the password for your account. Please use the following verification code to proceed with resetting your password:</p>
            <p style="font-size: 1.5em; font-weight: bold; color: #4CAF50;">Your Verification Code: {verification_code}</p>
            <p>Please enter this code on the password reset page to complete the process. If you did not request a password reset, please ignore this email.</p>
            <p>Thank you,</p>
            <p><strong>{ISSUE_TRACKER} Team</strong></p>
            <hr style="border: 0; border-top: 1px solid #ddd; margin: 20px 0;">
            <h3 style="color: #333;">Security Tips:</h3>
            <ul style="list-style-type: disc; padding-left: 20px;">
                <li>Never share your verification code with anyone.</li>
                <li>Always keep your account information secure.</li>
                <li>If you suspect any unusual activity, please change your password immediately and notify our support team.</li>
            </ul>
            <p>Thank you for using {ISSUE_TRACKER}.</p>
        </div>
    </body>
    </html>
    """
    return VERIFICATION_CODE_MESSAGE