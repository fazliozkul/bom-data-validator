import pandas as pd

def validate_bom(file_path):
    """
    Validates the Bill of Materials (BOM) for missing values and cost errors.
    """
    try:
        # Load data (Assuming Excel format)
        df = pd.read_excel(file_path)
        
        # Check 1: Missing Descriptions
        missing_desc = df[df['Description'].isnull()]
        if not missing_desc.empty:
            print(f"⚠️ Warning: {len(missing_desc)} items missing descriptions.")
        
        # Check 2: Negative Costs
        invalid_costs = df[df['Unit_Cost'] < 0]
        if not invalid_costs.empty:
            print(f"❌ Error: {len(invalid_costs)} items have negative cost values.")
        
        # Check 3: Stock Levels
        low_stock = df[df['Stock_Qty'] < 10]
        print(f"ℹ️ Info: {len(low_stock)} items are below safety stock levels.")
        
        print("Validation Complete.")
        
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Create dummy data for demonstration
    data = {
        'Part_Number': ['A101', 'B202', 'C303'],
        'Description': ['Resistor', None, 'Capacitor'],
        'Unit_Cost': [0.5, -1.2, 0.8],
        'Stock_Qty': [100, 5, 50]
    }
    df_dummy = pd.DataFrame(data)
    df_dummy.to_excel("dummy_bom.xlsx", index=False)
    
    # Run Validation
    validate_bom("dummy_bom.xlsx")
