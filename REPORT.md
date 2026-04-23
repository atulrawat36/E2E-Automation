# Test Execution Report — SauceDemo

## Overview

This report summarizes the execution of automated UI and API test cases, along with defects identified through exploratory (manual) testing.

The objective was to validate core user journeys and assess the stability of the application.

---

## Scope

### Automated Testing

* Login functionality
* Product listing and sorting
* Cart operations
* Checkout flow
* API endpoints (`/posts`)

### Manual Testing (Exploratory)

* Behavior across different user types
* Edge cases not covered in automation
* UI and usability observations

---

## Execution Summary

| Area      | Tests Executed | Passed | Failed |
| --------- | -------------- | ------ | ------ |
| UI Tests  | 30+            | All    | 0      |
| API Tests | 7              | All    | 0      |

All automated test cases passed successfully.

---

## Key Validations

### UI

* Login functionality works for standard users
* Proper error messages are displayed for invalid inputs
* Products are displayed with correct details
* Sorting works as expected
* Cart updates correctly when items are added/removed
* Cart state persists after page reload
* Checkout flow completes successfully

---

### API

* GET, POST, PUT, DELETE operations behave as expected
* Response structure and data types validated
* Negative scenarios handled correctly

---

## Defects Identified (Manual Testing)

The following issues were identified during exploratory testing and are **not covered in the automation suite**.

---

### 🔴 Bug 1 — Image mismatch for `problem_user`

* **Module:** Products
* **Severity:** High
* **Priority:** P1

**Steps to Reproduce:**

1. Login with `problem_user`
2. Observe product images

**Expected:**
Each product should display its correct image

**Actual:**
Multiple products display incorrect or identical images

**Impact:**
Misleading product representation, affecting user trust

---

### 🔴 Bug 2 — Sorting inconsistency with `problem_user`

* **Module:** Products
* **Severity:** High
* **Priority:** P1

**Steps to Reproduce:**

1. Login with `problem_user`
2. Apply sorting (e.g., price low → high)

**Expected:**
Products should be sorted correctly

**Actual:**
Sorting does not reflect correct order

**Impact:**
Incorrect product ordering affecting product discovery

---

### 🟡 Bug 3 — UI layout inconsistencies

* **Module:** Product / Cart pages
* **Severity:** Low
* **Priority:** P2

**Observation:**
Minor alignment and spacing inconsistencies across UI elements

**Impact:**
Affects visual quality but not functionality

---

### 🟡 Bug 4 — Performance delay with `performance_glitch_user`

* **Module:** Login / Product page
* **Severity:** Medium
* **Priority:** P2

**Steps to Reproduce:**

1. Login using `performance_glitch_user`

**Expected:**
Page loads within acceptable time

**Actual:**
Noticeable delay in product loading

**Impact:**
Degraded user experience

---

## Priority Definition

| Priority | Description                                 |
| -------- | ------------------------------------------- |
| P0       | Critical issue blocking core functionality  |
| P1       | High impact issue affecting user experience |
| P2       | Minor issue with low to moderate impact     |

---

## Observations

* Core flows are stable for standard users
* Issues are primarily user-type-specific
* No critical defects affecting primary workflows

---

## Risks & Limitations

* Cross-browser testing not performed
* Performance and load testing not included
* Security testing out of scope
* Limited edge case coverage

---

## Conclusion

The application is stable for core functionality, particularly for standard users.

However, inconsistencies observed for specific user types and minor UI issues should be addressed to improve overall user experience and reliability.

---
