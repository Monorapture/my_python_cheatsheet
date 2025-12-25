"""
MODULE: excel_tools.py
AUTHOR: Kilian Sender
DESCRIPTION: 
    Reusable utility functions for Excel reporting tasks.
    Focuses on UX improvements like auto-adjusting column widths.
"""

import os
import pandas as pd

def save_excel_auto_width(df: pd.DataFrame, filepath: str, sheetname: str = 'Report') -> None:
    """
    Saves a Pandas DataFrame to Excel and automatically adjusts column widths 
    to fit the content (Auto-Fit).

    Args:
        df (pd.DataFrame): The data to save.
        filepath (str): Full output path (e.g., 'reports/output.xlsx').
        sheetname (str, optional): Name of the Excel sheet. Defaults to 'Report'.
    
    Raises:
        PermissionError: If the file is open in Excel while writing.
    """
    
    # 1. Path Safety Check
    folder = os.path.dirname(filepath)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
        print(f"   [INFO] Created directory: {folder}")

    print(f"   [IO] Saving Excel report to: {filepath}...")

    try:
        # 2. Initialize Writer (using openpyxl engine)
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=sheetname, index=False)
            
            # 3. Access the Worksheet Object for Formatting
            worksheet = writer.sheets[sheetname]
            
            # 4. Iterate columns to calculate optimal width
            for column in worksheet.columns:
                max_length = 0
                # Get column letter (A, B, C...) from the header cell
                # openpyxl version safe approach
                column_letter = column[0].column_letter 
                
                for cell in column:
                    try:
                        # Measure length of cell content (converted to string)
                        cell_len = len(str(cell.value))
                        if cell_len > max_length:
                            max_length = cell_len
                    except:
                        pass
                
                # Apply Width: Max Length + Buffer (for filter arrows/margins)
                adjusted_width = (max_length + 2)
                worksheet.column_dimensions[column_letter].width = adjusted_width

        print("   [SUCCESS] File saved with auto-formatting.")

    except PermissionError:
        print(f"   [ERROR] Could not write to {filepath}. Is the file open in Excel?")
        raise
    except Exception as e:
        print(f"   [ERROR] An unexpected error occurred: {e}")
        raise