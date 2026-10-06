from html import escape


def completed_points(items):
    return sum(
        item["points"]
        for item in items
        if item["status"] == "Done"
    )


def render_page():
    items = [
        {"title": "Create backlog", "points": 3, "status": "Done"},
        {"title": "Build dashboard", "points": 5, "status": "In Progress"},
        {"title": "Review requirements", "points": 2, "status": "Done"},
    ]
    goal = "Deliver a tested dashboard through an automated pipeline."
    total = completed_points(items)
    rows = "".join(
        f"<li>{escape(item['title'])}: "
        f"{item['points']} points — {escape(item['status'])}</li>"
        for item in items
    )
    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sprint Dashboard</title>
</head>
<body>
    <h1>Sprint Dashboard</h1>
    <p><strong>Sprint goal:</strong> {escape(goal)}</p>
    <p>Completed story points: {total}</p>
    <ul>{rows}</ul>
</body>
</html>
"""
