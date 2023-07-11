from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from apps.models.models import RoosterData

@api_view(['GET', 'POST'])
def create_rooster_data(request):
    secret_key = request.data.get('secret_key')

    if secret_key != settings.SECRET_KEY:
        return Response({'error': 'Invalid secret key.'}, status=401)

    if request.method == 'POST':
        clt = request.data.get('clt')
        date = request.data.get('date')
        meta_value = request.data.get('meta_value')

        if clt and date and meta_value:
            rooster_data, created = RoosterData.objects.update_or_create(
                clt=clt, date=date,
                defaults={'meta_value': meta_value}
            )

            if created:
                return Response({'message': 'RoosterData created successfully.'}, status=201)
            else:
                return Response({'message': 'RoosterData updated successfully.'}, status=200)
        else:
            return Response({'error': 'Incomplete data provided.'}, status=400)
    else:
        return Response({'message': 'GET request received.'})
