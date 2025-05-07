import subprocess
import requests
import time

# List of Docker container names or image names to start
docker_containers = [
    'docker run -d --name server1 server1_image',
    'docker run -d --name server2 server2_image',
    'docker run -d --name server3 server3_image'
]

# List of server URLs to check
urls = [
    'http://localhost:5001/api/endpoint',
    'http://localhost:5002/api/endpoint',
    'http://localhost:5003/api/endpoint'
]

# Store container names for later shutdown
container_names = []

# Function to start the Docker containers
def start_docker_containers(commands):
    for command in commands:
        process = subprocess.Popen(command, shell=True)
        container_names.append(command.split(' ')[3])  # Extract container name
        print(f"Starting container with command: {command}")
        time.sleep(5)  # Adjust if needed to ensure containers start properly

# Function to check the status of URLs
def check_urls(url_list):
    for url in url_list:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"URL {url} is up and running!")
            else:
                print(f"URL {url} returned status code {response.status_code}.")
        except requests.exceptions.RequestException as e:
            print(f"URL {url} failed to connect: {e}")

# Function to stop Docker containers
def stop_docker_containers():
    for container in container_names:
        subprocess.run(f'docker stop {container}', shell=True)
        subprocess.run(f'docker rm {container}', shell=True)
        print(f"Container {container} has been stopped and removed.")

# Start the Docker containers
start_docker_containers(docker_containers)

# Verify the URLs after starting containers
check_urls(urls)

# Shut down the Docker containers after testing
stop_docker_containers()
