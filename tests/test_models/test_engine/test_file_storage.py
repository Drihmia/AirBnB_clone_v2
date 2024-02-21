#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from unittest.mock import patch
import shutil


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        self.backup_file = 'file.json.backup'
        if (os.path.exists('file.json')):
            shutil.move('file.json', self.backup_file)
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            if (os.path.exists(self.backup_file)):
                shutil.move(self.backup_file, 'file.json')
            # os.remove('file.json.backup')
        except Exception as e:
            # print("not done")
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
            self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        # Check if file.json exists
        if os.path.exists('file.json'):
            # If file exists, rename it
            shutil.move('file.json', 'file.json.backp')

        # Perform your test logic here
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

        # Restore the original file if it was renamed
        if os.path.exists('file.json.backp'):
            shutil.move('file.json.backp', 'file.json')

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    @patch('builtins.open', return_value=open('file.json', 'w'))
    def test_reload_empty(self, mock_open):
        """ Load from an empty file """
        # Check if file exists, if not, create an empty file
        if not os.path.exists('file.json'):
            open('file.json', 'w').close()
        storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)

    # new test cases with improvements
    def test_empty_reload(self):
        """Reload should not raise error when file is empty"""
        with open('file.json', 'w'):  # create an empty file
            with patch('builtins.open', return_value=open('file.json', 'w+')):
                storage.reload()

    def test_reload_nonexistent_file(self):
        """Reload should return None if file does not exist"""
        self.assertIsNone(storage.reload())

    def test_base_model_save_calls_storage_save(self):
        """BaseModel save method should call storage save"""
        new = BaseModel()
        with patch.object(storage, 'save') as mock_save:
            new.save()
            mock_save.assert_called_once()

    def test_base_model_save_no_file_created(self):
        """BaseModel save method should create file"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_base_model_save_data_saved_to_file(self):
        """Data should be saved to file upon BaseModel save"""
        new = BaseModel()
        new.save()
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_reload_successful(self):
        """Reload should successfully load objects from file"""
        new = BaseModel()
        new.save()
        storage.reload()
        loaded = storage.all().values()
        self.assertEqual(len(loaded), 1)


if __name__ == '__main__':
    unittest.main()
