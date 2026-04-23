# QA Automation Framework — SauceDemo

## Overview

This project contains an end-to-end UI automation framework for the SauceDemo application using Playwright and pytest.
It follows a Page Object Model (POM) design and focuses on validating core user flows.

In addition to UI automation, API tests have also been implemented using Playwright’s request context.

---

## Objective

* Validate critical user journeys (login, cart, checkout)
* Ensure application stability and correctness
* Build a clean and maintainable automation framework
* Cover both UI and API testing scenarios

---

## Project Structure

```
pages/
  base_page.py
  login_page.py
  products_page.py
  cart_page.py
  checkout_page.py

tests/
  test_login.py
  test_products.py
  test_cart.py
  test_checkout.py
  test_sorting.py

api_tests/
  test_api.py

reports/

conftest.py
pytest.ini
requirements.txt
README.md
```

---

## Configuration

The project uses the following pytest configuration:

```
[pytest]
addopts = -v --headed --slowmo=500
base_url = https://www.saucedemo.com
```

### Notes:

* Tests run in **headed mode by default** (browser visible)
* Slow execution is enabled for easier observation
* This can be overridden during execution

---

## Test Coverage

### UI Testing

**Login**

* Valid and invalid login scenarios
* Different user types (standard, locked, etc.)

**Products**

* Product visibility and details
* Sorting (price and name)

**Cart**

* Add/remove items
* Badge validation
* Multiple item handling
* Cart persistence after reload

**Checkout**

* End-to-end checkout flow
* Form validation

---

### API Testing

API tests are implemented using `APIRequestContext`.

Endpoints covered:

* GET /posts
* GET /posts/{id}
* Invalid ID handling
* POST /posts
* PUT /posts/{id}
* DELETE /posts/{id}
* GET /users/{id}/posts

Validations include:

* Status codes
* Response structure
* Data types
* Basic business checks

---

## Setup Instructions

### 1. Clone repository

```
git clone <your-repo-url>
cd E2E-Automation
```

---

### 2. Create virtual environment

```
python -m venv .venv
```

---

### 3. Activate environment

Windows:

```
.venv\Scripts\activate
```

Mac/Linux:

```
source .venv/bin/activate
```

---

### 4. Install dependencies

```
python -m pip install --upgrade pip
pip install pytest pytest-playwright pytest-xdist pytest-html
```

---

### 5. Install browsers

```
playwright install
```

---

## Test Execution

### Run UI tests (default)

```
pytest
```

---

### Run in headless mode

```
pytest -o addopts=""
```

---

### Run API tests

```
pytest api_tests/
```

---

### Run in parallel

```
pytest -n auto -o addopts=""
```

---

### Run with HTML report

```
pytest -n auto -o addopts="" --html=reports/report.html --self-contained-html
```

---

## Reporting

HTML reports are generated in the `reports/` folder and include:

* Test execution summary
* Pass/Fail results
* Failure details

---

## Approach

Testing is based on a simple risk-based approach:

* High priority: login, checkout
* Medium priority: cart, sorting
* Lower priority: UI validations

Focus was kept on:

* Core functionality
* Real user behavior
* Stability over exhaustive coverage

---

## Notes

* API testing is included as part of the assignment
* Headed execution is used by default for visibility
* Parallel execution is supported for faster runs

---

## Author

Atul Rawat
