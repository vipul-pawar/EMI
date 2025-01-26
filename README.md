# EMI Calculator

## Overview

The **EMI Calculator** is a web-based application built with Django. It helps users calculate their Equated Monthly Installments (EMI) for loans. By entering the loan amount, interest rate, and tenure, users can quickly determine their monthly payments and get a detailed breakdown of the total interest and principal amounts.

## Features

- User-friendly input form for loan details.
- Real-time calculation of EMIs.
- Displays a detailed breakdown of:
  - Monthly EMI
  - Total interest payable
  - Total amount payable (Principal + Interest)
- Interactive graph to visually represent the contribution of principal and interest over time.
- Responsive design for seamless usage on all devices.

## Prerequisites

Before running the project, ensure you have the following installed on your machine:

- Python 3.7 or higher
- Django 4.x or higher
- pip (Python package installer)
- Virtualenv (optional but recommended)

## Installation

Follow these steps to set up the EMI Calculator locally:


Follow these steps to set up the EMI Calculator locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vipul-pawar/EMI.git
   cd emi

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv .venv
   venv\Scripts\activate   

3. **Install Required Dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Apply Database Migrations**:
   ```bash
   python manage.py migrate
   
5. **Run the Development Server**:
    ```bash
    python manage.py runserver

Access the Application: Open your web browser and navigate to http://127.0.0.1:8000/.
