"""
MODULE: converters.py
DESCRIPTION: 
    Standard unit conversions for logistics and supply chain calculations.
"""

def pallets_to_loading_meters(pallets: int, stackable: bool = False) -> float:
    """
    Calculates required loading meters (Lademeter) for a standard Euro Truck.
    Assumption: Euro Pallet (0.8m x 1.2m).
    
    Args:
        pallets (int): Number of pallets.
        stackable (bool): If True, assumes double stacking is possible.
    
    Returns:
        float: Required loading meters.
    """
    if stackable:
        # If stackable, we can fit twice as many pallets per meter
        pallets = pallets / 2
        
    # Standard formula: 0.4 loading meters per Euro Pallet (non-stacked)
    # (Since 2 pallets fit side-by-side in 2.4m width, and they are 1.2m long -> 0.4 per pallet is mostly used for calculation base)
    # Correct generic formula: (Pallets * 0.4)
    ldm = pallets * 0.4
    return round(ldm, 2)

def kg_to_metric_tons(kg: float) -> float:
    """Simple conversion: Kilograms to Tons."""
    return kg / 1000.0