from django.contrib.auth import get_user_model
from django.conf import settings
import requests
import logging
logger = logging.getLogger(__name__)

User = get_user_model()
PERSONA_VERIFY_URL = 'https://verifier.login.persona.org/verify'

class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        response = requests.post(PERSONA_VERIFY_URL, data = {
            'audience': settings.DOMAIN,
            'assertion': assertion
        })
        if response.ok and response.json()['status'] == 'okay':
            email=response.json()['email']
            try:
                return User.objects.get(email=email)
            except User.DoesNotExist:
                return User.objects.create(email=email)
        else:
            logger.warning(
                'Persona says no. Json was: {}'.format(response.json())
            )

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
