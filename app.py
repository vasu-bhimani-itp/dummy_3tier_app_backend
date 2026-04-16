from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    tasks = []
    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "status": row[2]
        })
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    title = data.get("title")

    if not title:
        return jsonify({"error": "Title required"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    # 🔥 Logic: default status = pending
    cursor.execute("INSERT INTO tasks (title, status) VALUES (?, ?)", (title, "pending"))
    conn.commit()

    return jsonify({"message": "Task created"})

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.json
    status = data.get("status")

    # 🔥 Logic: only allow valid transitions
    if status not in ["pending", "completed"]:
        return jsonify({"error": "Invalid status"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status=? WHERE id=?", (status, id))
    conn.commit()

    return jsonify({"message": "Updated"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()

    return jsonify({"message": "Deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)