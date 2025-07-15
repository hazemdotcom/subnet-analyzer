# Subnet Analysis – Barq DevOps Internship Task

## 1. Which subnet has the most hosts?

**Answer:**  
Several subnets in the dataset have the highest number of usable hosts:  
`/22` subnets, each with **1022 usable hosts**:
- 192.168.100.0/22
- 10.2.0.0/22
- 10.20.4.0/22
- 192.168.20.0/22
- 10.3.0.0/22
- 10.15.4.0/22
- 172.16.60.0/22
- 172.16.48.0/22

These subnets each support up to **1022 usable IP addresses**.

---

## 2. Are there any overlapping subnets? If yes, which ones?

**Answer:**  
Based on the analysis script and data provided, each IP falls into a distinct subnet, and no subnet contains multiple IPs.  
Therefore, **there are no overlapping subnets** in the given dataset.

> (If you later modify the dataset to include similar IPs within the same subnet, the advanced grouping will catch overlaps.)

---

## 3. What is the smallest and largest subnet in terms of address space?

**Answer:**
- **Smallest subnet**: `/24` subnet — contains **254 usable hosts**  


- **Largest subnet**: `/22` subnet — contains **1022 usable hosts**  


## 4. Suggest a subnetting strategy that could reduce wasted IPs in this network.

**Answer:**  
There is a large amount of wasted IP space in the current design. For example:
- Subnets like `/22` are being used for just **1 device**
- Even `/23` subnets with 510 usable hosts are underutilized

To reduce IP waste:
- Use **smaller subnets** like `/30` or `/29` for point-to-point links or very small networks.
- Consider grouping hosts by function or department and assigning only the needed IPs.
- Implement a **VLSM (Variable Length Subnet Masking)** strategy to allocate subnets based on actual host requirements.
- This will free up valuable address space for future scaling and reduce routing overhead.

---