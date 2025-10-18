import matplotlib.pyplot as plt

def timekey_to_quarter(timekey, base_timekey=174, base_year=2023, base_quarter=2):
    """Convert timekey to quarter label"""
    quarters_diff = timekey - base_timekey
    total_quarters = (base_year - 1970) * 4 + (base_quarter - 1) + quarters_diff
    year = 1970 + total_quarters // 4
    quarter = (total_quarters % 4) + 1
    return f"{year}Q{quarter}"



def plot_bt(bt, deposits_col, pred_col, 
            title='Backtesting of 1-year Forecasted Deposits'):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(bt['quarter'], bt[deposits_col], 
            marker='o', linewidth=2, markersize=8, label='Actual Deposits')
    ax.plot(bt['quarter'], bt[pred_col], 
            marker='s', linewidth=2, markersize=8, linestyle='--', label='Predicted Deposits')
    
    ax.set_ylim(bottom=10_000_000, top=19_000_000)
    ax.set_xlabel('Quarter', fontsize=12)
    ax.set_ylabel('Domestic Office Deposits (Avg)', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    return fig

