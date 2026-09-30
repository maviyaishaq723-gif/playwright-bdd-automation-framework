# PTCL BPOCMS Automation Framework

An end-to-end automated QA testing suite for the **PTCL BPOCMS Web Portal** (`http://bpocms.ptclgroup.com/MultiTenantHDS/`), built using **Python**, **Playwright**, and **Behave (BDD)** framework.

---

## 🏗️ Architecture & Folder Structure

The project follows the standard **Page Object Model (POM)** pattern integrated with **Behavior-Driven Development (BDD)**:

```text
HDS Automation/
│
├── features/                  # BDD Gherkin Scenarios (.feature)
│   ├── order_booking.feature  # Order Booking scenarios
│   ├── reports.feature        # Sales, Cancelled, and Complaints reports scenarios
│   └── steps/                 # Step Definitions (Glue code)
│       ├── order_steps.py
│       └── reports_steps.py
│
├── pages/                     # Page Object Model (POM) Locators & Actions
│   ├── login_page.py
│   ├── active_order_page.py
│   ├── book_order_page.py
│   ├── complaint_page.py
│   ├── locations_page.py
│   ├── menu_management_page.py
│   ├── order_detail_page.py
│   ├── payment_modes_page.py
│   ├── reports_page.py
│   ├── riders_page.py
│   └── user_management_page.py
│
├── reports/                   # Test Execution HTML Output
│   └── report.html
│
└── README.md                  # Project Documentation & Execution Guide