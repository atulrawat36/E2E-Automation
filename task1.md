# 🧪 Test Plan — SauceDemo (Pre-Release Validation)

## 1. Objective

The objective of this test plan is to validate the functional correctness, stability, and user-critical flows of the SauceDemo e-commerce application prior to its first public release.

Given a **2-hour manual testing constraint**, the approach focuses on **risk-based prioritisation**, ensuring that high-impact and high-probability failure areas are tested first.

---

## 2. Scope

### ✅ In Scope

* User authentication (all user types)
* Product listing and sorting
* Add/remove items from cart
* Cart functionality and badge count
* Checkout flow (end-to-end)
* Form validation during checkout
* Session persistence (cart after reload)

### ❌ Out of Scope

* Performance and load testing
* Security testing (e.g., SQL injection)
* Cross-browser compatibility
* Mobile responsiveness
* Backend/database validation

---

## 3. Assumptions

* Application is stable and accessible
* Test data (users/products) is pre-seeded
* No third-party payment gateway involved
* Focus is on frontend behavior

---

## 4. Risk Analysis & Prioritisation

| Risk Area           | Description                                 | Severity | Likelihood | Priority | Rationale             |
| ------------------- | ------------------------------------------- | -------- | ---------- | -------- | --------------------- |
| Authentication      | Login failures block all user activity      | High     | High       | P0       | Entry point to system |
| Checkout Flow       | Failure prevents order completion           | High     | Medium     | P0       | Direct revenue impact |
| Cart Functionality  | Incorrect items/count leads to wrong orders | High     | Medium     | P1       | User trust & accuracy |
| Product Sorting     | Incorrect sorting affects user experience   | Medium   | High       | P1       | High usage frequency  |
| Session Persistence | Cart reset on reload impacts usability      | Medium   | Medium     | P2       | UX degradation        |

---

## 5. Testing Approach (Risk-Based)

### 🔐 Authentication (P0)

* Test all user types:

  * standard_user
  * locked_out_user
  * problem_user
  * performance_glitch_user
* Validate:

  * Successful login
  * Error messages
  * Locked user restriction

---

### 🛒 Checkout Flow (P0)

* End-to-end validation:

  * Add product → Cart → Checkout → Confirmation
* Validate:

  * Order success message
  * Navigation flow
* Negative cases:

  * Empty form submission
  * Invalid inputs

---

### 🧺 Cart Functionality (P1)

* Add/remove items
* Validate cart badge count
* Ensure correct items persist in cart

---

### 🔃 Product Sorting (P1)

* Validate all sorting options:

  * Name (A-Z, Z-A)
  * Price (Low-High, High-Low)
* Ensure correct order is applied

---

### 🔄 Session Persistence (P2)

* Add items → refresh page
* Validate cart state is retained

---

## 6. Detailed Test Cases

### TC_01 — Valid Login

* **Description:** Verify login with valid credentials
* **Steps:**

  1. Navigate to login page
  2. Enter valid username/password
  3. Click login
* **Expected Result:** User is redirected to product page
* **Priority:** P0
* **Type:** Automation Candidate

---

### TC_02 — Locked User Login

* **Description:** Verify locked user cannot log in
* **Steps:**

  1. Enter locked_out_user credentials
  2. Click login
* **Expected Result:** Error message displayed
* **Priority:** P0
* **Type:** Automation Candidate

---

### TC_03 — Add Item to Cart

* **Description:** Verify item can be added to cart
* **Steps:**

  1. Login
  2. Click "Add to Cart"
* **Expected Result:** Cart badge updates correctly
* **Priority:** P1
* **Type:** Automation Candidate

---

### TC_04 — Checkout with Missing Info

* **Description:** Validate form validation
* **Steps:**

  1. Proceed to checkout
  2. Leave fields blank
  3. Submit
* **Expected Result:** Error message shown
* **Priority:** P0
* **Type:** Automation Candidate

---

### TC_05 — Complete Checkout Flow

* **Description:** Verify successful order placement
* **Steps:**

  1. Add item to cart
  2. Proceed to checkout
  3. Enter valid details
  4. Complete order
* **Expected Result:** Order confirmation displayed
* **Priority:** P0
* **Type:** Automation Candidate

---

## 7. Bug Reports (Sample)

### 🐞 Bug 1 — Cart Badge Not Updating

* **Steps:**

  1. Add item to cart
* **Expected:** Cart count increases
* **Actual:** Count remains unchanged
* **Severity:** High
* **Business Impact:** Users may not see selected items → potential order errors

---

### 🐞 Bug 2 — Checkout Allows Blank Submission

* **Steps:**

  1. Go to checkout
  2. Submit empty form
* **Expected:** Validation error
* **Actual:** Form proceeds
* **Severity:** Critical
* **Business Impact:** Invalid orders → data integrity issues

---

### 🐞 Bug 3 — Sorting Not Applied Correctly

* **Steps:**

  1. Select price low-to-high
* **Expected:** Products sorted correctly
* **Actual:** Order incorrect
* **Severity:** Medium
* **Business Impact:** Poor user experience

---

## 8. Top 5 Flows to Automate (With Rationale)

| Flow              | Reason                        |
| ----------------- | ----------------------------- |
| Login (all users) | High frequency, blocks access |
| Add to cart       | Core functionality            |
| Checkout flow     | Revenue-critical              |
| Cart persistence  | UX reliability                |
| Product sorting   | High usage                    |

---

## 9. Conclusion

Given the time constraint, testing prioritises **critical user journeys and revenue-impacting flows**.

The application appears stable in core areas but requires **focused validation on checkout and cart logic** before release.

---
