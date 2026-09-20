from flask import Flask, render_template, request

app = Flask(__name__)

def is_valid_email(email):
    return email.endswith("@gmail.com")

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        email = request.form["email"]
        phone = request.form["phone"]

        # Validation
        if not age.isdigit():
            return "Invalid age format. Please enter a number."
        if not is_valid_email(email):
            return "Invalid email format. Only Gmail addresses ending with @gmail.com are allowed."
        if not is_valid_phone(phone):
            return "Invalid phone number. It must contain exactly 10 digits."

        return render_template("profile.html", name=name, age=age, email=email, phone=phone)

    # Styled form with background and header color
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Personal Information</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(to right, #cce7ff, #e6f2ff); 
            font-family: Arial, sans-serif;
        }
        .card {
            border-radius: 15px;
        }
        .card-header {
            background-color: black; 
        }
        .card-header h4 {
            margin: 0;
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <div class="card shadow mx-auto" style="max-width: 400px;">
            <div class="card-header text-center text-white">
                <h4>Personal Information</h4>
            </div>
            <div class="card-body">
                <form method="POST">
                    <div class="mb-3">
                        <label class="form-label">Name</label>
                        <input type="text" class="form-control" name="name" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Age</label>
                        <input type="number" class="form-control" name="age" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Email</label>
                        <input type="email" class="form-control" name="email" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Phone</label>
                        <input type="text" class="form-control" name="phone" required>
                    </div>
                    <button type="submit" class="btn btn-success w-100">Submit</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
'''


if __name__ == "__main__":
    app.run(debug=True)
