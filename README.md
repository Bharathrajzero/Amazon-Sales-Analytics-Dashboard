# Amazon Sales Dashboard

A web-based dashboard for analyzing Amazon sales data using Flask, Pandas, and Chart.js. The application provides sales insights through interactive charts and summary metrics.

---

## Screenshots
<img width="1920" height="1079" alt="image" src="https://github.com/user-attachments/assets/3d73618f-e30d-4ac0-9b0d-e0c83953487a" />

---
<img width="1920" height="1079" alt="image" src="https://github.com/user-attachments/assets/6720f3e2-ffe9-486d-bd81-ab8afb8cd834" />

---
<img width="1920" height="1079" alt="image" src="https://github.com/user-attachments/assets/4d4639a1-cabd-41f7-be7b-7502afd6d632" />

---
## Features

- Dashboard summary
  - Total Sales
  - Total Profit
  - Total Orders
  - Average Order Value

- Interactive charts
  - Monthly Sales
  - Sales by Category
  - Profit by Category
  - Top States
  - Top Products
  - Sales by Segment

- Customer analysis
  - Top Customers

---

## Tech Stack

### Backend

- Python
- Flask
- Pandas

### Frontend

- HTML
- CSS
- JavaScript
- Chart.js

---

## Project Structure

```
amazon-sales-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── Amazon_Sales.xlsx
│
├── services/
│   └── analytics.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── dashboard.js

```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/amazon-sales-dashboard.git
```

Move into the project directory

```bash
cd amazon-sales-dashboard
```

Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## Dataset

Place the Excel dataset inside the `data` folder.

```
data/
    Amazon_Sales.xlsx
```

---

## Future Improvements

- Date filters
- Category filters
- Region filters
- Export charts
- Export reports
- Database integration
- User authentication

---
## 📚 Learning & Usage

This project is developed for learning, portfolio, and personal use. Feel free to explore, modify, and enhance it for educational purposes.

---

## 👨‍💻 Author

**Bharath Raj**

GitHub: https://github.com/Bharathrajzero

**Built with ❤️ using Flask, Pandas & Chart.js**

Amazon Sales Analytics Dashboard

---

## 📝 License

This project is licensed under the MIT License © 2026 Bharath Raj.

---
