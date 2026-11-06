"""Exercise local saving without allowing the editor to spawn Git or other processes."""
import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("editor", Path(__file__).resolve().parents[1] / "scripts/server.py")
editor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(editor)


class EditorSaveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.previous_cwd = Path.cwd()
        os.chdir(self.temp.name)
        self.addCleanup(self.temp.cleanup)
        self.addCleanup(os.chdir, self.previous_cwd)
        editor.app.config.update(TESTING=True)
        self.client = editor.app.test_client()

    def save(self, title="Review-only article"):
        # Any previous git add/commit/push code would fail this test.
        with patch("subprocess.Popen", side_effect=AssertionError("editor must not run processes")):
            return self.client.post("/publish", data={"title": title, "category": "content-strategy", "content": "## Example\nBody"})

    def test_save_creates_one_local_file_and_returns_honest_confirmation(self):
        response = self.save()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, "/?saved=1")
        files = list(Path("_posts").glob("*.md"))
        self.assertEqual(len(files), 1)
        self.assertIn("Body", files[0].read_text())
        page = self.client.get(response.location)
        self.assertIn("已儲存本機文章，尚未上線。", page.get_data(as_text=True))

    def test_duplicate_save_does_not_overwrite_existing_article(self):
        self.assertEqual(self.save().status_code, 302)
        file = next(Path("_posts").glob("*.md"))
        file.write_text("existing user content")
        self.assertEqual(self.save().status_code, 409)
        self.assertEqual(file.read_text(), "existing user content")

    def test_invalid_title_does_not_create_a_file(self):
        for title in ["", "   ", "!!!"]:
            with self.subTest(title=title):
                self.assertEqual(self.save(title).status_code, 400)
        self.assertFalse(Path("_posts").exists())

    def test_preview_does_not_save_or_start_processes(self):
        with patch("subprocess.Popen", side_effect=AssertionError("preview must not run processes")):
            response = self.client.post("/", data={"title": "Preview", "content": "## Example"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Example", response.get_data(as_text=True))
        self.assertFalse(Path("_posts").exists())


if __name__ == "__main__":
    unittest.main()
