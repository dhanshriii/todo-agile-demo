from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

tasks = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Todo App</title>
</head>
<body>
    <h2>Add a Task</h2>

    <form method="POST">
        <input type="text" name="task" required>
        <button type="submit">Add Task</button>
    </form>

    <hr>

    <h2>All Tasks</h2>

    {% if tasks %}
        <ul>
            {% for task in tasks %}
                <li>{{ loop.index }}. {{ task }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>No tasks added yet.</p>
    {% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        tasks.append(task)
        return redirect("/")
    return render_template_string(HTML, tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
