# Flask Profile App 

A simple Flask web application that lets users create an account by entering their personal details (Name, Age, Email, Phone).  
The app validates inputs (only Gmail addresses, 10-digit phone numbers) and displays the submitted profile in a styled card with confetti celebration.

---

## Features
- Responsive **Create Account form** with Bootstrap styling
- Validation:
  - Age must be numeric
  - Email must end with `@gmail.com`
  - Phone must be exactly 10 digits
- Profile displayed in a colorful card
- Fun **confetti effect** after submission 
- Clean project structure with Flask templates

---

## Project Structure
Task1/
├── app.py              # Main Flask app
├── personal_info.py    # Console version (optional)
└── templates/
    └── profile.html   # Profile display template

## Install Dependencies and setup:
pip install flask
python app.py
python personal_info.py (optional)
Clone the repo: https://github.com/Trishika295/py-personal-profile
Live Demo:  https://trishika295.github.io/py-personal-profile/


