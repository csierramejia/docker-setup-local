import setup_mysql
import setup_mongo
import setup_minikube

def setup_all():
    setup_mysql.setup_mysql()
    setup_mongo.setup_mongo()
    setup_minikube.setup_minikube()

if __name__ == "__main__":
    setup_all()