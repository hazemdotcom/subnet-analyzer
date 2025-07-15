# 🔧 Subnet Analysis and Visualization Tool

This is a DevOps internship project for **Barq Systems**. The tool analyzes and visualizes subnet data using **Python** and **Docker**.

---

## 📁 Files

| File                           | Description                                         |
| ------------------------------ | --------------------------------------------------- |
| `subnet_analyzer.py`           | Main script: subnet analysis + bar chart generation |
| `Dockerfile`                   | Docker setup to containerize the tool               |
| `requirements.txt`             | List of required Python libraries                   |
| `ip_data.xlsx`                 | Input file containing IPs and subnet masks          |
| `subnet_report.csv`            | Output file with detailed subnet info               |
| `advanced_grouped_subnets.csv` | Grouped summary by CIDR                             |
| `network_plot.png`             | Bar chart showing usable hosts per subnet           |
| `report.md`                    | Answers to analysis questions                        |

---

## ⚙️ How to Run Locally

1. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/Scripts/activate      # On Windows
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analyzer and generate the chart**:

   ```bash
   python subnet_analyzer.py
   ```

   Output files will include:

   * `subnet_report.csv`
   * `advanced_grouped_subnets.csv`
   * `network_plot.png`

---

## 🐳 Run with Docker

### 1. **Build Docker image**:

```bash
docker build -t subnet-analyzer .
```

### 2. **Run subnet analysis inside container**:

#### ✅ PowerShell / Git Bash:

```bash
docker run --rm -v ${PWD}:/app subnet-analyzer
```

#### ✅ CMD:

```cmd
docker run --rm -v %cd%:/app subnet-analyzer
```

> This will run everything (including the chart generation) and output files will appear in your **local folder**.

---

## 📊 Output

* **subnet\_report.csv** → Full subnet analysis (CIDR, usable hosts, etc.)
* **advanced\_grouped\_subnets.csv** → Count of IPs per subnet
* **network\_plot.png** → Bar chart visualizing usable hosts per subnet

---

## 🧰 Tech Stack

| Tool            | Purpose                |
| --------------- | ---------------------- |
| **Python 3.10** | Programming language   |
| **Docker**      | Containerization       |
| **pandas**      | Data processing        |
| **ipaddress**   | IP/subnet calculations |
| **matplotlib**  | Visualization          |
| **openpyxl**    | Read Excel file        |

---

## 📌 Notes

* The tool automatically detects if it is running inside Docker.
* Everything runs in one step — no need to run separate scripts.
* Make sure Docker Desktop is running and WSL is properly set up on Windows.

---

## 📧 Contact

For any questions or feedback, please reach out to **Hazem** at hazem.a.m.bakr@gmail.com .
