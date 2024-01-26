
import logging
import requests as re

from django.core.management.base import BaseCommand



logger = logging.getLogger(__name__)

class Command(BaseCommand):
    """"""
    def handle(self, *args, **options):

        streamlit_response = re.get('https://citizenlabs-upwardmobility-raca.streamlitapp.com/')
        self.stdout.write(f'Script finished runnning with {streamlit_response}')
