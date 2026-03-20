#  Midstalker Analyzer - Complete Code Documentation

> **"Every packet hides a story. I give you the tools to decode it."**

**Developer:** err0rgod (Nirbhay Katiyar)  
**Version:** 2.0  
**Type:** PCAP Analysis Tool for Cybersecurity

---

##  **Project Structure Overview**

```
Midstalker analyzer/
├── app.py                    # Main Streamlit web application (1391 lines)
├── main.py                   # Test/development script not in use right now (140 lines)
├── requirements.txt          # Python dependencies (11 packages)
├── README.md                 # Project documentation (216 lines)
├── JupyterNotebook.ipynb     # Analysis notebook only for test abhi to koi kaam nhi hai uska (442 lines)
├── sample.pcap              # Sample PCAP file for testing
├── ftp-data.pcap            # FTP traffic sample
├── ftp3.pcap                # FTP session sample
└── utils/                   # Core processing modules
    ├── pcap_decode.py       # Packet decoder engine (237 lines)
    ├── data_extract.py      # Protocol data extraction (593 lines)
    ├── except_info.py       # Security threat detection (147 lines)
    ├── file_extract.py      # File reconstruction (200 lines)
    ├── flow_analyzer.py     # Traffic flow analysis (160 lines)
    ├── proto_analyzer.py    # Protocol statistics (117 lines)
    ├── pcap_filter.py       # Packet filtering (116 lines)
    ├── ipmap_tools.py       # Geographic mapping (57 lines)
    ├── packet_fake.py       # Packet generation (18 lines)
    ├── upload_tools.py      # File upload utilities (17 lines)
    ├── __init__.py          # Package initialization
    ├── GeoIP/               # Geographic IP database
    ├── protocol/            # Protocol definition files
    └── warning/             # Security warning patterns
```

---

## ️ **Core Files Documentation**

### **1. app.py** (Main Application)
**Purpose:** Streamlit web interface for PCAP analysis  
**Size:** 55KB, 1391 lines  
**Key Functions:**
- `main()`: Application entry point with navigation menu
- `page_file_upload()`: File upload and validation
- `RawDataView()`: Packet data display and filtering
- `Intro()`: Project introduction and developer info
- `DataPacketLengthStatistics()`: Packet size visualization
- `CommonProtocolStatistics()`: Protocol distribution charts
- `HTTP_HTTPSAccessStatistics()`: Web traffic analysis
- `DNSAccessStatistics()`: DNS query analysis
- `TimeFlowChart()`: Time-based traffic visualization
- `DataInOutStatistics()`: Traffic direction analysis
- `DrawFoliumMap()`: Geographic IP mapping

**Features:**
- 5-tab navigation (Home, Upload, Raw Data, Analysis, Geoplots)
- Interactive charts (Plotly, ECharts, Folium)
- Advanced filtering capabilities
- Real-time data processing
- Session state management

### **2. main.py** (Test Script)
**Purpose:** Development and testing utility  
**Size:** 4.4KB, 140 lines  
**Key Functions:**
- `get_all_pcap()`: Extract all packet data
- `get_filter_pcap()`: Filter packets by criteria
- `proto_filter()`: Protocol-based filtering
- `showdata_from_id()`: Display packet details
- `datashow()`: Generate packet reports

**Usage:** Command-line testing of core functionality

### **3. utils/pcap_decode.py** (Packet Decoder)
**Purpose:** Core packet parsing engine  
**Size:** 8.8KB, 237 lines  
**Key Functions:**
- `__init__()`: Load protocol definition files
- `ether_decode()`: Parse Ethernet layer
- `ip_decode()`: Parse IP layer
- `tcp_decode()`: Parse TCP layer
- `udp_decode()`: Parse UDP layer

**Protocol Support:**
- Ethernet, IP, IPv6, TCP, UDP, ARP, ICMP, DNS, HTTP, HTTPS
- Configuration files: ETHER, IP, PORT, TCP, UDP

### **4. utils/data_extract.py** (Data Extraction)
**Purpose:** Extract and reconstruct application data  
**Size:** 25KB, 593 lines  
**Key Functions:**
- `web_data()`: HTTP traffic extraction
- `mail_data()`: Email protocol data (POP3, IMAP, SMTP)
- `telnet_ftp_data()`: Telnet/FTP session data
- `dns_data()`: DNS query extraction
- `get_host_ip()`: Identify primary host IP

**Supported Protocols:**
- HTTP (ports 80, 8080)
- POP3 (port 110), IMAP (port 143), SMTP (port 25)
- FTP (port 21), Telnet (port 23)
- DNS (port 53)

### **5. utils/except_info.py** (Security Analysis)
**Purpose:** Threat detection and security warnings  
**Size:** 6.2KB, 147 lines  
**Key Functions:**
- `port_warning()`: Suspicious port detection
- `web_warning()`: Web attack pattern detection
- `ftp_warning()`: FTP brute force detection
- `telnet_warning()`: Telnet attack detection

**Threat Detection:**
- SQL injection, XSS, OS command injection
- Brute force attacks (HTTP, FTP, Telnet)
- Suspicious port activity
- Malware traffic patterns

### **6. utils/file_extract.py** (File Reconstruction)
**Purpose:** Extract and save files from network traffic  
**Size:** 8.3KB, 200 lines  
**Key Functions:**
- `web_file()`: Extract files from HTTP traffic
- `ftp_file()`: Extract files from FTP sessions
- `mail_file()`: Extract email attachments

**File Types:**
- HTTP downloads/uploads
- FTP file transfers
- Email attachments
- Binary and text files

