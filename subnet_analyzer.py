import pandas as pd #For reading the Excel file and handling tabular data.
import ipaddress #Built-in Python module to analyze IPs and subnets.
from collections import defaultdict #Automatically assigns a default value to a key that does not yet exist.
import os #To check if the script is running in Docker via an environment variable.
from itertools import combinations

#Docker Environment Check
print("🟢 Running inside Docker container" if os.environ.get("DOCKER_ENV") else "🟢 Running locally")

# Load IP data from Excel file
file_path = "ip_data.xlsx"
df = pd.read_excel(file_path)

# Function to Analyze Each Row
def analyze_row(ip, mask):
    try:
        network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
        return {
            "CIDR": str(network.with_prefixlen),
            "Network Address": str(network.network_address),
            "Broadcast Address": str(network.broadcast_address),
            "Usable Hosts": network.num_addresses - 2 if network.num_addresses > 2 else 0
        }
    except Exception as e:
        print(f"⚠️ Error processing {ip}/{mask}: {e}")
        return {
            "CIDR": None,
            "Network Address": None,
            "Broadcast Address": None,
            "Usable Hosts": None
        }

# Analyze each row and create a new DataFrame with results
results = df.apply(lambda row: analyze_row(row['IP Address'], row['Subnet Mask']), axis=1)
result_df = pd.concat([df, pd.DataFrame(results.tolist())], axis=1)

result_df.to_csv("subnet_report.csv", index=False)
print("✅ Subnet Analysis Completed")
print("✅ Report saved to subnet_report.csv")

# Advanced Grouping of Subnets
ip_list = list(df["IP Address"])
subnet_data = []

for index, row in df.iterrows():
    ip = row["IP Address"]
    mask = row["Subnet Mask"]
    try:
        subnet_data.append(ipaddress.IPv4Network(f"{ip}/{mask}", strict=False))
    except:
        continue

subnet_ip_map = defaultdict(set)
for subnet in subnet_data:
    for ip in ip_list:
        try:
            if ipaddress.IPv4Address(ip) in subnet:
                subnet_ip_map[str(subnet)].add(ip)
        except:
            continue

advanced_grouping = pd.DataFrame(
    [{"CIDR": cidr, "IP Count": len(ips)} for cidr, ips in subnet_ip_map.items()]
).sort_values(by="IP Count", ascending=False)

advanced_grouping.to_csv("advanced_grouped_subnets.csv", index=False)
print("✅ Advanced grouped subnets saved to advanced_grouped_subnets.csv")

# Extract unique subnets from the analysis result
unique_cidrs = result_df["CIDR"].dropna().unique()
subnet_objects = [ipaddress.IPv4Network(cidr) for cidr in unique_cidrs]

# Detect overlapping subnet pairs
overlapping_pairs = []
for net1, net2 in combinations(subnet_objects, 2):
    if net1.overlaps(net2):
        overlapping_pairs.append((str(net1), str(net2)))

# Report and optionally save the overlapping subnets
if overlapping_pairs:
    print("🔁 Overlapping Subnets Detected:")
    for a, b in overlapping_pairs:
        print(f" - {a} overlaps with {b}")
    
    # Save to CSV
    pd.DataFrame(overlapping_pairs, columns=["Subnet 1", "Subnet 2"]).to_csv("overlapping_subnets.csv", index=False)
    print("✅ Overlapping subnets saved to overlapping_subnets.csv")
else:
    print("✅ No overlapping subnets found.")
