import pprint
from requests import post
import global_variables
import unittest

PROF_URL = f'{global_variables.BASE_URL}/professional'


class TestProfessional(unittest.TestCase):

    def test_create_professional(self):
        body = {
            'name': 'User Professional',
            'email': 'professional@email.com',
            'password': 'strongcomplicated123',
            'phone_number': 849555555,
            'addresses': [
                {
                    'state': 'RN',
                    'city': 'Natal',
                    'street': 'Avenida Prudente de Morais',
                    'complement': 'AP 123 Bloco G'
                },
                {
                    'state': 'SP',
                    'city': 'São Paulo',
                    'street': 'Avenida 25 de Março',
                    'complement': 'AP 567 Bloco B'
                }
            ],
            'provides_home_service': True,
            'specialty': 'medicine',
            'subspecialties': ['dermo', 'oftalmo'],
            'accepted_health_plans': ['unimed', 'hapvida'],
            'council_registration': 791236,
            'twitter': 'aaaaa',
            'insta': '@aaaa',
            'linkedin': 'aaaaa',
            'bio': 'aaaaaa'
        }
        response = post(PROF_URL, json=body)
        self.assertEqual(response.status_code, 201, response.content)
        pprint(response.json(), ident=4)


if __name__ == '__main__':
    unittest.main()
