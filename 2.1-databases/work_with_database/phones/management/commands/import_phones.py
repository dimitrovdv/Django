import csv
import os

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = csv.reader(file, delimiter=';')
            print(phones)
            next(phones)
            for phone in phones:
                Phone.objects.create(
                        name = phone[1],
                        price = phone[3],
                        image = phone[2],
                        release_date = phone[4],
                        lte_exists = phone[5],
                        slug = slugify(phone[1])
                    )
