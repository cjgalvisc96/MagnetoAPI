import json

from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from mutants.tests.fixtures import humans, mutants


class StatsServiceTest(TestCase):

    def test_get_empty_stats(self):
        client = APIClient()
        response = client.get(path='/api/v1/stats')
        result = json.loads(response.content)
        self.assertEqual(
            status.HTTP_200_OK,
            response.status_code
        )
        self.assertEqual(
            result['count_mutant_dna'],
            0
        )
        self.assertEqual(
            result['count_human_dna'],
            0
        )
        self.assertEqual(
            result['ratio'],
            0.0
        )

    def test_get_stats_with_ratio(self):
        total_humans = 10
        total_mutants = 4
        expected_ratio = total_mutants / total_humans
        human = humans[0][0]
        mutant = mutants[0][0]
        client = APIClient()
        # Create humans
        for _ in range(total_humans):
            client.post(
                path='/api/v1/mutant',
                data={'dna': human},
                format='json'
            )

        # Create mutants
        for _ in range(total_mutants):
            client.post(
                path='/api/v1/mutant',
                data={'dna': mutant},
                format='json'
            )
        # Get stats
        response = client.get(path='/api/v1/stats')
        result = json.loads(response.content)
        self.assertEqual(
            status.HTTP_200_OK,
            response.status_code
        )
        self.assertEqual(
            result['count_human_dna'],
            total_humans
        )
        self.assertEqual(
            result['count_mutant_dna'],
            total_mutants
        )
        self.assertEqual(
            result['ratio'],
            expected_ratio
        )
