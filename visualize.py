import pandas as pd
import matplotlib.pyplot as plt

# Load analyzed data
df = pd.read_csv("subnet_report.csv")

# --- Chart: Usable Hosts per CIDR ---
grouped_hosts = df.groupby("CIDR")["Usable Hosts"].sum().reset_index()
grouped_hosts = grouped_hosts.sort_values(by="Usable Hosts", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(grouped_hosts["CIDR"], grouped_hosts["Usable Hosts"], color="skyblue")
plt.xticks(rotation=45, ha='right')
plt.title("Usable Hosts per Subnet")
plt.xlabel("CIDR")
plt.ylabel("Total Usable Hosts")
plt.tight_layout()
plt.savefig("hosts_per_subnet_chart.png")
print("✅ Chart saved as hosts_per_subnet_chart.png")
