# 🛠️ Logistics Data Utils

**A specialized Python library containing reusable modules for Data Engineering & Supply Chain Analytics.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Purpose
This repository adheres to the **DRY Principle (Don't Repeat Yourself)**. 
Instead of rewriting standard functions (like Excel formatting or unit conversions) in every project, they are centralized here for import across the data ecosystem.

## 📂 Modules

| Module | Functionality |
| :--- | :--- |
| **`excel_tools.py`** | Advanced Excel handling. Features **auto-width adjustment** (`Autofit`) for generation of stakeholder-ready reports using `openpyxl`. |
| **`converters.py`** | Domain-specific conversions (e.g., **Pallets to Loading Meters**, Weight conversions). |
| *Planned* | `validators.py` (EAN-13 Checksum validation), `freight_calc.py` (Rate calculation logic). |

## 💻 Usage Example

Simply clone this repo into your project structure or add to `PYTHONPATH`.

```python
from modules import excel_tools, converters

# 1. Create a professional report
excel_tools.save_excel_auto_width(df, "reports/weekly_stock.xlsx")

# 2. Calculate Truck Space
ldm = converters.pallets_to_loading_meters(pallets=33, stackable=False)
print(f"Required Truck Space: {ldm} LDM") # Output: 13.2 LDM (Full Truck)