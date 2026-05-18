from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Password Strength Checker</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 500px; margin: 100px auto; padding: 20px; }
        input { width: 100%; padding: 10px; margin: 10px 0; font-size: 16px; }
        button { width: 100%; padding: 10px; background: #007bff; color: white; border: none; font-size: 16px; cursor: pointer; }
        .result { margin-top: 20px; padding: 15px; border-radius: 5px; }
        .strong { background: #d4edda; color: #155724; }
        .moderate { background: #fff3cd; color: #856404; }
        .weak { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <h2>Password Strength Checker</h2>
    <input type="password" id="password" placeholder="Enter your password">
    <button onclick="checkPassword()">Check Password</button>
    <div id="result"></div>

    <script>
        async function checkPassword() {
            const password = document.getElementById("password").value;
            const response = await fetch("/check", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({password: password})
            });
            const data = await response.json();
            const result = document.getElementById("result");
            result.className = "result " + data.strength.toLowerCase();
            result.innerHTML = "<strong>" + data.strength + " Password</strong><br>" + data.feedback.join("<br>");
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    password = data.get('password', '')
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Add at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add a number")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add a special character (!@#$%^&*)")

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {"strength": strength, "feedback": feedback}

if __name__ == '__main__':
    app.run(debug=True)