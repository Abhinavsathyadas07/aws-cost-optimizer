from django.urls import path
from .views import (
    HomeView,
    CostCalculatorView,
    TemplateGeneratorView,
    ScalingOptimizerView,
    RegionAnalyzerView
)

app_name = 'optimizer'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/cost-calculator/', CostCalculatorView.as_view(), name='cost-calculator'),
    path('api/template-generator/', TemplateGeneratorView.as_view(), name='template-generator'),
    path('api/scaling-optimizer/', ScalingOptimizerView.as_view(), name='scaling-optimizer'),
    path('api/region-analyzer/', RegionAnalyzerView.as_view(), name='region-analyzer'),
]