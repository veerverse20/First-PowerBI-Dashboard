```markdown
# 📊 First Dashboard - Power BI Sales Analytics

An end-to-end Power BI analytics project designed to analyze regional sales performance, product revenue, and operational demand trends. 

---

## 📌 Project Overview

This dashboard provides executive leadership and sales managers with clear insights into total revenue generated, regional performance distribution, product category demand, and daily sales consistency. Built with a structured data model, it helps identify high-performing categories and track revenue trends.

![Dashboard Preview](assets/dashboard_preview.png)


---


## 📊 Key Business Metrics & Insights

* **Total Revenue Generated:** **$545.23K** achieved in gross sales across key operational regions.
* **Top Revenue Region:** **East Region** generated the highest proportion of total sales (~$266K), followed by the South region.
* **Product Demand Breakdown:** Laptops and Smartphones drive the highest overall revenue contribution, while Mice and Monitors lead in volume sales.
* **Sales Trends:** Daily tracking shows steady sales velocity across 30-day windows, revealing clear mid-month demand spikes.

---

## 🏗 Data Architecture & Modeling

The project follows a standard **Star Schema** layout to optimize DAX calculations, ensure analytical scalability, and maintain clean data governance:

| Table Name | Type | Description |
| :--- | :--- | :--- |
| `Fact_Sales` | **Fact Table** | Contains core transactional data including sales amounts, order quantities, and foreign keys. |
| `Dim_Customers` | **Dimension** | Stores customer attributes, demographic details, and location identifiers. |
| `Dim_Products` | **Dimension** | Contains item details, product categories, unit prices, and specifications. |
| `Dim_Date` | **Dimension** | Dedicated calendar table supporting time-intelligence functions (YTD, MoM). |

---

## 📐 Key Calculations & DAX Measures

All business logic calculations are organized within a dedicated `_Measures` repository table for seamless maintenance:

```dax
// 1. Total Sales Calculation
Total Sales = SUM(Fact_Sales[TotalSales])

// 2. Total Quantity Sold
Total Quantity = SUM(Fact_Sales[Quantity])

// 3. Average Order Value (AOV)
Average Order Value = DIVIDE([Total Sales], COUNT(Fact_Sales[SalesID]), 0)

// 4. Year-to-Date (YTD) Revenue
Sales YTD = TOTALYTD([Total Sales], Dim_Date[Date])

```

---

## 📁 Repository Structure

```text
├── assets/
│   └── dashboard_preview.png    # High-resolution screenshot of the report
├── data/
│   └── raw_sales_dataset.xlsx   # Sample dataset used for building the model
├── First Dashboard.pbip          # Power BI Developer Project file
├── First Dashboard.pdf           # Standalone PDF export for quick viewing
└── README.md                    # Project documentation

```

---

## 🚀 Getting Started

1. **Clone this repository:**
```bash
git clone [https://github.com/your-username/First-Dashboard.git](https://github.com/your-username/First-Dashboard.git)

```


2. **Open in Power BI Desktop:**
* Open `First Dashboard.pbip` (Power BI Desktop version 2023+ required).


3. **Explore interactive reporting:**
* Interact with visuals, apply dynamic slicers, and explore drill-through capabilities.



---

## 💡 Future Enhancements

* Integrate a dynamic Currency Switcher (USD, EUR, INR) using DAX parameters.
* Add dynamic drill-through pages for deep customer segmentation analytics.
* Set up Row-Level Security (RLS) based on Regional Sales Managers.

```

```
