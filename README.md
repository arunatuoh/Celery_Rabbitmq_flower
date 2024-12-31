This project demonstrates how to set up Celery with RabbitMQ to manage background tasks asynchronously. The example includes the steps to install RabbitMQ, configure Celery, and run tasks. It also includes instructions on how to monitor tasks using Flower.

Prerequisites
Python 3.10.12 or higher
RabbitMQ server installed
Celery package installed
Flower (for monitoring tasks, optional)


Setup Instructions

1. Install RabbitMQ Server
To use RabbitMQ as the message broker for Celery, you need to install RabbitMQ. Follow the command below to install it on your system:
sudo apt-get install rabbitmq-server
After installation, ensure RabbitMQ is running properly by checking its status:
sudo rabbitmqctl status
Alternatively, you can also check the status using the systemctl command:
sudo systemctl status rabbitmq-server


2. Enable RabbitMQ to Start Automatically on Boot
You need to enable RabbitMQ so that it starts automatically when the system boots up:
sudo systemctl enable rabbitmq-server

3. Enable RabbitMQ Management Plugin (Optional)
For a user-friendly management interface, you can enable the RabbitMQ management plugin. This will allow you to manage RabbitMQ via a web UI:
rabbitmq-plugins enable rabbitmq_management
The RabbitMQ management UI will be available at http://localhost:15672 in your browser.

Default credentials:
Username: guest
Password: guest

4. Install Celery
In order to use Celery for background task processing, you need to install the Celery package. Install it via pip:
pip install celery


5. Running Celery Worker
After installing Celery and RabbitMQ, you can start a Celery worker that will listen for tasks and execute them in the background.

Run the following command to start the Celery worker:
celery -A celery_example worker --loglevel=info

Explanation:

-A celery_example: This specifies the Python file (without the .py extension) that contains your Celery app and tasks.
worker: This starts the Celery worker that will listen for tasks.
--loglevel=info: This sets the logging level to info, which helps you monitor what the worker is doing.

6. Run Flower (Optional)
Flower is a real-time web-based tool that allows you to monitor the status of your Celery tasks. To use Flower, run the following command:
celery -A celery_example flower --broker=pyamqp://guest@localhost:5672

This will start Flower and make it available at http://localhost:5555 in your browser. You can use Flower to view task progress, failures, retries, and other details.