### **7. utils/flow_analyzer.py** (Traffic Analysis)
**Purpose:** Network traffic flow analysis  
**Size:** 5.6KB, 160 lines  
**Key Functions:**
- `time_flow()`: Time-based traffic patterns
- `get_host_ip()`: Identify primary host
- `data_flow()`: Inbound/outbound traffic analysis
- `data_in_out_ip()`: IP-based traffic statistics
- `proto_flow()`: Protocol-based flow analysis

**Analysis Types:**
- Time-series traffic visualization
- Traffic direction analysis
- IP-based traffic statistics
- Protocol flow distribution

### **8. utils/proto_analyzer.py** (Protocol Statistics)
**Purpose:** Protocol distribution and statistics  
**Size:** 3.7KB, 117 lines  
**Key Functions:**
- `pcap_len_statistic()`: Packet size distribution
- `common_proto_statistic()`: Protocol frequency analysis
- `most_proto_statistic()`: Top protocol identification
- `http_statistic()`: HTTP/HTTPS traffic analysis
- `dns_statistic()`: DNS query analysis

**Statistics:**
- Packet length distribution (0-300, 301-600, etc.)
- Protocol frequency (IP, TCP, UDP, HTTP, etc.)
- Top 10 most common protocols
- HTTP/HTTPS access patterns

### **9. utils/pcap_filter.py** (Packet Filtering)
**Purpose:** Advanced packet filtering capabilities  
**Size:** 3.5KB, 116 lines  
**Key Functions:**
- `get_all_pcap()`: Extract all packets
- `get_filter_pcap()`: Filter by specific criteria
- `proto_filter()`: Protocol-based filtering
- `showdata_from_id()`: Display packet details

**Filter Options:**
- Protocol type (TCP, UDP, HTTP, etc.)
- Source IP address
- Destination IP address
- Packet length ranges

### **10. utils/ipmap_tools.py** (Geographic Mapping)
**Purpose:** IP geolocation and mapping  
**Size:** 1.7KB, 57 lines  
**Key Functions:**
- `get_geo()`: IP to location conversion
- `get_ipmap()`: Generate geographic data
- Geographic visualization support

**Features:**
- MaxMind GeoLite2 database integration
- IP to city/country mapping
- Geographic traffic visualization

### **11. utils/packet_fake.py** (Packet Generation)
**Purpose:** Generate test packets  
**Size:** 752B, 18 lines  
**Key Functions:**
- Packet creation for testing
- Network simulation support

### **12. utils/upload_tools.py** (File Upload)
**Purpose:** File upload utilities  
**Size:** 450B, 17 lines  
**Key Functions:**
- File validation
- Upload processing

---

##  **Data Flow Architecture**

```
PCAP File Upload
       
   pcap_decode.py (Packet Parsing)
       
   data_extract.py (Data Extraction)
       
   proto_analyzer.py (Statistics)
       
   flow_analyzer.py (Traffic Analysis)
       
   except_info.py (Security Analysis)
       
   ipmap_tools.py (Geographic Mapping)
       
   app.py (Visualization & UI)
```

---

##  **Dependencies** (requirements.txt)

| Package | Purpose |
|---------|---------|
| `streamlit` | Web application framework |
| `numpy` | Numerical computations |
| `pandas` | Data manipulation |
| `plost` | Plotting library |
| `streamlit_folium` | Geographic mapping |
| `scapy` | Packet manipulation |
| `streamlit_echarts` | Interactive charts |
| `geoip2` | IP geolocation |
| `streamlit_option_menu` | Navigation menu |
| `plotly` | Data visualization |
| `folium` | Map visualization |

---

##  **Key Features Summary**

### **Core Capabilities**
-  Multi-protocol packet analysis
-  Real-time data processing
-  Advanced filtering system
-  Security threat detection
-  Geographic IP mapping
-  File reconstruction
-  Interactive visualizations

### **Protocol Support**
-  Ethernet, IP, IPv6
-  TCP, UDP, ARP, ICMP
-  DNS, HTTP, HTTPS
-  FTP, Telnet, SMTP, POP3, IMAP

### **Security Features**
-  Attack pattern detection
-  Brute force identification
-  Suspicious port warnings
-  Malware traffic analysis

### **Visualization**
-  Interactive charts (Plotly, ECharts)
-  Geographic maps (Folium)
-  Statistical summaries
-  Real-time dashboards

---

##  **Usage Workflow**

1. **Upload PCAP**  `app.py` (page_file_upload)
2. **Parse Packets**  `pcap_decode.py` (ether_decode)
3. **Extract Data**  `data_extract.py` (web_data, mail_data)
4. **Analyze Traffic**  `flow_analyzer.py` (time_flow, data_flow)
5. **Generate Stats**  `proto_analyzer.py` (common_proto_statistic)
6. **Detect Threats**  `except_info.py` (web_warning, port_warning)
7. **Map Locations**  `ipmap_tools.py` (get_ipmap)
8. **Visualize Results**  `app.py` (various chart functions)

---

## ️ **Security & Privacy**

- **Local Processing**: All analysis done locally
- **No Data Transmission**: PCAP files not sent to external servers
- **Open Source**: Transparent code for security review
- **Educational Use**: Designed for legitimate cybersecurity research

---

##  **Performance Metrics**

- **File Size Support**: Up to several GB PCAP files
- **Processing Speed**: Real-time packet analysis
- **Memory Usage**: Efficient streaming processing
- **Concurrent Users**: Single-user web application

---

##  **Development Status**

- **Version**: 2.0 (Enhanced by err0rgod)
- **Status**: Production Ready
- **Maintenance**: Active development
- **Documentation**: Comprehensive (English)

---

**Built with ️ by err0rgod for the cybersecurity community**

*"In the world of cybersecurity, knowledge is power, and packets are the truth."*
