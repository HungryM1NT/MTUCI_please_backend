from rest_framework.views import APIView
from rest_framework.response import Response
from random import *
from .models import Person
from datetime import *


class PersonsRandomize(APIView):
    def get(self, request):
        output = dict()
        for i in range(10):
            gender = choice(['М', 'Ж'])
            person = Person.objects.filter(gender=gender)
            photo = choice(person.values_list('photo'))[0]
            surname = choice(person.values_list('surname'))
            name = choice(person.values_list('name'))
            middle_name = choice(person.values_list('middle_name'))
            full_name = surname[0] + " " + name[0] + " " + middle_name[0]
            output[i] = [photo, full_name, dict()]

            if randint(1, 10) <= 6:
                if randint(1, 10) <= 5:
                    wrong_pass_photo = photo = choice(person.values_list('photo'))[0]
                    while wrong_pass_photo == photo:
                        photo = choice(person.values_list('photo'))[0]
                    output[i][2]["pass"] = wrong_pass_photo
                    output[i].append(1)
                else:
                    year = 2003
                    output[i][2]["pass"] = photo, full_name, year
            else:
                if randint(1, 10) <= 6:
                    if len(output[i]) == 3:
                        if randint(1, 10) <= 5:
                            if randint(1, 2) == 1:
                                pass
                            else:
                                pass
                    else:
                        output[i][2]["student_it"] = photo, t

                if randint(1, 10) <= 6:
                    passport_photo = photo

            if len(output[i]) == 3:
                output[i].append(0)

        return Response(output)