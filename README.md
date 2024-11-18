# <p style="text-align: center;">Python Test Automation Framework</p>
The project is a Testing Automation framework based on Python.

## Purpose
Implementation of automated test scripts

## Project Structure
```plaintext
├── test/
│   ├── step_definition/        # Test steps
│   ├── pages/                  # Page Object Models
│   ├── utilities/              # Customized methods
│   ├── runner/                 # Run configurations              
├── resources/
│   ├── testData/               # Test data
├── output                      # Test reports + logs + screenshots
├── requirement.txt             # Dependencies
├── Configuration.ini           # Configuration files
```

## Stack of tools
- Selenium
- Pytest
- Openpyxl

## Design patterns
- Singleton
- Page Object Model
- DDT (Data Driven Testing)

## Pre requirements
- Python 3 to up

## Installation
1. Clone the repository
2. Reload the requirements.txt to get the dependencies

## Execution of tests
1. Change the config of the Configuration.properties (the URL of the page to test)
2. Generate a class to implement the test steps
3. Set markers on the scenarios or tests to be executed (e.g. @regression)
4. Set the locators of the test in a page class
5. Enter the marker to be executed on the Runner class (e.g. on Runner.run_tests_with_mark("@regression"))
6. Execute on the Runner class

***Happy Testing!***