from flask import Flask, jsonify, render_template
from services.analytics import SalesAnalytics
import os

app = Flask(__name__)

# Dataset location
DATA_FILE = os.path.join("data", "amazon.xlsx")

# Load analytics service
analytics = SalesAnalytics(DATA_FILE)


@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Dashboard Summary
# -----------------------------
@app.route("/api/summary")
def summary():
    return jsonify(analytics.get_summary())


# -----------------------------
# Monthly Sales
# -----------------------------
@app.route("/api/monthly-sales")
def monthly_sales():
    return jsonify(analytics.get_monthly_sales())


# -----------------------------
# Sales by Category
# -----------------------------
@app.route("/api/category-sales")
def category_sales():
    return jsonify(analytics.get_category_sales())


# -----------------------------
# Profit by Category
# -----------------------------
@app.route("/api/category-profit")
def category_profit():
    return jsonify(analytics.get_category_profit())


# -----------------------------
# State Sales
# -----------------------------
@app.route("/api/state-sales")
def state_sales():
    return jsonify(analytics.get_state_sales())


# -----------------------------
# Top Products
# -----------------------------
@app.route("/api/top-products")
def top_products():
    return jsonify(analytics.get_top_products())


# -----------------------------
# Top Customers
# -----------------------------
@app.route("/api/top-customers")
def top_customers():
    return jsonify(analytics.get_top_customers())


# -----------------------------
# Segment Sales
# -----------------------------
@app.route("/api/segment-sales")
def segment_sales():
    return jsonify(analytics.get_segment_sales())


# -----------------------------
# Complete Dashboard
# -----------------------------
@app.route("/api/dashboard")
def dashboard():
    return jsonify(analytics.get_dashboard_data())


if __name__ == "__main__":
    app.run(debug=True)