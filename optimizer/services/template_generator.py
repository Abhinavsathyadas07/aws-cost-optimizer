class TemplateGenerator:
    def generate_beanstalk_template(self, config):
        # Stub: Return a sample AWS Elastic Beanstalk template
        # Replace with actual template logic
        template = {
            'AWSTemplateFormatVersion': '2010-09-09',
            'Resources': {
                'MyElasticBeanstalkEnv': {
                    'Type': 'AWS::ElasticBeanstalk::Environment',
                    'Properties': config,
                }
            }
        }
        return template
