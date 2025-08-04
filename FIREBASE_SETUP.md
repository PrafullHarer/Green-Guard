# Firebase Password Reset Setup Guide

## 🔧 Firebase Project Configuration

To ensure the password reset functionality works correctly, follow these steps in your Firebase Console:

### 1. Enable Email/Password Authentication

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project: `greenguard-408ed`
3. Navigate to **Authentication** → **Sign-in method**
4. Enable **Email/Password** provider
5. Make sure **Email link (passwordless sign-in)** is also enabled if needed

### 2. Configure Password Reset Settings

1. In **Authentication** → **Settings** → **General**
2. Scroll down to **Authorized domains**
3. Add your domain (e.g., `localhost` for development)
4. In **Templates** → **Password reset**
5. Customize the email template if needed
6. Set the **Action URL** to: `http://localhost:8000/templates/reset_password.html`

### 3. Email Configuration

1. In **Authentication** → **Settings** → **General**
2. Verify your **Sender email** is set correctly
3. Test the email delivery by sending a test password reset

## 🔗 How the Link-Based Reset Works

### Step 1: User Requests Reset
- User enters email on `forget_password.html`
- System checks if email exists in Firebase
- If valid, Firebase sends reset email with secure link

### Step 2: User Clicks Reset Link
- Email contains link like: `https://greenguard-408ed.firebaseapp.com/__/auth/action?mode=resetPassword&oobCode=...`
- Link redirects to `reset_password.html` with reset code

### Step 3: User Sets New Password
- User enters new password on `reset_password.html`
- System validates password strength
- Firebase updates the password
- User is redirected to login page

## 🛠️ Troubleshooting

### Common Issues:

1. **"Email not registered" error**
   - Check if user actually exists in Firebase Console
   - Verify email spelling
   - Ensure user was created with email/password method

2. **Reset link not working**
   - Check Firebase project settings
   - Verify authorized domains
   - Check email spam folder

3. **Password reset email not received**
   - Check Firebase email settings
   - Verify sender email configuration
   - Check email provider settings

### Testing Steps:

1. **Register a test user**:
   - Go to `templates/register.html`
   - Create account with test email

2. **Test password reset**:
   - Go to `templates/forget_password.html`
   - Enter test email
   - Check email for reset link

3. **Complete password reset**:
   - Click link in email
   - Set new password on `reset_password.html`
   - Verify login works with new password

## 📧 Email Template Customization

You can customize the password reset email in Firebase Console:

1. Go to **Authentication** → **Templates** → **Password reset**
2. Customize:
   - Subject line
   - Email content
   - Action URL
   - Sender name

## 🔒 Security Features

- Reset links expire after 1 hour
- Links can only be used once
- Secure token-based authentication
- Password strength validation
- Rate limiting protection

## 📱 Mobile Responsive

Both pages are mobile-responsive and work on all devices.

## 🚀 Deployment Notes

When deploying to production:

1. Update authorized domains in Firebase Console
2. Change action URL to your production domain
3. Test the complete flow
4. Monitor Firebase Console for any errors 