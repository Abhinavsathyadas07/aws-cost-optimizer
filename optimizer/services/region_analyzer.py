import boto3
from django.conf import settings

class RegionAnalyzer:
    def __init__(self):
        self.client = boto3.client(
            'ec2',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_DEFAULT_REGION
        )

    def get_available_regions(self, service_name='ec2'):
        # Returns a region list for specified service
        return self.client.describe_regions()['Regions']

    def compare_costs(self, instance_type, regions):
        # Stub: Compare instance cost across regions
        return {region: 0.0 for region in regions}
