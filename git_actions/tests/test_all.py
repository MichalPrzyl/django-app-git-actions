import pytest
#from example_app.models import Person
from example_app.models import Person

@pytest.mark.django_db
def test_first():
    Person.objects.create(first_name="Michał", last_name="Przyłucki")
    queryset = Person.objects.all()
    assert queryset.count() == 1

@pytest.mark.django_db
def test_second():
    Person.objects.create(first_name="Michał", last_name="Przyłucki")
    queryset = Person.objects.all()
    print(f"\n\n")
    print(queryset)
    assert queryset.count() == 1