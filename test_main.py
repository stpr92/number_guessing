import unittest
import runpy

class TestRun(unittest.TestCase):
    def test_program_runs(self):
        try:
            runpy.run_path("main.py", run_name="__main__")
        except Exception as e:
            self.fail(f"Program crashed with exception: {e}")

if __name__ == "__main__":
    unittest.main()
