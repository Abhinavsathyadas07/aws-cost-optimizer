# AWS Cost Optimizer

**Cloud Architecture & Cost Optimization Tool**

A Python/Django web application to help AWS solution architects and developers optimize cloud architecture deployments.

> **Status: early prototype.** The services are scaffolds; the AWS Pricing API lookup is not implemented yet (`CostCalculator.get_instance_price` returns `0.0`).

## Features

- **Elastic Beanstalk architecture template generator**
- **Cost calculator for different deployment scenarios**
- **Auto-scaling configuration optimizer**
- **Multi-region deployment analyzer**

## Tech Stack

- **Backend:** Python, Django, AWS SDK (boto3)
- **Frontend:** Django Templates (extendable to React/Vue)
- **Cloud:** AWS Elastic Beanstalk & core AWS services

## Getting Started

1. `git clone https://github.com/Abhinavsathyadas07/aws-cost-optimizer.git`
2. Set up a Python virtual environment
3. Install requirements: `pip install -r requirements.txt`
4. Configure AWS credentials
5. Run Django dev server: `python manage.py runserver`
