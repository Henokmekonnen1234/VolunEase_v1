import unittest
from datetime import datetime
from models.event import Event
from models.base_model import BaseModel

class TestEvent(unittest.TestCase):
    """Test the Event class"""

    def test_is_subclass(self):
        """Test that Event is a subclass of BaseModel"""
        event = Event()
        self.assertIsInstance(event, BaseModel)
        self.assertTrue(hasattr(event, "id"))
        self.assertTrue(hasattr(event, "created_date"))
        self.assertTrue(hasattr(event, "updated_date"))

    def test_title_attr(self):
        """Test that Event has attribute title, and it's an empty string"""
        event = Event()
        self.assertTrue(hasattr(event, "title"))
        self.assertIsNone(event.title)

    def test_place_attr(self):
        """Test that Event has attribute place, and it's an empty string"""
        event = Event()
        self.assertTrue(hasattr(event, "place"))
        self.assertIsNone(event.place)

    def test_start_time_attr(self):
        """Test that Event has attribute start_time, and it's None"""
        event = Event()
        self.assertTrue(hasattr(event, "start_time"))
        self.assertIsNone(event.start_time)

    def test_end_time_attr(self):
        """Test that Event has attribute end_time, and it's None"""
        event = Event()
        self.assertTrue(hasattr(event, "end_time"))
        self.assertIsNone(event.end_time)

    def test_image_attr(self):
        """Test that Event has attribute image, and it's an empty string"""
        event = Event()
        self.assertTrue(hasattr(event, "image"))
        self.assertIsNone(event.image)

    def test_org_id_attr(self):
        """Test that Event has attribute org_id, and it's an empty string"""
        event = Event()
        self.assertTrue(hasattr(event, "org_id"))
        self.assertIsNone(event.org_id)

    def test_part_time_attr(self):
        """Test that Event has attribute part_time, and it's None"""
        event = Event()
        self.assertTrue(hasattr(event, "part_time"))
        self.assertIsNone(event.part_time)

    def test_description_attr(self):
        """Test that Event has attribute description, and it's an empty string"""
        event = Event()
        self.assertTrue(hasattr(event, "description"))
        self.assertIsNone(event.description)

    def test_volunteers_attr(self):
        """Test that Event has attribute volunteers, and it's an empty list"""
        event = Event()
        self.assertTrue(hasattr(event, "volunteers"))
        self.assertEqual(event.volunteers, [])

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        event = Event()
        new_d = event.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in event.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        event = Event()
        new_d = event.to_dict()
        self.assertEqual(new_d["__class__"], "Event")
        self.assertEqual(type(new_d["created_date"]), str)
        self.assertEqual(type(new_d["updated_date"]), str)
        self.assertEqual(new_d["created_date"], event.created_date.strftime(t_format))
        self.assertEqual(new_d["updated_date"], event.updated_date.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        event = Event()
        string = "[Event] ({}) {}".format(event.id, event.__dict__)
        self.assertEqual(string, str(event))

if __name__ == '__main__':
    unittest.main()
