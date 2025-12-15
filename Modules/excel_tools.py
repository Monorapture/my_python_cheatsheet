import pandas as pd
import os

def save_excel_auto_width(df, filepath, sheetname='Report'):
    """
    Speichert einen Pandas DataFrame als Excel-Datei und passt 
    die Spaltenbreite automatisch an den Inhalt an.
    
    Args:
        df (pd.DataFrame): Die Daten, die gespeichert werden sollen.
        filepath (str): Der volle Pfad inkl. Dateiname (z.B. 'reports/liste.xlsx').
        sheetname (str): Name des Tabellenblatts (Standard: 'Report').
    """
    
    # Sicherstellen, dass der Ordner existiert (Sicherheits-Check)
    ordner = os.path.dirname(filepath)
    if ordner and not os.path.exists(ordner):
        os.makedirs(ordner)
        print(f"📁 Ordner wurde erstellt: {ordner}")

    print(f"💾 Speichere Excel-Datei: {filepath}...")

    # Der "Engine" Parameter ist wichtig für die Formatierung
    with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
        # 1. Daten schreiben
        df.to_excel(writer, sheet_name=sheetname, index=False)
        
        # 2. Arbeitsblatt für Bearbeitung holen
        worksheet = writer.sheets[sheetname]
        
        # 3. Durch alle Spalten loopen und Breite anpassen
        for column in worksheet.columns:
            max_length = 0
            # Spaltenbuchstabe holen (A, B, C...)
            column_letter = column[0].column_letter 
            
            for cell in column:
                try:
                    # Wir messen die Länge des Inhalts als String
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            
            # Breite setzen (Länge + 2 Puffer für Lesbarkeit)
            adjusted_width = (max_length + 2)
            worksheet.column_dimensions[column_letter].width = adjusted_width

    print(f"✅ Fertig! Datei liegt hier: {filepath}")