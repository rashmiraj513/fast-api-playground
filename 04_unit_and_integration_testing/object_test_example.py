import pytest


class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years


@pytest.fixture
def default_employee():
    return Student("Rashmi", "Raj", "Computer Science", 4)


def test_student_initialization(default_employee):
    assert default_employee.first_name == "Rashmi", "First name should be Rashmi"
    assert default_employee.last_name == "Raj", "Last name should be Raj"
    assert default_employee.major == "Computer Science"
    assert default_employee.years == 4
