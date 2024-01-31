// Sample data for demonstration purposes
const data = [
  { month: "January", income: 10000, expenses: 5000, netDifference: 5000 },
  { month: "February", income: 12000, expenses: 6000, netDifference: 6000 },
  // Add more months as needed
];

// Function to update the data table
function updateDataTable() {
  const dataTable = document.getElementById("dataTable");
  dataTable.innerHTML = ""; // Clear existing content

  // Create table headers
  const headerRow = dataTable.insertRow();
  const headers = ["Month", "Income", "Expenses", "Net Difference"];
  headers.forEach((headerText) => {
    const th = document.createElement("th");
    th.textContent = headerText;
    headerRow.appendChild(th);
  });

  // Populate table rows with data
  data.forEach((entry) => {
    const row = dataTable.insertRow();
    Object.values(entry).forEach((value) => {
      const cell = row.insertCell();
      cell.textContent = value;
    });
  });
}

// Function to update summary boxes
function updateSummaryBoxes() {
  const grossIncomeBox = document.getElementById("grossIncomeBox");
  const grossExpensesBox = document.getElementById("grossExpensesBox");
  const netDifferenceBox = document.getElementById("netDifferenceBox");

  // Sample data for demonstration purposes (replace with actual data)
  const summaryData = {
    grossIncome: 10000,
    grossExpenses: 5000,
    netDifference: 5000,
  };

  grossIncomeBox.querySelector("p").textContent = `$${summaryData.grossIncome}`;
  grossExpensesBox.querySelector("p").textContent =
    `$${summaryData.grossExpenses}`;
  netDifferenceBox.querySelector("p").textContent =
    `$${summaryData.netDifference}`;
}

// Function to update the line chart (using a library like Chart.js)
function updateLineChart() {
  // Sample code to create a line chart using Chart.js
  const lineChartCanvas = document.getElementById("lineChart");
  // Replace this code with the actual implementation for your chart library
  // (e.g., Chart.js, D3.js, Plotly)
  // Refer to the documentation of your chosen library for details.
}

// Event listeners for sidebar buttons
document.getElementById("btnIncome").addEventListener("click", () => {
  // Replace this with logic to update data and re-render the page accordingly
  updateSummaryBoxes();
  updateDataTable();
  updateLineChart();
});

document.getElementById("btnExpenses").addEventListener("click", () => {
  // Replace this with logic to update data and re-render the page accordingly
  updateSummaryBoxes();
  updateDataTable();
  updateLineChart();
});

document.getElementById("btnNetDifference").addEventListener("click", () => {
  // Replace this with logic to update data and re-render the page accordingly
  updateSummaryBoxes();
  updateDataTable();
  updateLineChart();
});

// Function to update the line chart using Chart.js
function updateLineChart() {
  // Sample data for demonstration purposes (replace with actual data)
  const months = ["January", "February", "March", "April", "May"];
  const incomeData = [10000, 12000, 15000, 11000, 13000];
  const expensesData = [5000, 6000, 7500, 5500, 6000];
  const netDifferenceData = [5000, 6000, 7500, 5500, 7000];

  const ctx = document.getElementById("lineChart").getContext("2d");

  // Replace this with the actual Chart.js configuration
  const chart = new Chart(ctx, {
    type: "line",
    data: {
      labels: months,
      datasets: [
        {
          label: "Income",
          data: incomeData,
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 2,
          fill: false,
        },
        {
          label: "Expenses",
          data: expensesData,
          borderColor: "rgba(255, 99, 132, 1)",
          borderWidth: 2,
          fill: false,
        },
        {
          label: "Net Difference",
          data: netDifferenceData,
          borderColor: "rgba(54, 162, 235, 1)",
          borderWidth: 2,
          fill: false,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
    },
  });
}

// Initial page load
updateSummaryBoxes();
updateDataTable();
updateLineChart();
