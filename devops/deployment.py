import subprocess

# Dockerfile content
DOCKERFILE_CONTENT = """
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app
"""

def create_dockerfile():
    with open("Dockerfile", "w") as dockerfile:
        dockerfile.write(DOCKERFILE_CONTENT)

def build_docker_image():
    subprocess.run(["docker", "build", "-t", "myapp", "."])

def run_docker_container():
    subprocess.run(["docker", "run", "-d", "--name", "myappcontainer", "-p", "80:80", "myapp"])

if __name__ == "__main__":
    create_dockerfile()
    build_docker_image()
    run_docker_container()
