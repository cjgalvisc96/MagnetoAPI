import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from mutants import services as mutants_services
from mutants.serializers import DNAInputSerializer, StatsOutputSerializer

logger = logging.getLogger(__name__)


class MutantView(APIView):

    @staticmethod
    def post(request):
        input_serializer = DNAInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        _data = input_serializer.validated_data
        response = mutants_services.is_mutant(dna=_data.get('dna'))
        if response:
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_403_FORBIDDEN)


class StatView(APIView):

    @staticmethod
    def get(request):
        stats = mutants_services.get_stats()
        try:
            output_data = StatsOutputSerializer(stats).data
        except Exception as error:
            logger.error(f"StatView :: output exception :: {error}")
            return Response(status=status.HTTP_403_FORBIDDEN)

        return Response(
            data=output_data,
            status=status.HTTP_200_OK
        )
