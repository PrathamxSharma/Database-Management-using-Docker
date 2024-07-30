Orders Analysis Application


Project Overview
This project is designed to analyze customer order data using Python and Docker. The analysis includes calculating total revenue per month, per product, and per customer, as well as identifying the top 10 customers by revenue.

Project Structure
.
├── Dockerfile              # Dockerfile for the main application
├── Dockerfile.test         # Dockerfile for the test service
├── README.md               # Project documentation
├── analyze_orders.py       # Main script to analyze orders
├── generate_data.py        # Script to generate random order data
├── orders.csv              # Generated orders data file
├── requirements.txt        # Python dependencies
├── test_analyze_orders.py  # Unit tests for the analysis script
└── docker-compose.yml      # Docker Compose file to manage services


Project Components
1. generate_data.py
Generates random order data using the Faker library.
Creates orders.csv with columns: order_id, customer_id, order_date, product_id, product_name, product_price, quantity.
2. analyze_orders.py
Reads the orders.csv file and performs the following analyses:
Computes total revenue per month.
Computes total revenue per product.
Computes total revenue per customer.
Identifies the top 10 customers by revenue.
3. test_analyze_orders.py
Contains unit tests for the functions in analyze_orders.py using the unittest framework.
4. Docker Setup
Dockerfile: Builds the Docker image for the main application.
Dockerfile.test: Builds the Docker image for the test service.
docker-compose.yml: Manages and orchestrates the Docker containers.


Bringing Up the Project Using Docker
Prerequisites
Ensure Docker and Docker Compose are installed on your system.

Steps to Run the Project

Build the Docker Images:
docker-compose build

Run the Application:

docker-compose up app
This command starts the Docker container for the main application, reads orders.csv, performs the analysis, and displays the results.
Run the Tests:

docker-compose up test
This command starts the Docker container for the test service, runs the unit tests, and shows the test results.

Output Explanation
Monthly Revenue: Lists total revenue for each month.
Product Revenue: Shows total revenue for each product.
Customer Revenue: Displays total revenue for each customer.
Top Customers by Revenue: Highlights the top 10 customers by revenue.

Conclusion
This project automates the analysis of customer order data, ensuring accurate and efficient data processing. It leverages Docker for containerization, making it easy to set up and run the application consistently across different environments.

About This Project
This project is for tanX.fi. I am passionate about working on data analysis projects like this. I admire tanX.fi's innovative approach to technology solutions and their commitment to excellence. I would be excited to bring my skills to your team and contribute to your continued success.