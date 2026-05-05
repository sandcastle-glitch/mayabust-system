# MAYABUST
Mayabust is a smart agricultural solution designed to protect crops from bird-related damage using a Raspberry Pi-based detection and deterrence system. This repository contains the web-based monitoring dashboard.

# 🚀 Features
Real-time Dashboard: Monitor system status and historical data.
Data Logs: Detailed records of every sensor activation (PIR, Ultrasonic, etc.).
Automated Deterrence: Integration with buzzers and LED strobe lights.
SQLite Integration: Localized data storage for reliable logging in remote areas.

# 🛠 Tech Stack
Backend: Python (Flask)
Database: SQLite3
Frontend: HTML5, CSS3 (Modern Green UI)
Hardware: Raspberry Pi 4/5, PIR Motion Sensors, Ultrasonic Sensors.


# ⚙️ Installation & Setup
1. Clone the repository:
  **git clone https://github.com/yourusername/Mayabust.git
  cd Mayabust**

2. Set up the Virtual Environment:
   **python -m venv .venv
    source .venv/Scripts/activate  # Windows**

3. Install Dependencies: **pip install flask**

4. Initialize the Database: **python init_db.py**

5. Run the dashboard: **python app.py**


Access the dashboard at http://127.0.0.1:5000
