import pandas as pd


class SalesAnalytics:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = self.load_data()

    def load_data(self):
        df = pd.read_excel(self.file_path)

        df["OrderDate"] = pd.to_datetime(df["OrderDate"])

        numeric_columns = [
            "Quantity",
            "UnitPrice",
            "Discount",
            "Tax",
            "ShippingCost",
            "TotalAmount"
        ]

        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

        # Calculate estimated profit
        df["Profit"] = (
            df["TotalAmount"]
            - df["Tax"]
            - df["ShippingCost"]
        )

        return df

    # -------------------------
    # Dashboard Summary
    # -------------------------

    def get_summary(self):

        total_sales = round(self.df["TotalAmount"].sum(), 2)
        total_profit = round(self.df["Profit"].sum(), 2)
        total_orders = self.df["OrderID"].nunique()
        average_order = round(total_sales / total_orders, 2)

        return {
            "total_sales": total_sales,
            "total_profit": total_profit,
            "total_orders": int(total_orders),
            "average_order_value": average_order
        }

    # -------------------------
    # Monthly Sales
    # -------------------------

    def get_monthly_sales(self):

        monthly = (
            self.df
            .set_index("OrderDate")
            .resample("ME")["TotalAmount"]
            .sum()
        )

        return {
            "labels": monthly.index.strftime("%b %Y").tolist(),
            "values": monthly.values.tolist()
        }

    # -------------------------
    # Category Sales
    # -------------------------

    def get_category_sales(self):

        data = (
            self.df
            .groupby("Category")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
        )

        return {
            "labels": data.index.tolist(),
            "values": data.values.tolist()
        }

    # -------------------------
    # Profit by Category
    # -------------------------

    def get_category_profit(self):

        data = (
            self.df
            .groupby("Category")["Profit"]
            .sum()
            .sort_values(ascending=False)
        )

        return {
            "labels": data.index.tolist(),
            "values": data.values.tolist()
        }

    # -------------------------
    # State Sales
    # -------------------------

    def get_state_sales(self):

        data = (
            self.df
            .groupby("State")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        return {
            "labels": data.index.tolist(),
            "values": data.values.tolist()
        }

    # -------------------------
    # Top Products
    # -------------------------

    def get_top_products(self):

        data = (
            self.df
            .groupby("ProductName")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        return {
            "labels": data.index.tolist(),
            "values": data.values.tolist()
        }

    # -------------------------
    # Top Customers
    # -------------------------

    def get_top_customers(self):

        data = (
            self.df
            .groupby("CustomerName")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        return {
            "labels": data.index.tolist(),
            "values": data.values.tolist()
        }

    # -------------------------
    # Payment Method
    # -------------------------

    def get_segment_sales(self):

        data = (
            self.df
            .groupby("PaymentMethod")["TotalAmount"]
            .sum()
            .sort_values(ascending=False)
        )

        return {
            "labels": data.index.tolist(),
            "values": data.values.tolist()
        }

    # -------------------------

    def get_dashboard_data(self):

        return {
            "summary": self.get_summary(),
            "monthly_sales": self.get_monthly_sales(),
            "category_sales": self.get_category_sales(),
            "category_profit": self.get_category_profit(),
            "state_sales": self.get_state_sales(),
            "top_products": self.get_top_products(),
            "top_customers": self.get_top_customers(),
            "segment_sales": self.get_segment_sales()
        }