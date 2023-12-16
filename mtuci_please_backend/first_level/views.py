from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from random import *
from .models import Person
from datetime import *


class PersonsRandomize(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    def get(self, request):
        output = []
        for i in range(25):
            person_data = dict()
            gender = choice(['М', 'Ж'])
            person = Person.objects.filter(gender=gender)
            photo = choice(person.values_list('photo'))[0]
            surname = choice(person.values_list('surname'))[0]
            name = choice(person.values_list('name'))[0]
            middle_name = choice(person.values_list('middle_name'))[0]
            fullname = surname + " " + name + " " + middle_name
            now_date = datetime.now()

            person_data["photo"] = photo
            person_data['error_code'] = 0

            if randint(1, 10) <= 6:
                person_data["pass"] = True
                person_data["fullname"] = fullname
                if randint(1, 10) <= 5:
                    wrong_pass_photo = photo
                    while wrong_pass_photo == photo:
                        wrong_pass_photo = choice(person.values_list('photo'))[0]
                    person_data["pass_photo"] = wrong_pass_photo
                    person_data["error_code"] = 1
                else:
                    person_data["pass_photo"] = photo
            else:
                person_data["pass"] = False

            if randint(1, 10) <= 7:
                person_data["student_id"] = True
                person_data["student_id_photo"] = photo
                person_data["student_id_fullname"] = fullname
                person_data["student_id_date"] = "31 августа " + str(now_date.year)
            else:
                person_data["student_id"] = False

            if randint(1, 10) <= 7:
                person_data["passport"] = True
                person_data["passport_photo"] = photo
                person_data["passport_fullname"] = fullname
            else:
                person_data["passport"] = False

            if not person_data["pass"]:
                if not person_data["student_id"]:
                    person_data["error_code"] = 2
                elif not person_data["passport"]:
                    person_data["error_code"] = 3
                elif not person_data["student_id"] and not person_data["passport"]:
                    person_data["error_code"] = 4
                else:
                    if randint(1, 10) <= 2:
                        wrong_student_id_photo = photo
                        while wrong_student_id_photo == photo:
                            wrong_student_id_photo = choice(person.values_list('photo'))[0]
                        person_data["student_id_photo"] = wrong_student_id_photo
                        person_data["error_code"] = 5

                    elif randint(1, 10) <= 2:
                        wrong_index = randint(0, 3)
                        if wrong_index == 0:
                            wrong_surname = surname
                            while wrong_surname == surname:
                                wrong_surname = choice(person.values_list('surname'))[0]
                            person_data["student_id_fullname"] = wrong_surname + " " + name + " " + middle_name
                        elif wrong_index == 1:
                            wrong_name = name
                            while wrong_name == name:
                                wrong_name = choice(person.values_list('name'))[0]
                            person_data["student_id_fullname"] = surname + " " + wrong_name + " " + middle_name
                        else:
                            wrong_middle_name = middle_name
                            while wrong_middle_name == middle_name:
                                wrong_middle_name = choice(person.values_list('middle_name'))[0]
                            person_data["student_id_fullname"] = surname + " " + name + " " + wrong_middle_name
                        person_data["error_code"] = 6

                    elif randint(1, 10) <= 2:
                        person_data["student_id_date"] = "31 августа " + str(now_date.year - randint(1, 3))
                        person_data["error_code"] = 7

                    elif randint(1, 10) <= 2:
                        wrong_passport_photo = photo
                        while wrong_passport_photo == photo:
                            wrong_passport_photo = choice(person.values_list('photo'))[0]
                        person_data["passport_photo"] = wrong_passport_photo
                        person_data["error_code"] = 8
            output.append(person_data)
        return Response(output)
