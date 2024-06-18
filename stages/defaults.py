
# defaults.py
from stages.models  import Stage

DEFAULT_LEAD_STAGES = [
    {'stage': 'assigned'},
    {'stage': 'in process'},
    {'stage': 'converted'},
    {'stage': 'recycled'},
    {'stage': 'dead'}
]

DEFAULT_OPPORTUNITY_STAGES = [
    {'stage': 'QUALIFICATION'},
    {'stage': 'NEEDS ANALYSIS'},
    {'stage': 'VALUE PROPOSITION'},
    {'stage': 'ID.DECISION MAKERS'},
    {'stage': 'PERCEPTION ANALYSIS'},
    {'stage': 'PROPOSAL/PRICE QUOTE'},
    {'stage': 'NEGOTIATION/REVIEW'},
    {'stage': 'CLOSED WON'},
    {'stage': 'CLOSED LOST'}
]

def get_or_create_default_stages(tenant, model_name):
    if model_name == 'LEAD':
        default_stages = DEFAULT_LEAD_STAGES
    elif model_name == 'OPPORTUNITY':
        default_stages = DEFAULT_OPPORTUNITY_STAGES
    else:
        return []

    stages = Stage.objects.filter(tenant=tenant, model_name=model_name)
    if not stages.exists():
        for stage in default_stages:
            Stage.objects.create(stage=stage['stage'], model_name=model_name, tenant=tenant)
        stages = Stage.objects.filter(tenant=tenant, model_name=model_name)

    return stages
