import random

from django.core.management.base import BaseCommand
from faker import Faker

from app1.model.job import STATES, Job
from app1.model.task import Task


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker(locale=['pt-BR', 'pt_BR'])
        jobs = []
        for i in range(0, 100):
            state = random.choice(STATES)[0]
            data = {
                'state': state,
                'name': fake.company(),
                'address': fake.street_name(),
                'number': random.randint(123, 8952)
            }

            job = Job.objects.create(**data)

            for j in range(2, 6):
                name = fake.word(ext_word_list=None)
                name_prefix = ["Clean", "Wash", "Remove"]
                full_name = random.choice(name_prefix) + ' ' + name

                Task.objects.create(job=job, name=full_name)
