import pandas as pd
import matplotlib.pyplot as plt

# Load analyzed data
df = pd.read_csv("subnet_report.csv")

# --- Chart 1: Number of IPs per CIDR (Advanced Grouping) ---
advanced_grouping = pd.read_csv("advanced_grouped_subnets.csv")

plt.figure(figsize=(12, 6))
plt.bar(advanced_grouping["CIDR"], advanced_grouping["IP Count"], color="orange")
plt.xticks(rotation=45, ha='right')
plt.title("Number of IPs per Subnet")
plt.xlabel("CIDR")
plt.ylabel("Number of IPs")
plt.tight_layout()
plt.savefig("network_plot.png")
print("✅ Chart saved as network_plot.png")

# --- Chart 2: Usable Hosts per CIDR ---
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
