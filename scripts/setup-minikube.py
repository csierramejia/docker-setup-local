import subprocess

def setup_services():
    try:
        subprocess.run(["kubectl", "delete", "-f", "./minikube/deployment.yaml"], check=False)
        subprocess.run(["kubectl", "delete", "-f", "./minikube/service.yaml"], check=False)
        subprocess.run(["kubectl", "delete", "-f", "./minikube/castlemock-pvc.yaml"], check=False)

        # Stop and remove services defined in docker-compose.yml
        subprocess.run(["kubectl", "apply", "-f", "./minikube/castlemock-pvc.yaml"], check=True)
        print("Apply pvc.")

        subprocess.run(["kubectl", "apply", "-f", "./minikube/deployment.yaml"], check=True)
        print("Apply deployment.")

        subprocess.run(["kubectl", "apply", "-f", "./minikube/service.yaml"], check=True)
        print("Apply service.")

    except subprocess.CalledProcessError as e:
        print(f"Error starting services: {e}")
        raise

if __name__ == "__main__":
    setup_services()
