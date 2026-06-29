// -----------------------------
// Helper Functions
// -----------------------------

function formatCurrency(value) {
    return new Intl.NumberFormat("en-IN", {
        style: "currency",
        currency: "INR",
        maximumFractionDigits: 2
    }).format(value);
}

async function getData(url) {
    const response = await fetch(url);

    if (!response.ok) {
        throw new Error("Failed to load data");
    }

    return await response.json();
}

// -----------------------------
// Summary Cards
// -----------------------------

async function loadSummary() {

    const data = await getData("/api/summary");

    document.getElementById("total-sales").textContent =
        formatCurrency(data.total_sales);

    document.getElementById("total-profit").textContent =
        formatCurrency(data.total_profit);

    document.getElementById("total-orders").textContent =
        data.total_orders.toLocaleString();

    document.getElementById("average-order").textContent =
        formatCurrency(data.average_order_value);
}

// -----------------------------
// Chart Creator
// -----------------------------

function createChart(id, type, labels, values, label) {

    new Chart(document.getElementById(id), {

        type: type,

        data: {

            labels: labels,

            datasets: [{
                label: label,
                data: values,
                borderWidth: 2,
                borderRadius: 5
            }]
        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {
                    display: type !== "bar"
                }

            }

        }

    });

}

// -----------------------------
// Monthly Sales
// -----------------------------

async function loadMonthlySales() {

    const data = await getData("/api/monthly-sales");

    createChart(
        "monthlyChart",
        "line",
        data.labels,
        data.values,
        "Monthly Sales"
    );

}

// -----------------------------
// Category Sales
// -----------------------------

async function loadCategorySales() {

    const data = await getData("/api/category-sales");

    createChart(
        "categoryChart",
        "pie",
        data.labels,
        data.values,
        "Category Sales"
    );

}

// -----------------------------
// Category Profit
// -----------------------------

async function loadCategoryProfit() {

    const data = await getData("/api/category-profit");

    createChart(
        "profitChart",
        "bar",
        data.labels,
        data.values,
        "Profit"
    );

}

// -----------------------------
// State Sales
// -----------------------------

async function loadStateSales() {

    const data = await getData("/api/state-sales");

    createChart(
        "stateChart",
        "bar",
        data.labels,
        data.values,
        "Sales"
    );

}

// -----------------------------
// Top Products
// -----------------------------

async function loadTopProducts() {

    const data = await getData("/api/top-products");

    createChart(
        "productChart",
        "bar",
        data.labels,
        data.values,
        "Sales"
    );

}

// -----------------------------
// Segment Sales
// -----------------------------

async function loadSegmentSales() {

    const data = await getData("/api/segment-sales");

    createChart(
        "segmentChart",
        "doughnut",
        data.labels,
        data.values,
        "Sales"
    );

}

// -----------------------------
// Top Customers Table
// -----------------------------

async function loadCustomers() {

    const data = await getData("/api/top-customers");

    const table = document.getElementById("customer-table");

    table.innerHTML = "";

    data.labels.forEach((customer, index) => {

        table.innerHTML += `
            <tr>
                <td>${customer}</td>
                <td>${formatCurrency(data.values[index])}</td>
            </tr>
        `;

    });

}

// -----------------------------
// Initialize Dashboard
// -----------------------------

async function initializeDashboard() {

    try {

        await loadSummary();

        await loadMonthlySales();

        await loadCategorySales();

        await loadCategoryProfit();

        await loadStateSales();

        await loadTopProducts();

        await loadSegmentSales();

        await loadCustomers();

    } catch (error) {

        console.error(error);

    }

}

initializeDashboard();