### **Azure Load Balancer Interview Questions**

1. **What is Azure Load Balancer?**
   - Azure Load Balancer is a Layer 4 (TCP/UDP) load balancer that distributes incoming traffic across multiple virtual machines (VMs) to ensure high availability and reliability.

2. **What are the types of Load Balancers in Azure?**
   - **Public Load Balancer**: Distributes traffic from the internet to VMs.
   - **Internal Load Balancer**: Distributes traffic within a virtual network.

3. **What is the difference between Azure Load Balancer and Application Gateway?**
   - Azure Load Balancer operates at Layer 4 (TCP/UDP), while Application Gateway operates at Layer 7 (HTTP/HTTPS) and provides features like SSL termination and URL-based routing.

4. **How does Azure Load Balancer perform health checks?**
   - It uses health probes to monitor the availability of backend instances. If an instance fails the health check, it is removed from the pool until it becomes healthy again.

5. **What is the difference between Basic and Standard Load Balancer in Azure?**
   - **Basic Load Balancer**: Limited to a single availability set and lacks advanced features.
   - **Standard Load Balancer**: Supports multiple availability zones, higher scalability, and advanced diagnostics.

---

### **AWS Load Balancer Interview Questions**

1. **What is Elastic Load Balancer (ELB) in AWS?**
   - ELB automatically distributes incoming application traffic across multiple targets, such as EC2 instances, containers, and IP addresses.

2. **What are the types of Load Balancers in AWS?**
   - **Application Load Balancer (ALB)**: Operates at Layer 7 (HTTP/HTTPS).
   - **Network Load Balancer (NLB)**: Operates at Layer 4 (TCP/UDP).
   - **Gateway Load Balancer (GLB)**: Operates at Layer 3 for virtual appliances.
   - **Classic Load Balancer (CLB)**: Legacy option supporting both Layer 4 and Layer 7.

3. **What is Cross-Zone Load Balancing in AWS?**
   - Cross-Zone Load Balancing distributes traffic evenly across all registered targets in all enabled availability zones.

4. **How does AWS ELB handle SSL termination?**
   - ELB supports SSL termination by offloading SSL decryption at the load balancer level, reducing the load on backend servers.

5. **What is a Target Group in AWS Load Balancing?**
   - A Target Group is a logical grouping of targets (e.g., EC2 instances) that the load balancer routes traffic to.

---

### **GCP Load Balancer Interview Questions**

1. **What is Load Balancing in Google Cloud?**
   - GCP Load Balancing is a fully distributed, software-defined service that distributes traffic across multiple backend instances to ensure scalability and availability.

2. **What are the types of Load Balancers in GCP?**
   - **HTTP(S) Load Balancer**: Operates at Layer 7 for web traffic.
   - **TCP/UDP Load Balancer**: Operates at Layer 4 for non-HTTP traffic.
   - **Internal Load Balancer**: Distributes traffic within a private network.

3. **What is the difference between Global and Regional Load Balancing in GCP?**
   - **Global Load Balancing**: Distributes traffic across multiple regions.
   - **Regional Load Balancing**: Distributes traffic within a single region.

4. **How does GCP Load Balancer perform health checks?**
   - GCP uses configurable health checks to monitor the health of backend instances. Unhealthy instances are automatically removed from the pool.

5. **What is the role of a Backend Service in GCP Load Balancing?**
   - A Backend Service defines the backend instances, health checks, and session affinity settings for the load balancer.
