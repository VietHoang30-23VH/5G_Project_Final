# Building interactive dashboard in order to monitor network traffic in 5G environment 
`This markdown is written by Viet Hoang.`

**I. Introduction** 
- Plotly: graphs, figures: layout, data, trace
https://plotly.com/python/plotly-fundamentals/
- Dash: là một Python Framework, dùng để tạo ra các web dashboard có thể tương tác. Có thể kết hợp giữa Python, HTML và js.
---
**II. Set up environment**

*`Windows`*
1. Create python virtual environment
   
        mkdir 5gdashboard
        cd 5gdashboard
        python -m venv mydash5genv
        .\mydash5genv\Scripts\activate
2. Install needed libraries

        pip install numpy==2.0.0
        pip install pandas==2.2.2
        pip install plotly=5.22.0
        pip install dash==2.17.1
        pip install jupyterlab "ipywidgets>=7.5
        pip install dash dash-core-components dash-html-components jupyter-dash dash-bootstrap-components
        jupyter labextension install jupyterlab-plotly@4.8.2

3. Deploy locally
        
        python main.py

4. Description about output from command line

- Number Packet Captured: Total, total bytes, Lost, Duration
- Network Flow charts: line charts
- Attack Types Distribution: bar charts 
- Initial Traffic: Table "Proto","AckDat","sHops","Seq", "State", "TcpRtt", "dmeansz","offset","sttl", "flgs", "mean", "cause", "stcpb", "dloss","smeansz","loss", "dttl", "sbytes", "bytes"  
- Processed Traffic: Table 'tcp', 'AckDat', 'sHops', 'Seq', 'RST', 'TcpRtt', 'REQ', 'dMeanPktSz','Offset', 'CON', 'FIN', 'sTtl', ' e        ', 'INT', 'Mean', 'Status', 'icmp',
 'SrcTCPBase', ' e d      ', 'sMeanPktSz', 'DstLoss', 'Loss', 'dTtl', 'SrcBytes', 'TotBytes' 
- Time	Source IP	Destination IP	Attack Type	Tool: table 
- Define benign and malicious: figure-factory-table (4.4)
        
        current_time = datetime.datetime.now(pytz.timezone('Etc/GMT-7')).strftime("%H:%M:%S-%d/%m/%Y")
        print(f"Mẫu {idx+1} with [{current_time}]:")
        print(f"  - Label        : {label}")
        print(f"  - Attack Type  : {attack_type}")
        print(f"  - Attack Tool  : {tool}\n")
---
**III. File Structure**

    5G_dashboard/
    ├── app/
    │   ├── __init__.py
    │   ├── assets/  
    │   ├── pages/
    │   │   ├── __init__.py
    │   │   ├── login.py               # Script cho trang login
    │   │   ├── dashboard.py           # Script cho trang dashboard
    │   │   └── home.py                # Trang chính hoặc trang mặc định
    │   └── callbacks/
    │       ├── __init__.py
    │       ├── login_callbacks.py     # Callback cho trang login
    │       └── dashboard_callbacks.py # Callback cho dashboard
    ├── data/
    │   ├── __init__.py
    │   ├── fetch_data.py              # Script lấy dữ liệu mạng
    │   └── processed_data/            # Thư mục lưu dữ liệu đã xử lý (nếu cần)
    ├── main.py                        # File chính để chạy ứng dụng Dash
    ├── Dockerfile                     # File để triển khai bằng Docker
    ├── README.md                      # Hướng dẫn dự án
    └── .gitignore                     # File bỏ qua các tệp không cần thiết

---
`This project is conducted by Viet Hoang and Ba Can.`