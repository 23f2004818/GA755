# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style for professional look
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic seasonal revenue data
np.random.seed(42)
months = pd.date_range(start="2023-01", periods=12, freq="M")
revenue = (20000 + 5000 * np.sin(np.linspace(0, 2 * np.pi, 12)) +
           np.random.normal(0, 1000, 12))  # seasonal + noise

data = pd.DataFrame({
    "Month": months,
    "Revenue": revenue
})

# Create the lineplot
plt.figure(figsize=(8, 8))  # 8x8 inches * 64 dpi = 512x512 pixels
sns.lineplot(data=data, x="Month", y="Revenue", marker="o", color="royalblue")

# Customize chart
plt.title("Seasonal Revenue Trends (Synthetic Data)", fontsize=16, weight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart with exact 512x512 resolution
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
