from django.test import TestCase

from rest_framework.test import APIClient

from mutants.tests.fixtures import humans, invalid_entries, mutants


class MutantServiceTest(TestCase):

    def test_check_humans(self):
        client = APIClient()
        for human in humans:
            response = client.post(
                path='/api/v1/mutant',
                data={'dna': human[0]},
                format='json'
            )
            self.assertEqual(
                human[1],
                response.status_code
            )

    def test_check_mutants(self):
        client = APIClient()
        for mutant in mutants:
            response = client.post(
                path='/api/v1/mutant',
                data={'dna': mutant[0]},
                format='json'
            )
            self.assertEqual(
                mutant[1],
                response.status_code
            )

    def test_check_invalid_entries(self):
        client = APIClient()
        for invalid_entry in invalid_entries:
            response = client.post(
                path='/api/v1/mutant',
                data={'dna': invalid_entry[0]},
                format='json'
            )
            self.assertEqual(
                invalid_entry[1],
                response.status_code
            )
