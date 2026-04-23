# 🧪 QA Automation Framework — SauceDemo

## 📌 Overview

This project implements an end-to-end **UI automation framework** for the SauceDemo application using **Playwright (Python)** and **pytest**.

The framework follows a **Page Object Model (POM)** design and focuses on **risk-based testing**, prioritizing critical user journeys such as login, cart, checkout, and sorting.

---

## 🎯 Objective

* Validate **core business flows** (login → cart → checkout)
* Ensure **functional correctness and stability**
* Build a **maintainable and scalable automation framework**
* Demonstrate **QA thinking and prioritization**

---

## 🏗️ Framework Design

### ✅ Page Object Model (POM)

* All locators and UI interactions are encapsulated in page classes
* Tests contain only business logic
* No raw locators used in test files
* Improves maintainability and readability

---

## 📂 Project Structure

```bash
tests/
├── test_login.py
├── test_products.py
├── test_cart.py
├── test_checkout.py
├── test_sorting.py

pages/
├── base_page.py
├── login_page.py
├── products_page.py
├── cart_page.py
└── checkout_page.py
```

---

## ⚙️ Configuration (`pytest.ini`)

```ini
[pytest]
addopts = -v --headed --slowmo=500
base_url = https://www.saucedemo.com
```

### 🔍 Behavior

* `--headed` → runs tests with visible browser (useful for debugging/demo)
* `--slowmo=500` → slows execution for better observation
* `-v` → verbose output

---

## 🧪 Test Coverage

### 🔐 Authentication

* Standard user login
* Locked user validation
* Problem user
* Performance glitch user
* Negative scenarios (invalid credentials, empty fields)

---

### 🛒 Cart

* Add/remove items
* Cart badge validation
* Multiple item handling
* Navigation to cart page
* **Session persistence after page reload**

---

### 🧾 Checkout

* End-to-end checkout flow
* Form validation (negative scenarios)

---

### 🔃 Sorting

* Price: Low → High
* Price: High → Low
* Name: A → Z
* Name: Z → A

(All sorting validations include assertions)

---

## 🚀 Setup Instructions

### 1. Clone repository

```bash
git clone <your-repo-url>
cd playwright-saucedemo-automation
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
```

---

### 3. Activate environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Mac/Linux

```bash
source .venv/bin/activate
```

---

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install pytest pytest-playwright pytest-xdist pytest-html
```

---

### 5. Install Playwright browsers

```bash
playwright install
```

---

## ▶️ Test Execution

### Run tests (default: headed + slow execution)

```bash
pytest
```

---

### Run tests in headless mode (override config)

```bash
pytest -o addopts="" --browser chromium
```

---

### Run tests in parallel

```bash
pytest -n auto -o addopts=""
```

---

### Run parallel + HTML report (recommended)

```bash
pytest -n auto -o addopts="" --html=reports/report.html --self-contained-html
```

---

## 📊 Reporting

* HTML reports are generated in `/reports`
* Includes:

  * Test results (pass/fail)
  * Execution summary
  * Failure details

---

## 🧠 Testing Approach

This framework follows a **risk-based testing strategy**:

| Priority | Area            |
| -------- | --------------- |
| P0       | Login, Checkout |
| P1       | Cart, Sorting   |
| P2       | UI validations  |

Focus areas:

* Business-critical flows
* High-impact user scenarios
* Real-world behavior (e.g., session persistence)

---

## ⚖️ Trade-offs

* API testing not included (not part of assignment)
* Focus on critical flows over exhaustive coverage
* Headed execution by default for clarity (not speed)

---

## 🔮 Future Improvements

* CI/CD integration
* API testing layer
* Cross-browser execution
* Advanced reporting (Allure)

---

## 👤 Author

**Atul Rawat**

---
