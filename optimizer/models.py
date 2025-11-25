from django.db import models


class DeploymentScenario(models.Model):
    """Store deployment scenarios for cost analysis"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    instance_type = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AutoScalingConfig(models.Model):
    """Store auto-scaling configurations"""
    scenario = models.ForeignKey(DeploymentScenario, on_delete=models.CASCADE, related_name='scaling_configs')
    min_instances = models.IntegerField(default=1)
    max_instances = models.IntegerField(default=10)
    target_cpu_utilization = models.IntegerField(default=70)
    scale_up_cooldown = models.IntegerField(default=300)
    scale_down_cooldown = models.IntegerField(default=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AutoScaling for {self.scenario.name}"