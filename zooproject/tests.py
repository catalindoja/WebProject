from django.test import TestCase
from django.contrib.auth.models import *
from .models import *


# Create your tests here.
class ZooCreationTestCase(TestCase):
    def setUp(self):
        Zoo.objects.create(name='Zoo Test', description='Testing the zoo class',
                           max_visitors=200, address='Lleida', postalcode=25005)

    def test_zoo_creation_and_retrieval(self):
        zoo = Zoo.objects.get(name='Zoo Test')
        self.assertEqual(zoo.name, 'Zoo Test')
        self.assertEqual(zoo.max_visitors, 200)
        self.assertEqual(zoo.postalcode, 25005)


class AnimalCreationTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name='Horse')

    def test_animal_creation_and_retrieval(self):
        animal = Animal.objects.get(name='Horse')
        self.assertEqual(animal.name, 'Horse')


class VeterinaryCreationTestCase(TestCase):
    def setUp(self):
        zoo = Zoo.objects.create(name='Zoo Test', description='Testing the zoo class',
                           max_visitors=200, address='Lleida', postalcode=25005)
        user = WebUser.objects.create_user(username='testuser')
        user.is_veterinary = True
        Veterinary.objects.create(
            User=user, postalcode=25005,
            zoo_id=zoo, number_assigned_animals=10,
            name='John Doe', address='Lleida',
            age=25)

    def test_veterinary_creation_and_retrieval(self):
        user = WebUser.objects.get(username='testuser')
        vet = Veterinary.objects.get(User=user)
        self.assertEqual(vet.name, 'John Doe')


class StaffCreationTestCase(TestCase):
    def setUp(self):
        zoo = Zoo.objects.create(name='Zoo Test', description='Testing the zoo class',
                           max_visitors=200, address='Lleida', postalcode=25005)
        user = WebUser.objects.create_user(username='testuser2')
        user.is_zoo_staff = True
        Staff.objects.create(
            User=user, postalcode=25005,
            zoo_id=zoo, assigned_habitat='Zebras',
            name='John Doe', address='Lleida',
            age=25)

    def test_staff_creation_and_retrieval(self):
        user = WebUser.objects.get(username='testuser2')
        staff = Staff.objects.get(User=user)
        self.assertEqual(staff.name, 'John Doe')


class VisitorCreationTestCase(TestCase):
    def setUp(self):
        zoo = Zoo.objects.create(name='Zoo Test', description='Testing the zoo class',
                                 max_visitors=200, address='Lleida', postalcode=25005)
        user = WebUser.objects.create_user(username='testuser3')
        user.is_visitor = True
        Visitor.objects.create(
            User=user, telephone=111111111, name='John Doe', email='abc@a.com',
            age=25, dateLatestVisit='2022-10-05', zoo_id=zoo)

    def test_staff_creation_and_retrieval(self):
        user = WebUser.objects.get(username='testuser3')
        visitor = Visitor.objects.get(User=user)
        self.assertEqual(visitor.name, 'John Doe')

class AnimalEditTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name='Giraffe')

    def test_animal_creation_and_retrieval(self):
        Animal.objects.filter(name='Giraffe').update(name='Shark')
        animal = Animal.objects.get(name='Shark')
        self.assertEqual(animal.name, 'Shark')

class AnimalDeleteTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name='Rhino')

    def test_animal_creation_and_retrieval(self):
        Animal.objects.filter(name='Rhino').delete()
        self.assertEqual(Animal.objects.filter(name='Rhino').exists(), False)
