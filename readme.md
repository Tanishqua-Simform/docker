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

- **docker network ls** -> To list all networks
- **docker network create <network_name>** -> To create new network
- **docker run -e <variable_value_pair>** -> To run container with environment variables
- **docker run --net <network_name>** -> To run container is a specified network
- **docker logs <container_name> | tail** -> To create logs of a container
- **docker-compose -f <file_name> up** -> To build a network of containers using Compose
- **docker-compose -f <file_name> down** -> To stop the network of containers
- **docker build -t <image_name>:<version> <file_path>** -> To build an image of application

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

##### Dt. 23 May, 2025.

Today, I have implemented Email in FastAPI using Jinja Template. I have implemented both Async way of sending emails as well as sending those as background tasks.

Async handler paused the execution and buffered a little till the mail was sent whereas in background task the task was performed in a different thread than main execution thread, so it returned response instantaneously. You can have a look at it here -> [Email](/Email/)

Later we had an hour long meet with the HR regarding the training period and what we liked about our training and what improvements can be made in it.

I found these blogs useful,

- [Medium - Email in FastApi](https://medium.com/nerd-for-tech/how-to-send-email-using-python-fastapi-947921059f0c)
- [FastAPI - Templates](https://fastapi.tiangolo.com/advanced/templates/)
- [FastAPI-mail - Sample Mail](https://sabuhish.github.io/fastapi-mail/example/)

Then I started working on implementing email sending feature with celery but it was throwing some errors, then we all trainee went to have Vadapav and Dabeli, but when we returned there was some downtime in network, so we were told to leave early and hence, I am writing this on (26th May)

##### Dt. 26 May, 2025.

Today, I have solved 16 Sql queries from [SQL Practice](https://www.sql-practice.com/) for having a change of mind. Then I solved 2 questions from LeetCode.

Then I read about Async Programming from - [Concurrency and Async-Await](https://fastapi.tiangolo.com/async/), which we later discussed with our mentor.

- Concurrency is better for tasks that have a lot of waiting time (idle state for CPU), whereas parallelism is better for sequential tasks with minimal to no waiting time.

- Multitasking in python is performed using -

  1. Async Programming (Single threaded, Concurrrent, IO-bound tasks),
  2. Multi-threading (Multiple-threads, IO-bound Tasks, Shared memory),
  3. Multi-processing (Multiple-processes, CPU-bound tasks).

Then I completed the celery and redis task which was pending on Friday. I containerized them as well using docker later.

I found these blogs useful -

- [Stackoverflow - Celery Executable not found in path (Error)](https://stackoverflow.com/questions/75075546/celery-executable-file-not-found-in-path)
- [Blog - Dockerize FastAPI and Celery](https://www.nashruddinamin.com/blog/dockerize-your-fastapi-and-celery-application)

So that's it for today, see you tomorrow. Bye.

##### Dt. 27 May, 2025.

## **💾 Section 5: Data Persistence in Docker**

By default, when a container is removed, **all its data is lost**. To persist or share data, we use **Volumes** and **Mounts**.

### **5.1 Types of Storage in Docker**

| Storage Type     | Description                                                            |
| ---------------- | ---------------------------------------------------------------------- |
| **Volumes**      | Managed by Docker, best for persistent data                            |
| **Bind Mounts**  | Link host path to container path directly                              |
| **tmpfs Mounts** | Stored in memory, disappears when container stops (useful for secrets) |

### **5.2 Docker Volumes**

#### 📦 Create a Volume

```bash
docker volume create mydata
```

#### 🔍 List Volumes

```bash
docker volume ls
```

#### 🗑️ Remove Volume

```bash
docker volume rm mydata
```

#### 📌 Use Volume in a Container

```bash
docker run -d --name db \
  -v mydata:/var/lib/mysql \
  mysql:8
```

- `mydata`: Volume name
- `/var/lib/mysql`: Path **inside the container**

> Docker stores volume data in `/var/lib/docker/volumes/`

### **5.3 Bind Mounts**

#### 📎 Mount a Host Directory

```bash
docker run -v /absolute/host/path:/app myimage
```

Example:

```bash
docker run -it --rm \
  -v $PWD:/app \
  python:3.11-slim \
  bash
```

> ✅ Good for **development** — changes on host reflect instantly in the container.

### **5.4 tmpfs Mounts**

#### 📂 In-Memory Storage

```bash
docker run --tmpfs /run/secrets busybox
```

- Data written here is stored in memory.
- Use for **ephemeral, sensitive** data.

### **5.5 Inspect Mounts in a Container**

```bash
docker inspect <container_name>
```

Look for the `Mounts` key in the JSON output.

### **5.6 Named vs Anonymous Volumes**

#### Named Volume (explicit):

```bash
-v mydata:/data
```

#### Anonymous Volume (implicit):

```bash
-v /data
```

- Docker creates a random name.
- Harder to manage.

## **🌐 Section 6: Docker Networking**

Docker uses virtual networks to allow containers to **communicate with each other**, with the host, and with the internet.

### **6.1 Docker Network Types**

| Network Type | Description                               |
| ------------ | ----------------------------------------- |
| **bridge**   | Default for standalone containers         |
| **host**     | Shares host’s network stack               |
| **none**     | Isolated container (no network access)    |
| **overlay**  | Cross-host communication (used in Swarm)  |
| **macvlan**  | Assigns MAC address from physical network |

For most use cases, you'll work with **bridge** and **custom bridge networks**.

### **6.2 Inspect Docker Networks**

```bash
docker network ls
docker network inspect bridge
```

### **6.3 Create a Custom Network**

```bash
docker network create mynet
```

> Why? Containers on **custom networks** can communicate by name (DNS enabled).

### **6.4 Connecting Containers**

```bash
# Create network
docker network create app-net

# Run containers in that network
docker run -d --name db --network app-net postgres
docker run -d --name web --network app-net mywebapp
```

Now `web` can access the `db` container by hostname `db`.

### **6.5 Bridge Network Example**

```bash
docker network create my-bridge-net

docker run -d --name app1 --network my-bridge-net alpine sleep 1000
docker run -it --name app2 --network my-bridge-net alpine sh
```

Inside `app2`:

```sh
ping app1
```

> 🔗 Docker sets up internal DNS for containers on the **same custom bridge**.

### **6.6 Host Network (Linux only)**

```bash
docker run --network host nginx
```

- Shares host’s network namespace.
- Fast, but risky (no isolation).

### **6.7 Disconnect / Connect Containers**

```bash
docker network disconnect mynet container_name
docker network connect mynet container_name
```

### **6.8 Port Mapping (Host ↔️ Container)**

```bash
docker run -p 8080:80 nginx
```

| Host Port | Container Port       |
| --------- | -------------------- |
| `8080`    | `80` (Nginx default) |

Now visit: `http://localhost:8080`

### **6.9 Expose Port (in Dockerfile)**

```dockerfile
EXPOSE 5000
```

> This does **not** publish the port — it’s only documentation. Use `-p` to actually publish.

## **Section 7: Docker Compose**

Docker Compose lets you **define and manage multi-container applications** using a simple YAML file.

### **7.1 What is Docker Compose?**

- Tool for **defining** and **running** multi-container Docker applications.
- Configuration stored in `docker-compose.yml`.
- Run all services with **one command**.

### **7.2 Install Docker Compose (if needed)**

Docker Compose is bundled with Docker Desktop.
On Linux, install it with:

```bash
sudo apt install docker-compose-plugin
```

Verify:

```bash
docker compose version
```

### **7.3 Basic `docker-compose.yml` Example**

```yaml
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
```

### **7.4 Commands to Use**

```bash
docker compose up            # Start services
docker compose up -d         # Detached mode
docker compose down          # Stop & remove containers, networks, volumes
docker compose build         # Build images
docker compose logs          # Show logs
docker compose ps            # List running containers
```

### \*\*7.5 Volumes, Networks, Env in Compose\*\*

#### Add volumes:

```yaml
volumes:
  - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

#### Add networks:

```yaml
networks:
  - backend

networks:
  backend:
```

#### Load env variables:

```yaml
env_file:
  - .env
```

### **7.6 Depends On**

```yaml
depends_on:
  - db
```

> Controls startup **order**, but not readiness. For wait-until-ready behavior, use healthchecks or wait-for-it.sh.

### **7.7 Compose File Structure Summary**

```yaml
version: "3.9"
services:
  servicename:
    build: ./dir
    image: customimage
    ports: ["host:container"]
    volumes: ["host:container"]
    environment: ["KEY=value"]
    env_file: [.env]
    networks: [net1]
    depends_on: [other_service]
volumes:
  myvolume:
networks:
  net1:
```

## **🧠 Section 8: Dockerfile Best Practices**

A clean, efficient, and secure Dockerfile results in **smaller, faster, and more secure containers**.

### **8.1 Use Small Base Images**

Start with **minimal images** when possible.

```dockerfile
FROM python:3.11-slim   # ✅ Better than full python:3.11
FROM alpine              # ✅ Extremely lightweight (5 MB)
```

> Smaller images = faster downloads, reduced attack surface.

### **8.2 Reduce Layers**

Each `RUN`, `COPY`, `ADD` creates a **layer**. Combine commands to minimize:

```dockerfile
# ✅ Better (fewer layers)
RUN apt-get update && apt-get install -y \
    gcc libpq-dev \
 && rm -rf /var/lib/apt/lists/*
```

### **8.3 Avoid Installing Unnecessary Packages**

Only install what your app needs. Don’t blindly use:

```dockerfile
RUN apt-get install -y build-essential  # ❌ Overkill
```

### **8.4 Use `.dockerignore` File**

Avoid sending unnecessary files to Docker daemon:

```dockerignore
.git
node_modules
__pycache__/
*.pyc
.env
```

### **8.5 Pin Image Versions**

Avoid breaking changes by locking versions:

```dockerfile
FROM node:18.16.1   # ✅ Safe
FROM node:latest    # ❌ Risky
```

### **8.6 Use Multi-Stage Builds**

Keep build tools out of your final image:

```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY . .
RUN npm install && npm run build

# Stage 2: Runtime
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```

> ✅ Final image is clean and minimal.

### **8.7 Set a Non-Root User**

```dockerfile
RUN useradd -m appuser
USER appuser
```

> Never run containers as `root` in production.

### **8.8 Use `ENTRYPOINT` vs `CMD`**

- `ENTRYPOINT`: defines **fixed** command
- `CMD`: defines **default arguments**

```dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]
```

Run:

```bash
docker run myimage              # → python app.py
docker run myimage test.py     # → python test.py
```

### **8.9 Layer Caching Optimization**

Put frequently-changing steps **last** to use Docker cache effectively.

```dockerfile
# ✅ Better cache use
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

## **📦 Section 9: Docker Hub, Registries, and Image Distribution**

Docker images need to be **shared and distributed** — this is done via **container registries** like Docker Hub, GitHub Container Registry, AWS ECR, etc.

### **9.1 What is a Container Registry?**

A **registry** is a storage and distribution system for container images.

- **Public Registry** (e.g., Docker Hub)
- **Private Registry** (e.g., self-hosted or cloud-specific like AWS ECR, GCP Artifact Registry)

> Docker pulls images from registries and pushes images to registries.

### **9.2 Popular Registries**

| Registry                      | Description                       |
| ----------------------------- | --------------------------------- |
| **Docker Hub**                | Default public registry           |
| **GitHub Container Registry** | Tied to GitHub accounts           |
| **AWS ECR**                   | Amazon Elastic Container Registry |
| **GCP Artifact Registry**     | Google Cloud's registry           |
| **Azure ACR**                 | Azure Container Registry          |

### **9.3 Docker Hub Basics**

#### 🔐 Login

```bash
docker login
```

Enter Docker Hub username and password/token.

#### 📤 Push an Image

```bash
docker tag myimage username/myimage:tag
docker push username/myimage:tag
```

#### 📥 Pull an Image

```bash
docker pull ubuntu:latest
```

### **9.4 Docker Image Tags**

Docker images have names like:

```bash
repository[:tag]
```

Examples:

- `nginx:latest`
- `myuser/myapp:v1.0`
- `python:3.11-slim`

> Tag `latest` is default if no tag is given.

### **9.5 Build and Push Workflow**

```bash
# Build image
docker build -t myapp .

# Tag for Docker Hub
docker tag myapp myusername/myapp:1.0

# Push to Docker Hub
docker push myusername/myapp:1.0
```

### **9.6 View & Manage Repositories on Docker Hub**

Go to: [https://hub.docker.com](https://hub.docker.com)

- Create a repo
- Manage visibility (public/private)
- Add collaborators

### **9.7 Image Pull Policy**

Docker determines whether to pull an image based on tag and availability.

| Policy           | Behavior                                     |
| ---------------- | -------------------------------------------- |
| `always`         | Always pulls from registry                   |
| `never`          | Never pulls — only use local                 |
| `if-not-present` | Default; pulls only if not locally available |

Used in Kubernetes or advanced Compose configs.

### **9.8 Private Registry (Optional)**

Run a registry locally:

```bash
docker run -d -p 5000:5000 --name registry registry:2
```

Push image:

```bash
docker tag myapp localhost:5000/myapp
docker push localhost:5000/myapp
```

> Useful in internal networks.

Then, I solved 2 questions on backtracking from LeetCode. Later, I attended a session on SDLC by ML team, it covered various phases of SDLC as well as Monolithic and Microservices architecture. We will discuss about HLD and LLD in next session.

SDLC consists of 6 phases - Requirement gathering, Designing, Development, Testing, Deployment, Maintainence.

I found these resources helpful -

- [Monolithic Vs. MicroServices](https://www.geeksforgeeks.org/monolithic-vs-microservices-architecture/)
- [API Throttling Vs. API Rate Limiting](https://www.geeksforgeeks.org/api-throttling-vs-api-rate-limiting-system-design/)

Later, I read about testing in FastAPI and jot down following points -

- Fixtures in Pytest are used for setup and cleaning work to be done during testing.
- Fixtures are given cartain scope in which they nust be set up and torn down.
- Autouse in fixtures is used to send that particular fixture as argument to all the test functions.

I also read about few of the security breaches that can be performed on a system, such as XSS, CSRF, and MITM attacks.

So that's it for this repo, see you tomorrow with new concept. Bye!

###### With this we come to an end for our Docker Course (Learning duration - 7 days)
