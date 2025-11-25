from django.test import TestCase
from optimizer.services.cost_calculator import CostCalculator
from optimizer.services.region_analyzer import RegionAnalyzer
from optimizer.services.scaling_optimizer import ScalingOptimizer
from optimizer.services.template_generator import TemplateGenerator

class CostCalculatorTest(TestCase):
    def setUp(self):
        self.calc = CostCalculator()

    def test_calculate_deployment_cost(self):
        cost = self.calc.calculate_deployment_cost('t3.micro', 2, 24)
        self.assertTrue(isinstance(cost, float))

class TemplateGeneratorTest(TestCase):
    def test_generate_template(self):
        gen = TemplateGenerator()
        conf = {'ApplicationName': 'testApp', 'EnvironmentName': 'testEnv'}
        template = gen.generate_beanstalk_template(conf)
        self.assertIn('Resources', template)

class ScalingOptimizerTest(TestCase):
    def test_optimize(self):
        opt = ScalingOptimizer()
        config = {'min_instances': 2, 'max_instances': 15}
        result = opt.optimize(config)
        self.assertIn('recommendation', result)

class RegionAnalyzerTest(TestCase):
    def setUp(self):
        self.analyzer = RegionAnalyzer()

    def test_compare_costs(self):
        costs = self.analyzer.compare_costs('t3.micro', ['us-east-1', 'eu-west-1'])
        self.assertIn('us-east-1', costs)
        self.assertIn('eu-west-1', costs)
