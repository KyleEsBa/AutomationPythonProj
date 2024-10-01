import pytest
import os
from datetime import datetime

class Runner:

    @staticmethod
    def run_tests_with_mark(mark: str):
        testPathTest="../../test/testCases"
        reportDir = "../../test/reports"
        # Create report directory if it doesn't exist
        if not os.path.exists(reportDir):
            os.makedirs(reportDir)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        reportFile = os.path.join(reportDir, f"report_{timestamp}.html")

        pytest_args = [
            testPathTest,
            "-v",
            f"-m {mark}",
            f"--html={reportFile}",  # HTML report path
            "--self-contained-html"   # Embed CSS and JS into the HTML report
        ]
        pytest.main(pytest_args)

if __name__ == "__main__":
    # Running by mark
    Runner.run_tests_with_mark("wip")