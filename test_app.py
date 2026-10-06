import unittest
from app import completed_points, render_page


class DashboardTests(unittest.TestCase):
    def test_counts_only_done_items(self):
        items = [
            {"points": 3, "status": "Done"},
            {"points": 5, "status": "In Progress"},
            {"points": 2, "status": "Done"},
        ]
        self.assertEqual(completed_points(items), 5)

    def test_empty_backlog_returns_zero(self):
        self.assertEqual(completed_points([]), 0)

    def test_unfinished_items_return_zero(self):
        items = [
            {"points": 8, "status": "To Do"},
            {"points": 3, "status": "In Progress"},
        ]
        self.assertEqual(completed_points(items), 0)

    def test_page_contains_title(self):
        self.assertIn("<h1>Sprint Dashboard</h1>", render_page())

    def test_page_displays_completed_points(self):
        self.assertIn("Completed story points: 5", render_page())


if __name__ == "__main__":
    unittest.main()
