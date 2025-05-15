
# Load Balancer Setup in Azure and AWS

This guide explains what a Load Balancer is, and how to set up load balancers in **Azure** and **AWS**, including real-world examples for FastAPI deployments.

---

## ✅ What is a Load Balancer?

A **load balancer** distributes incoming traffic across multiple servers (backend instances) to:

- Improve performance
- Ensure high availability
- Prevent overloading any single server
- Handle failovers

It operates at:
- **Layer 4 Transmission Control Protocol(TCP)** or
- **Layer 7 HyperText Transmission Protocol/ Security (HTTP/HTTPS)** of the OSI model.

---

## ⚙️ Setting Up a Load Balancer

---

### 🔷 Azure Load Balancer

Azure offers:

1. **Azure Load Balancer (L4)** – Basic/Standard (TCP/UDP) User Datagram Protocol
2. **Azure Application Gateway (L7)** – HTTP routing, SSL(Secure Socket Layer) termination, WAF(Web Application Firewall)

#### 📌 Example: Azure Load Balancer Setup (Layer 4)

**Scenario**: Two VMs running FastAPI on port `8000`.

#### Steps:

1. **Create VMs** in the same VNet and subnet.
2. **Install FastAPI** and run the app (`uvicorn`) on port `8000`.
3. **Create Availability Set** or **VMSS** to group VMs.
4. **Create a Load Balancer**:
   - Frontend IP: Public
   - Backend Pool: Add VMs
   - Health Probe: TCP port 8000
   - Load Balancing Rule: Port 80 → Port 8000
5. **Test** the Load Balancer public IP.

---

### 🟠 AWS Load Balancer

AWS offers:

1. Classic Load Balancer (legacy)
2. **Application Load Balancer (ALB)** – L7 (HTTP/HTTPS)
3. **Network Load Balancer (NLB)** – L4 (TCP/UDP)

#### 📌 Example: AWS ALB Setup (Layer 7)

**Scenario**: Two EC2s running FastAPI on port `8000`.

#### Steps:

1. **Launch EC2s** in same VPC.
2. **Install FastAPI** on each:
   ```bash
   pip install fastapi uvicorn
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
3. **Create Target Group**:
   - Protocol: HTTP
   - Port: 8000
   - Register EC2s
4. **Create ALB**:
   - Listener on port 80
   - Target group: above
5. **Security Groups**:
   - Inbound: Allow 80, 8000
   - Outbound: Allow 0.0.0.0/0
6. **Test** using the ALB DNS name.

---

## 🧪 Sample FastAPI App for Load Testing

```python
from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": f"Handled by: {socket.gethostname()}"}
```

Use this to verify that load balancing is working — you’ll see different hostnames as traffic is routed.

---

## 🛡️ Azure vs AWS Comparison

| Feature                  | Azure                      | AWS                            |
|--------------------------|----------------------------|---------------------------------|
| L7 Load Balancer         | Application Gateway        | Application Load Balancer      |
| Autoscaling Integration  | VMSS                       | Auto Scaling Group             |
| Health Probes            | TCP/HTTP                   | HTTP/TCP health checks         |
| SSL Termination          | Application Gateway        | ALB                            |
| WAF Integration          | WAF                        | AWS WAF                        |

---


