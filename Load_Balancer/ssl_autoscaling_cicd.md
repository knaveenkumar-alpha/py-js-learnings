
# 🔐 SSL/HTTPS Setup, Autoscaling & CI/CD for FastAPI Apps on Azure and AWS

---

## ✅ SSL/HTTPS Setup

### 🔷 Azure: Using Application Gateway (L7)

1. **Provision Application Gateway**
   - Choose **Frontend IP** (Public).
   - Configure **Listener** on port 443.
   - Add **SSL certificate** (PFX format with password).
   - Backend pool → your VMs or App Service.

2. **Generate PFX Certificate**:
   ```bash
   openssl pkcs12 -export -out cert.pfx -inkey private.key -in cert.crt
   ```

3. **Upload certificate** while configuring listener.

4. **Verify** via HTTPS access to the frontend public IP.

---

### 🟠 AWS: Using Application Load Balancer (ALB)

1. **Get an SSL Certificate**:
   - Use **AWS Certificate Manager (ACM)** to issue a public cert.

2. **Create ALB Listener**:
   - Add HTTPS listener on port 443.
   - Attach SSL certificate from ACM.
   - Forward to target group (your EC2s running FastAPI).

3. **Security Groups**:
   - Allow port 443 inbound.

4. **Test** via ALB DNS: `https://<your-alb>.elb.amazonaws.com`

---

## 📈 Autoscaling Setup

### 🔷 Azure (VM Scale Set + Load Balancer)

1. Create a **VMSS** with your FastAPI VM image.
2. Attach to **Azure Load Balancer**.
3. Configure **Autoscale settings**:
   - Scale out on CPU > 70%
   - Scale in on CPU < 30%

4. Backend health is monitored via probes.

---

### 🟠 AWS (EC2 Auto Scaling + ALB)

1. Create **Launch Template** for EC2 with your app setup.
2. Create **Auto Scaling Group (ASG)**:
   - Attach to **Target Group** (linked to ALB).
   - Define min, max, desired instance count.
   - Add CPU/memory-based scaling policies.

3. ALB balances load across instances in the ASG.

---

## 🚀 CI/CD Pipeline Integration

### GitHub Actions for AWS EC2

```yaml
name: Deploy to AWS

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: SSH into EC2 & deploy
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.HOST }}
          username: ubuntu
          key: ${{ secrets.SSH_KEY }}
          script: |
            cd app
            git pull origin main
            pip install -r requirements.txt
            sudo systemctl restart fastapi-app
```

---

### Azure DevOps Pipeline (Linux VM)

```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
- checkout: self
- task: SSH@0
  inputs:
    sshEndpoint: 'azure-ssh'
    runOptions: 'commands'
    commands: |
      cd app
      git pull origin main
      pip install -r requirements.txt
      sudo systemctl restart fastapi-app
```

---

## 🛠️ Final Tips

- Use **Let's Encrypt** for free SSL (with certbot).
- Monitor CPU/Memory with **CloudWatch** (AWS) or **Azure Monitor**.
- Use **Secrets Manager / Key Vault** for sensitive credentials.
