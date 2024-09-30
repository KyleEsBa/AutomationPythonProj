import pytest
import os

class Runner:

    @staticmethod
    def run_tests_with_mark(mark: str, testPathTest: str = ""):
        if not os.path.exists(testPathTest):
            raise ValueError(f"Test path '{testPathTest}' does not exist.")

        pytest_args = [testPathTest, "-v", f"-m {mark}"]
        pytest.main(pytest_args)

if __name__ == "__main__":
    # Running by mark
    Runner.run_tests_with_mark("wip", "C:\\Users\\User\\IdeaProjects\\AutomationPythonProj\\testCases")