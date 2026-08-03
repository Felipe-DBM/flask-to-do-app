import unittest

from app import app, db, Task


class AppTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True, SQLALCHEMY_DATABASE_URI='sqlite:///:memory:')
        self.client = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(Task(title='Sample task'))
            db.session.commit()

    def test_home_page_renders_toggle_form_for_tasks(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'/toggle/1', response.data)


if __name__ == '__main__':
    unittest.main()
