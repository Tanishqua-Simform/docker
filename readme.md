# Docker

Now that we have a good grasp over Python web frameworks, it is time to understand in depth about Docker, a containerization platform.

## **🧱 Section 1: Core Concepts & Architecture**

### **1.1 Containers vs Virtual Machines (VMs)**

#### 🔹 What is a **Container**?

- A lightweight, standalone, executable package of software that includes everything needed to run it: **code + runtime + system tools + libraries + settings**.
- **Shares the host OS kernel** (Linux or Windows) but isolates the app environment using **namespaces** and **cgroups**.

#### 🔹 What is a **Virtual Machine (VM)?**

- Emulates an entire computer with its **own OS kernel** running on top of a hypervisor (like VirtualBox, VMware, or KVM).
- Heavier, slower to boot, and consumes more resources than containers.

#### 🔸 Key Differences:

| Feature        | Container             | Virtual Machine                       |
| -------------- | --------------------- | ------------------------------------- |
| OS             | Shares host OS kernel | Has its own OS kernel                 |
| Boot Time      | Seconds               | Minutes                               |
| Performance    | Near-native           | Slower due to virtualization overhead |
| Resource Usage | Lightweight (MBs)     | Heavy (GBs)                           |
| Isolation      | Process-level         | Full machine-level                    |
| Portability    | High                  | Medium                                |

#### 📌 Use Case:

- **Containers:** Microservices, CI/CD pipelines, scaling apps quickly.
- **VMs:** When you need **stronger isolation**, **different OS types**, or **legacy apps**.

### **1.2 Docker Engine & CLI Internals**

#### 🧠 Docker Architecture

```plaintext
                +---------------------+
                |     Docker CLI      |
                +---------------------+
                         |
                         v
                +---------------------+
                |   Docker REST API   |
                +---------------------+
                         |
                         v
                +---------------------+
                |    Docker Engine    |
                +---------------------+
                         |
     ----------------------------------------------
     |              |               |             |
 Containers      Images        Networks       Volumes
```

#### 📦 Components:

| Component                     | Role                                                                                    |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| **Docker CLI**                | The command-line tool (`docker`) used to interact with the Docker daemon.               |
| **Docker Daemon (`dockerd`)** | Runs in the background. Manages images, containers, volumes, networks.                  |
| **Docker REST API**           | Interface between CLI and Docker Engine (also used by other tools like Docker Compose). |

### **1.3 Docker Images, Containers, and OCI Standards**

#### 🖼️ Image

- A **read-only** template used to create containers.
- Built using a **Dockerfile** (a script with instructions).

#### 📦 Container

- A **running instance** of an image.
- Think: _Image = Blueprint_, _Container = House built from it_.

#### 🔖 Layers

- Docker images are made of **layers** (one per Dockerfile instruction). Layers are cached and reused.

#### 🔐 OCI (Open Container Initiative)

- Docker images & containers follow **OCI specifications**:

  - 📁 **Image Spec:** Format for container images.
  - 🧰 **Runtime Spec:** How to run those images (runc, containerd).

## **🧰 Section 2: Installation & Environment Setup**

### **2.1 Install Docker on Linux/macOS/Windows**

#### ✅ Requirements

| OS          | Requirements                                  |
| ----------- | --------------------------------------------- |
| **Linux**   | Kernel 3.10+ (Most distros are fine)          |
| **macOS**   | macOS 10.15+ (Docker Desktop)                 |
| **Windows** | Windows 10/11 (Pro for WSL2 + Docker Desktop) |

#### 🔧 **Linux Installation (Ubuntu example)**

```bash
# 1. Remove older Docker versions if any
sudo apt remove docker docker-engine docker.io containerd runc

# 2. Install dependencies
sudo apt update
sudo apt install ca-certificates curl gnupg

# 3. Add Docker's official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# 4. Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 5. Install Docker Engine
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 6. Verify installation
sudo docker version
```

> 🔄 You can also run Docker without `sudo` by adding your user to the docker group:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

#### 🍎 **macOS (via Docker Desktop)**

1. Download: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
2. Install and run the app.
3. Check with:

```bash
docker version
docker info
```

> ✅ Docker Desktop includes Docker Engine, Docker CLI, Docker Compose, Kubernetes (optional), and a GUI dashboard.

#### 🪟 **Windows (via Docker Desktop)**

1. Enable **WSL2** and **Virtualization** in BIOS.
2. Install Docker Desktop from:
   [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
3. Set **backend** to **WSL2** during installation.
4. Verify with:

```powershell
docker version
docker info
```

### **2.2 Docker Daemon & Configuration**

#### 🔧 Config file paths:

| OS      | Path                                       |
| ------- | ------------------------------------------ |
| Linux   | `/etc/docker/daemon.json`                  |
| Windows | `C:\ProgramData\Docker\config\daemon.json` |
| macOS   | Controlled via GUI (Docker Desktop)        |

#### 🔹 Example: `daemon.json`

```json
{
  "log-driver": "json-file",
  "log-level": "warn",
  "storage-driver": "overlay2",
  "insecure-registries": ["myregistry.local:5000"]
}
```

After changes:

```bash
sudo systemctl restart docker
```

### **2.3 Rootless Docker (Advanced but Important)**

#### 🔒 What is it?

Run Docker **entirely as a non-root user** — improves security in multi-user systems.

#### Setup (Linux):

```bash
# Install user-level Docker
sudo apt install docker-ce-rootless-extras
dockerd-rootless-setuptool.sh install
```

> Use `docker context use rootless` to switch.

### ✅ Verify Docker Installation

Try:

```bash
docker run hello-world
```

If successful, you’ll see:

> “Hello from Docker! This message shows that your installation appears to be working correctly.”

I have been following [Udemy - Docker Essentials](https://www.udemy.com/course/docker-essentials/) course, to gain basic understanding about Docker and its commands.

Later we had a session on FastAPI by our seniors. In that, he had created an API for tenant based Task management.

After the session, my mentor and I discussed about Tenant in detail, how various components of FastAPI and database schemas are handled in it. Middleware plays a crucial part in dividing the requests on organizational level.

Also, we have a potluck party day after tomorrow, so we finalized a dish that we are going to prepare.

So that's it for today. See you tomorrow. Bye!
