from rest_framework.views import APIView
from rest_framework.response import Response
from random import *
from .models import Person


class PersonsRandomize(APIView):
    def get(self, request):
        output = dict()
        for i in range(10):
            gender = choice(['М', 'Ж'])
            person = Person.objects.filter(gender=gender)
            photo = choice(person.values_list('photo'))
            surname = choice(person.values_list('surname'))
            name = choice(person.values_list('name'))
            middle_name = choice(person.values_list('middle_name'))
            full_name = surname[0] + " " + name[0] + " " + middle_name[0]
            output[i] = [photo, full_name]

            if randint(1, 10) <= 6:
                pass_photo = photo
                if randint(1, 10) <= 5:
                    pass
            else:
                if randint(1, 10) <= 6:
                    student_card_photo = photo

                if randint(1, 10) <= 6:
                    passport_photo = photo
        return Response(output)