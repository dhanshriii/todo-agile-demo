from flask import Flask, request, redirect, render_template_string, url_for

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

    <form method="POST" action="/">
        <input type="text" name="task" required>
        <button type="submit">Add Task</button>
    </form>

    <hr>

    <h2>All Tasks</h2>

    {% if tasks %}
        <ul>
            {% for task in tasks %}
                <li>
                    {{ loop.index }}. {{ task }}
                    <form method="POST" action="/delete/{{ loop.index0 }}" style="display:inline;">
                        <button type="submit">Delete</button>
                    </form>
                </li>
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
        if task:
            tasks.append(task)
        return redirect(url_for("home"))
    return render_template_string(HTML, tasks=tasks)

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
