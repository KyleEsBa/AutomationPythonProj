import pytest
import os

class Runner:

    @staticmethod
    def run_tests_with_mark(mark: str, test_path: str = ""):
        if not os.path.exists(test_path):
            raise ValueError(f"Test path '{test_path}' does not exist.")

        pytest_args = [test_path, "-v", f"-m {mark}"]
        pytest.main(pytest_args)

if __name__ == "__main__":
    # Running by mark
    Runner.run_tests_with_mark("wip", "C:\\Users\\User\\IdeaProjects\\AutomationPythonProj\\testCases")