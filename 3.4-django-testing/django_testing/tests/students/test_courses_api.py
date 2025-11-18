import pytest
from rest_framework.test import APIClient
from tests.conftest import client, course_factory, student_factory
import json

@pytest.mark.django_db
def test_get_course_1(client, course_factory):
    course = course_factory()

    response = client.get('/api/v1/courses/?id=1')

    assert  response.status_code == 200
    data = response.json()
    assert  data[0]['id'] ==1

@pytest.mark.django_db
def test_get_list_course(client, course_factory):
    course = course_factory(_quantity = 3)

    response = client.get('/api/v1/courses/')

    assert  response.status_code == 200
    data = response.json()
    for i, c in enumerate(data):
        assert  c['name'] == course[i].name

@pytest.mark.django_db
def test_get_filter_id_course(client, course_factory):
    course = course_factory(_quantity = 3)

    response = client.get(f'/api/v1/courses/?id={course[1].id}')

    assert response.status_code ==200
    data = response.json()
    assert data[0]['id'] == course[1].id

@pytest.mark.django_db
def test_get_filter_name_course(client, course_factory):
    course = course_factory(_quantity=3)

    response = client.get(f'/api/v1/courses/?name={course[1].name}')

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course[1].name

@pytest.mark.django_db
def test_patch_course(client, course_factory):
    data_course = {
        "name": "Paython для новичков",
        "students":[
            {
                "name": "Наташа"
            },
            {
                "name":"Леша",
                "birth_date": "2010-06-26"
            }

        ]
    }
    course = course_factory()
    response_get = client.get(f'/api/v1/courses/?id={course.id}')
    response = client.patch(f'/api/v1/courses/{course.id}/', data=json.dumps(data_course), content_type='application/json')

    assert response_get.status_code == 200
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == data_course.get('name')



@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory()  # вызовите фабрику, чтобы создать объект
    response_get = client.get(f'/api/v1/courses/?id={course.id}')
    response = client.delete(f'/api/v1/courses/{course.id}/')

    assert response_get.status_code == 200
    assert response.status_code == 204