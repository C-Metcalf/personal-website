function showTab(tabId) {
  document.getElementById("income-tab").style.display =
    tabId === "income" ? "block" : "none";
  document.getElementById("expense-tab").style.display =
    tabId === "expense" ? "block" : "none";
}