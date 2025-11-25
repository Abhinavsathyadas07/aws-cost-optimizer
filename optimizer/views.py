from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .services.cost_calculator import CostCalculator
from .services.template_generator import TemplateGenerator
from .services.scaling_optimizer import ScalingOptimizer
from .services.region_analyzer import RegionAnalyzer

# Keep a simple in-memory cache for stat updates
dashboard_stats = {
    'savings': 823,
    'uptime': 96.2,
    'projection': 2452,
    'calc_time': 2.1,
    'cheapest_region': 'us-east-1',
    'lambda_count': 0,
    's3_status': 'Healthy',
}

class HomeView(View):
    def get(self, request):
        return render(request, 'optimizer/sidebar_dashboard.html', {'dashboard_stats': dashboard_stats})

@method_decorator(csrf_exempt, name='dispatch')
class CostCalculatorView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            instance_type = data.get('instance_type','t3.micro')
            count = int(data.get('count',1))
            hours = int(data.get('hours',720))
            calc = CostCalculator()
            cost = calc.calculate_deployment_cost(instance_type, count, hours)
            dashboard_stats['projection'] = cost
            dashboard_stats['calc_time'] = 2.05  # Simulate timing, real value needed
            return JsonResponse({'status':'success','cost':cost,'stats':dashboard_stats})
        except Exception as e:
            return JsonResponse({'status':'error','error':str(e),'stats':dashboard_stats})

@method_decorator(csrf_exempt, name='dispatch')
class ScalingOptimizerView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            optimizer = ScalingOptimizer()
            optimized = optimizer.optimize(data)
            dashboard_stats['uptime'] = 97.8  # Example, use result if possible
            dashboard_stats['savings'] = 901  # Example, simulate saving
            return JsonResponse({'status': 'success', 'optimized': optimized, 'stats': dashboard_stats})
        except Exception as e:
            return JsonResponse({'status':'error','error':str(e),'stats':dashboard_stats})

@method_decorator(csrf_exempt, name='dispatch')
class RegionAnalyzerView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            analyzer = RegionAnalyzer()
            instance_type = data.get('instance_type','t3.micro')
            regions = data.get('regions',['us-east-1','eu-west-1'])
            comparison = analyzer.compare_costs(instance_type, regions)
            min_region = min(comparison, key=comparison.get) if comparison else 'N/A'
            dashboard_stats['cheapest_region'] = min_region
            return JsonResponse({'status': 'success', 'comparison': comparison, 'stats': dashboard_stats})
        except Exception as e:
            return JsonResponse({'status':'error','error':str(e),'stats':dashboard_stats})

@method_decorator(csrf_exempt, name='dispatch')
class TemplateGeneratorView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            generator = TemplateGenerator()
            template = generator.generate_beanstalk_template(data)
            dashboard_stats['lambda_count'] += 1  # Simulate a lambda event
            dashboard_stats['s3_status'] = 'Healthy'  # Example, call real service if needed
            return JsonResponse({'status': 'success', 'template': template, 'stats': dashboard_stats})
        except Exception as e:
            return JsonResponse({'status':'error','error':str(e),'stats':dashboard_stats})
