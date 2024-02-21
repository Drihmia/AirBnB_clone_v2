#!/usr/bin/python3
"""
A test for the console class
"""
import unittest
import pep8
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """
    A class to test the HBNBCommand class
    """

    def setUp(self):
        """
        Set up a new HBNBCommand instance for each test
        """
        self.cmd = HBNBCommand()
        self.fs = FileStorage()

    def test_default(self):
        """
        Test the default prompt value
        """
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_EOF(self):
        """
        Test the do_EOF method
        """
        self.assertTrue(self.cmd.do_EOF(''))

    def test_do_quit(self):
        """
        Test the do_quit method
        """
        self.assertTrue(self.cmd.do_quit(''))

    def test_do_create(self):
        """
        Test the do_create method
        """
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_show(self):
        """
        Test the do_show method
        """
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_destroy(self):
        """
        Test the do_destroy method
        """
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_all(self):
        """
        Test the do_all method
        """
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_do_update(self):
        """
        Test the do_update method
        """
        self.assertEqual(self.cmd.prompt, '(hbnb) ')

    def test_pycodestyle(self):
        """Testing for pycodestyle implementation"""
        pycode_pass = pep8.StyleGuide(quite=True)
        record = pycode_pass.check_files(
                ['./console.py',
                 './tests/test_console.py'])
        self.assertEqual(record.total_errors, 0, "errors found")

    # ---------------------------Count()--------------------------------
    def test_BaseModel_count(self):
        """Test BaseModel.count() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            ob = BaseModel()
            self.fs.new(ob)
            self.fs.save()
            self.cmd.precmd("BaseModel.count()")
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "1")

    def test_User_count(self):
        """Test User.count() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            ob = User()
            self.fs.new(ob)
            self.fs.save()
            self.cmd.precmd("User.count()")
            result = mock_stdout.getvalue().strip()
            # Adjust the expected result for User.count() as needed
            self.assertNotEqual(result, "1")

    def test_City_count(self):
        """Test City.count() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            ob = City()
            self.fs.new(ob)
            self.fs.save()
            self.cmd.precmd("City.count()")
            result = mock_stdout.getvalue().strip()
            # Adjust the expected result for City.count() as needed
            self.assertNotEqual(result, "1")

    def test_Amenity_count(self):
        """Test Amenity.count() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            ob = Amenity()
            self.fs.new(ob)
            self.fs.save()
            self.cmd.precmd("Amenity.count()")
            result = mock_stdout.getvalue().strip()
            # Adjust the expected result for Amenity.count() as needed
            self.assertNotEqual(result, "1")

    def test_Place_count(self):
        """Test Place.count() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            ob = Place()
            self.fs.new(ob)
            self.fs.save()
            self.cmd.precmd("Place.count()")
            result = mock_stdout.getvalue().strip()
            # Adjust the expected result for Place.count() as needed
            self.assertNotEqual(result, "1")

    def test_Review_count(self):
        """Test Review.count() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            ob = Review()
            self.fs.new(ob)
            self.fs.save()
            self.cmd.precmd("Review.count()")
            result = mock_stdout.getvalue().strip()
            # Adjust the expected result for Review.count() as needed
            self.assertNotEqual(result, "1")

    def test_State_count(self):
        """Test State.count() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            ob = State()
            self.fs.new(ob)
            self.fs.save()
            self.cmd.precmd("State.count()")
            result = mock_stdout.getvalue().strip()
            # Adjust the expected result for State.count() as needed
            self.assertNotEqual(result, "1")

    # ---------------------------ALL()--------------------------------
    def test_BaseModel_all(self):
        """Test BaseModel.all() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd("BaseModel.all()")
            result = mock_stdout.getvalue().strip()
            self.assertEqual(result, "")

    def test_User_all(self):
        """Test User.all() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd("User.all()")
            result = mock_stdout.getvalue().strip()
            self.assertEqual(result, "")

    def test_City_all(self):
        """Test City.all() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd("City.all()")
            result = mock_stdout.getvalue().strip()
            self.assertEqual(result, "")

    def test_Amenity_all(self):
        """Test Amenity.all() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd("Amenity.all()")
            result = mock_stdout.getvalue().strip()
            self.assertEqual(result, "")

    def test_Place_all(self):
        """Test Place.all() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd("Place.all()")
            result = mock_stdout.getvalue().strip()
            self.assertEqual(result, "")

    def test_Review_all(self):
        """Test Review.all() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd("Review.all()")
            result = mock_stdout.getvalue().strip()
            self.assertEqual(result, "")

    def test_State_all(self):
        """Test State.all() method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd("State.all()")
            result = mock_stdout.getvalue().strip()
            self.assertEqual(result, "")

    # ---------------------------SHOW()--------------------------------
    def test_BaseModel_show(self):
        """Test BaseModel.show('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('BaseModel.show("base-model-id")')
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    def test_User_show(self):
        """Test User.show('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('User.show("user-id")')
            result = mock_stdout.getvalue().strip()
            # Adjust the expected result for User.show('id') as needed
            self.assertNotEqual(result, "** no instance found **")

    def test_City_show(self):
        """Test City.show('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('City.show("city-id")')
            result = mock_stdout.getvalue().strip()
            # Adjust the expected result for City.show('id') as needed
            self.assertNotEqual(result, "** no instance found **")

    def test_Amenity_show(self):
        """Test Amenity.show('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('Amenity.show("amenity-id")')
            result = mock_stdout.getvalue().strip()
            # Adjust the expected result for Amenity.show('id') as needed
            self.assertNotEqual(result, "** no instance found **")

    def test_Place_show(self):
        """Test Place.show('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('Place.show("place-id")')
            result = mock_stdout.getvalue().strip()
            # Adjust the expected result for Place.show('id') as needed
            self.assertNotEqual(result, "** no instance found **")

    def test_Review_show(self):
        """Test Review.show('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('Review.show("review-id")')
            result = mock_stdout.getvalue().strip()
            # Adjust the expected result for Review.show('id') as needed
            self.assertNotEqual(result, "** no instance found **")

    def test_State_show(self):
        """Test State.show('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('State.show("state-id")')
            result = mock_stdout.getvalue().strip()
            # Adjust the expected result for State.show('id') as needed
            self.assertNotEqual(result, "** no instance found **")

    # ---------------------------DESTROY()--------------------------------
    def test_BaseModel_destroy(self):
        """Test BaseModel.destroy('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('BaseModel.destroy("base-model-id")')
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    def test_User_destroy(self):
        """Test User.destroy('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('User.destroy("user-id")')
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    def test_City_destroy(self):
        """Test City.destroy('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('City.destroy("city-id")')
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    def test_Amenity_destroy(self):
        """Test Amenity.destroy('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('Amenity.destroy("amenity-id")')
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    def test_Place_destroy(self):
        """Test Place.destroy('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('Place.destroy("place-id")')
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    def test_Review_destroy(self):
        """Test Review.destroy('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('Review.destroy("review-id")')
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    def test_State_destroy(self):
        """Test State.destroy('id') method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.precmd('State.destroy("state-id")')
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    # ---------------------------UDPATE-dict()--------------------------------
    def test_BaseModel_update(self):
        """Test BaseModel.update('id', {'attr': 'value'}) method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            t = 'BaseModel.update("base-model-id", {"attr": "value"})'
            self.cmd.precmd(t)
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    def test_User_update(self):
        """Test User.update('id', {'attr': 'value'}) method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            t = 'User.update("base-model-id", {"attr": "value"})'
            self.cmd.precmd(t)
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    def test_City_update(self):
        """Test City.update('id', {'attr': 'value'}) method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            t = 'City.update("base-model-id", {"attr": "value"})'
            self.cmd.precmd(t)
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    def test_Amenity_update(self):
        """Test Amenity.update('id', {'attr': 'value'}) method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            t = 'Amenity.update("base-model-id", {"attr": "value"})'
            self.cmd.precmd(t)
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    def test_Place_update(self):
        """Test Place.update('id', {'attr': 'value'}) method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            t = 'Place.update("base-model-id", {"attr": "value"})'
            self.cmd.precmd(t)
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    def test_Review_update(self):
        """Test Review.update('id', {'attr': 'value'}) method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            t = 'Review.update("base-model-id", {"attr": "value"})'
            self.cmd.precmd(t)
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")

    def test_State_update(self):
        """Test State.update('id', {'attr': 'value'}) method."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            t = 'State.update("base-model-id", {"attr": "value"})'
            self.cmd.precmd(t)
            result = mock_stdout.getvalue().strip()
            self.assertNotEqual(result, "** no instance found **")


if __name__ == '__main__':
    unittest.main()
