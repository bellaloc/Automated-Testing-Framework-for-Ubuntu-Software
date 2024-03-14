# Automated Testing Framework API Reference

Welcome to the API reference for the Automated Testing Framework! This reference guide provides information on the available endpoints and functionalities of the backend API.

## Table of Contents
1. [Introduction](#introduction)
2. [Endpoints](#endpoints)
3. [Request and Response Formats](#request-and-response-formats)

## Introduction
The Automated Testing Framework backend provides a RESTful API for managing test suites, test cases, and test results. This API allows developers to interact with the framework programmatically to perform various testing tasks.

## Endpoints
### GET /test-suites
- Description: Retrieve a list of all test suites.
- Response: JSON array containing test suite objects.

### POST /test-suites
- Description: Create a new test suite.
- Request: JSON object containing test suite details.
- Response: JSON object confirming creation of the test suite.

### GET /test-suites/{suite_id}
- Description: Retrieve details of a specific test suite.
- Parameters:
  - `suite_id`: ID of the test suite.
- Response: JSON object containing test suite details.

### GET /test-cases/{suite_id}
- Description: Retrieve all test cases belonging to a test suite.
- Parameters:
  - `suite_id`: ID of the test suite.
- Response: JSON array containing test case objects.

### POST /test-cases/{suite_id}
- Description: Create a new test case within a test suite.
- Parameters:
  - `suite_id`: ID of the test suite.
- Request: JSON object containing test case details.
- Response: JSON object confirming creation of the test case.

### POST /execute-tests/{suite_id}
- Description: Execute all tests within a test suite.
- Parameters:
  - `suite_id`: ID of the test suite.
- Response: JSON object containing execution status and results.

## Request and Response Formats
### Test Suite Object
```json
{
  "id": 1,
  "name": "Test Suite 1"
}

Test Case Object

{
  "id": 1,
  "name": "Test Case 1",
  "input": "input_data",
  "expected_output": "expected_output_data",
  "conditions": "test_conditions"
}

Execution Result Object

{
  "suite_id": 1,
  "status": "success",
  "results": [
    {
      "test_case_id": 1,
      "name": "Test Case 1",
      "result": "pass"
    },
    {
      "test_case_id": 2,
      "name": "Test Case 2",
      "result": "fail"
    }
  ]
}
That's it! You now have access to the API reference for the Automated Testing Framework backend.

