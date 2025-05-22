# Docker

Now that we have a good grasp over Python web frameworks, it is time to understand in depth about Docker, a containerization platform.

##### Dt. 19 May, 2025.

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

##### Dt. 20 May, 2025.

## **📦 Section 3: Building & Managing Docker Images**

### **3.1 Dockerfile Syntax & Basics**

A `Dockerfile` is a **recipe** for building a Docker image. It's made of instructions that get executed step-by-step.

#### 🧾 Sample `Dockerfile`

```dockerfile
# 1. Base image
FROM python:3.11-slim

# 2. Working directory inside container
WORKDIR /app

# 3. Copy app files
COPY . .

# 4. Install dependencies
RUN pip install -r requirements.txt

# 5. Default command
CMD ["python", "app.py"]
```

#### 🧱 Key Dockerfile Instructions

| Instruction    | Purpose                                      |
| -------------- | -------------------------------------------- |
| `FROM`         | Base image (first line, required)            |
| `RUN`          | Run shell commands during image build        |
| `COPY` / `ADD` | Copy files/folders into the image            |
| `WORKDIR`      | Set working directory inside container       |
| `CMD`          | Default command to run when container starts |
| `EXPOSE`       | Document the port the container will use     |
| `ENV`          | Set environment variables                    |
| `ENTRYPOINT`   | Preferred startup command behavior           |
| `VOLUME`       | Declare volume mount points                  |

### **3.2 Build Context & Multi-Stage Builds**

#### 🔍 Build Context

The build context is the folder you pass to the `docker build` command — everything inside it is **sent to the Docker daemon**.

```bash
docker build -t myapp:latest .
```

- The dot (`.`) means "current directory" as context.
- Avoid including `.git/`, `venv/`, etc. — use a `.dockerignore` file.

#### 📁 `.dockerignore`

```bash
.git
__pycache__/
*.pyc
venv/
```

#### 🧱 Multi-Stage Builds (Optimize image size)

```dockerfile
# Stage 1: Builder
FROM node:18 as builder
WORKDIR /app
COPY . .
RUN npm install && npm run build

# Stage 2: Final image
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
```

> ⚡ Reduces final image size — great for production!

### **3.3 Tagging, Pushing, Pulling, Pruning**

#### 📦 Build and Tag an Image

```bash
docker build -t username/myapp:1.0 .
```

#### ⬆️ Push to Docker Hub

```bash
docker login
docker push username/myapp:1.0
```

#### ⬇️ Pull from Docker Hub

```bash
docker pull username/myapp:1.0
```

#### 🗑️ Clean Up

```bash
# Remove dangling images (untagged)
docker image prune

# Remove all unused images
docker image prune -a

# List images
docker images
```

## **🚀 Section 4: Container Lifecycle**

### **4.1 Creating, Running, Attaching to Containers**

#### ▶️ Create and Run a Container

```bash
docker run -d --name myapp -p 5000:5000 myimage:latest
```

| Flag     | Meaning                            |
| -------- | ---------------------------------- |
| `-d`     | Detached mode (runs in background) |
| `--name` | Assign a name to the container     |
| `-p`     | Map port `host:container`          |

#### 🧪 Interactively Run a Container

```bash
docker run -it ubuntu bash
```

- `-i`: Interactive
- `-t`: Allocate TTY (terminal)
- `ubuntu`: Image name
- `bash`: Start with bash shell

#### 🔗 Attach to a Running Container

```bash
docker attach myapp
```

Or spawn a new shell into it:

```bash
docker exec -it myapp bash
```

> Useful for debugging or manual inspections.

### **4.2 Inspect, Logs, Stats**

#### 📋 Inspect Container Details

```bash
docker inspect myapp
```

Outputs full JSON about mounts, network, config, etc.

#### 📜 View Logs

```bash
docker logs myapp
```

Use `-f` to follow logs in real-time:

```bash
docker logs -f myapp
```

#### 📊 View Stats (Live)

```bash
docker stats
```

### **4.3 Start, Stop, Restart, Remove**

```bash
docker stop myapp
docker start myapp
docker restart myapp
docker rm myapp
```

- Use `-f` with `rm` to force remove a running container.

