# Network Subnet Analysis Report

## 1. Subnet with the Most Hosts
- **Subnet Mask:** `255.255.252.0` (`/22`)
- **Usable Hosts:** 1022

## 2. Overlapping Subnets
- **Findings:** No overlapping subnets detected.
- **Reason:** All subnets belong to different private IP ranges.

## 3. Smallest and Largest Subnets
| Metric      | Subnet Mask       | Prefix | Usable Hosts |
|-------------|-------------------|--------|--------------|
| **Smallest** | `255.255.255.0`   | `/24`  | 254          |
| **Largest**  | `255.255.252.0`   | `/22`  | 1022         |

## 4. Subnetting Strategy to Reduce Wasted IPs
### Recommended Approach: Variable-Length Subnet Masking (VLSM)
1. **Right-size subnets** based on actual host requirements:
   - Use `/25` (126 hosts) for medium-sized networks
   - Use `/26` (62 hosts) for smaller networks
2. **Consolidate contiguous subnets**:
   - Merge two `/24` subnets into one `/23` (510 hosts) if possible
3. **Implementation Example**:
   - Replace multiple `/24` subnets (e.g., `192.168.1.0/24`, `192.168.2.0/24`) with a single `/23` (`192.168.1.0/23`)

### Benefits:
- Minimizes unused IP addresses
- Improves address space utilization
- Maintains network segmentation requirements
