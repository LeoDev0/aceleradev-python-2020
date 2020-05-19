from main import Manager, Employee, Seller
import pytest


class TestChalange2:

    def test_employer_class(self):
        with pytest.raises(TypeError):
            Employee(123, 123, 123)

    def test_manager_class(self):
        manager = Manager(123, 123, 123)
        with pytest.raises(AttributeError):
            manager.departament.name

    def test_seller_class(self):
        seller = Seller(123, 123, 123)
        with pytest.raises(AttributeError):
            seller.departament.name = 'coders'
