import unittest
from models.organization import Organization
from models.base_model import BaseModel

class TestOrganization(unittest.TestCase):
    """Test the Organization class"""

    def test_is_subclass(self):
        """Test that Organization is a subclass of BaseModel"""
        org = Organization()
        self.assertIsInstance(org, BaseModel)
        self.assertTrue(hasattr(org, "id"))
        self.assertTrue(hasattr(org, "created_date"))
        self.assertTrue(hasattr(org, "updated_date"))

    def test_attributes_default_values(self):
        """Test that attributes have default values"""
        org = Organization()
        self.assertEqual(org.name, None)
        self.assertEqual(org.email, None)
        self.assertEqual(org.password, None)
        self.assertEqual(org.phone_no, None)
        self.assertEqual(org.description, None)
        self.assertEqual(org.legal_document, None)
        self.assertEqual(org.address, None)

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        org = Organization()
        new_d = org.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in org.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        org = Organization()
        new_d = org.to_dict()
        self.assertEqual(new_d["__class__"], "Organization")
        self.assertEqual(type(new_d["created_date"]), str)
        self.assertEqual(type(new_d["updated_date"]), str)
        self.assertEqual(new_d["created_date"], org.created_date.strftime(t_format))
        self.assertEqual(new_d["updated_date"], org.updated_date.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        org = Organization()
        string = "[Organization] ({}) {}".format(org.id, org.__dict__)
        self.assertEqual(string, str(org))

if __name__ == '__main__':
    unittest.main()
