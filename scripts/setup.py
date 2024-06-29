import subprocess

def setup_services():
    try:
        # Stop and remove services defined in docker-compose.yml
        subprocess.run(["docker-compose", "down"], check=True)
        print("Services removed successfully.")

        # Build and start services defined in docker-compose.yml
        subprocess.run(["docker-compose", "up", "-d"], check=True)
        print("Services started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting services: {e}")
        raise

if __name__ == "__main__":
    setup_services()
