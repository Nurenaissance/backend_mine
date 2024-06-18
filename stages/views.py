from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from .models import Stage
from tenant.models import Tenant
from .defaults import DEFAULT_LEAD_STAGES, DEFAULT_OPPORTUNITY_STAGES, get_or_create_default_stages
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

User = get_user_model()

@permission_classes([AllowAny])
@require_http_methods(["GET"])
def stage_list(request, model_name):
    tenant = None
    if request.user.is_authenticated:
        tenant = request.user.tenant

    stages = get_or_create_default_stages(tenant, model_name)
    stages_data = [{'id': stage.id, 'status': stage.status, 'model_name': stage.model_name} for stage in stages]
    return JsonResponse(stages_data, safe=False, status=200)

@csrf_exempt
@require_http_methods(["POST"])
def stage_create(request):
    status = request.POST.get('status')
    model_name = request.POST.get('model_name')
    tenant = None
    if request.user.is_authenticated:
        tenant = request.user.tenant

    stage_obj = Stage.objects.create(status=status, model_name=model_name, tenant=tenant)
    return JsonResponse({'id': stage_obj.id, 'status': stage_obj.status, 'model_name': stage_obj.model_name}, status=201)

@require_http_methods(["POST"])
def stage_update(request, stage_id):
    stage_obj = get_object_or_404(Stage, id=stage_id)
    stage_obj.status = request.POST.get('status')
    stage_obj.save()
    return JsonResponse({'id': stage_obj.id, 'status': stage_obj.status, 'model_name': stage_obj.model_name}, status=200)

@require_http_methods(["DELETE"])
def stage_delete(request, stage_id):
    stage_obj = get_object_or_404(Stage, id=stage_id)
    stage_obj.delete()
    return JsonResponse({'message': 'Stage deleted successfully'}, status=200)