#### 🧹 Clean up all stopped containers

```bash
docker container prune
```

### **4.4 Resource Limits (CPU, Memory, PID)**

#### 🧠 Limit Memory

```bash
docker run -m 256m myapp
```

#### 🧮 Limit CPU

```bash
docker run --cpus="1.5" myapp
```

#### 🚫 Limit Max Processes (PIDs)

```bash
docker run --pids-limit=100 myapp
```

Later, I read about [psycopg2 - cursor.mogrify()](https://www.geeksforgeeks.org/format-sql-in-python-with-psycopgs-mogrify/) method to insert parametrized SQL statements in FastAPI.

I helped solve Package related issues for one of my co-trainees. Later, one of my other co-trainee gave me an overview for Docker and DockerHub.

We have planned for having Cold Sandwich for tomorrow's Potluck party!

So that's it for today, see you tomorrow. Bye!

##### Dt. 21 May, 2025.

I have watched a video tutorial of [Techworld by Nana](https://youtu.be/3c-iBn73dDE) and following is a short summary of commands I have encountered in the tutorial as of now -

- **docker pull <image_name>** => Pull image from repository
- **docker run <image_name>** => Run a new container
- **docker start <container_id>** => Start a stopped container
- **docker stop <container_id>** => Stop a running container
- **docker rm <container_id>** => Remove Container
- **docker run -d <image_name>** => detached mode (runs in the background)
- **docker run -p<host_port>:<container_port> <image_name>** => Run container on specific port
- **docker ps** => List of Running Containers
- **docker ps -a** => List of all running and stopped Container
- **docker images** => List of all pulled Images
- **docker rmi <image_name>** => Remove a pulled Image
- **docker exec -it <container_id> /bin/bash** => Executes the Interactive Terminal inside of a Container
- **docker run -d --name <container_name> <image_name>** => for name of container

I found this blog fundamental for an overview of Docker -> [Medium - Docker Tutorial for beginners](https://medium.com/geekculture/docker-tutorial-for-beginners-8af6a4967378)

Now the fun part of the day - We had the Potluck Party today, and it was amazingggg. We got to taste so many delicious delicacies - featuring lip-smacking Coleslaw Sandwich (made by our python trainees team), and super delicious Mojito (by python developers team).

Few of the other tasty dishes were - Cheese Loaded Mexican Nachos, Monaco bites, and everybody's favourite - Pani puri and Dahi Puri.

So that's it for today, see you tomorrow. Bye!

##### Dt. 22 May, 2025.

I have completed 2 hours from [Techworld with Nana](https://youtu.be/3c-iBn73dDE) video. Following new commands I have learnt -

**docker network ls** -> To list all networks
**docker network create <network_name>** -> To create new network
**docker run -e <variable_value_pair>** -> To run container with environment variables
**docker run --net <network_name>** -> To run container is a specified network
**docker logs <container_name> | tail** -> To create logs of a container
**docker-compose -f <file_name> up** -> To build a network of containers using Compose
**docker-compose -f <file_name> down** -> To stop the network of containers
**docker build -t <image_name>:<version> <file_path>** -> To build an image of application

#### Few Notes -

- Everytime new container is built its data is lost, to have persistent data use Docker Volumes instead.
- Docker Compose is used to bundle various containers together and all the parameters of the Docker command can be added inside the yaml file instead.
- Dockerfile is a blueprint to create Docker images. It is always based on another image, using the FROM keyword.
- FROM, ENV, RUN, CMD and COPY are the kywords used inside dockerfile.
- Why you should not copy env files inside images? Because of security reasons as those confidential data can be accessed by others as well.
- Rather add it in docker-compose file or add the env variables in command on runtime

I found this stackoverflow article useful - [Docker-Compose Common Mistake](https://stackoverflow.com/questions/36724948/docker-compose-unsupported-config-option-for-services-service-web)

I have containerized both the POCs that I had created in FastAPI, you can have a look at it here -> [FastAPI-POC](https://github.com/Tanishqua-Simform/FastAPI-POC).

I have created a simple container for POC-1 whereas 2 containers for POC-2 using docker compose. One I have created for Postgres and the other for my FastAPI App.

So that's it for today, see you tomorrow. Bye!
