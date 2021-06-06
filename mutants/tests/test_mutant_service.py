from django.test import TestCase

from rest_framework.test import APIClient

from mutants.tests.fixtures import humans, invalid_entries, mutants


class MutantServiceTest(TestCase):

    def test_check_humans(self):
        for human in humans:
            client = APIClient()
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
        for mutant in mutants:
            client = APIClient()
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
        for invalid_entry in invalid_entries:
            client = APIClient()
            response = client.post(
                path='/api/v1/mutant',
                data={'dna': invalid_entry[0]},
                format='json'
            )
            self.assertEqual(
                invalid_entry[1],
                response.status_code
            )
