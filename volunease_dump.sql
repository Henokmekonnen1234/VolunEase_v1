-- Organizations
INSERT INTO `organizations` VALUES ('GreenEarth Foundation','info@greenearth.org','$2b$12$X3S6pOp0euZyK.3uT1HkLOimyfjOeV9pYx0wS9Jn1FJv9ZfA/t3dS','555-123-4567', 'profile_image_url_1.jpg','http://www.greenearth.org','123 Nature Street, EcoCity','legal_doc_url_2.pdf','Promoting environmental sustainability.','0a1762da-18ab-44f5-9f3f-05721dcf88f5','2023-11-01 09:30:00','2023-11-01 09:30:00');

-- Events
INSERT INTO `events` VALUES ('Environmental Cleanup','city park','2023-11-15 10:00:00','2023-11-15 16:00:00','','0a1762da-18ab-44f5-9f3f-05721dcf88f5',6.0,'Join us in cleaning the city park and promoting environmental awareness.','b3cefe2c-25d4-45c6-b684-78a7e8ecb523','2023-10-28 14:30:00','2023-10-28 14:30:00');
INSERT INTO `events` VALUES ('Community Garden Planting','community garden','2023-12-05 09:00:00','2023-12-05 12:00:00','','0a1762da-18ab-44f5-9f3f-05721dcf88f5',3.0,'Help us plant new trees and flowers in the community garden.','cb4eae94-7d6c-4ae0-8eac-9a31a0b6fc6a','2023-11-15 12:45:00','2023-11-15 12:45:00');
-- Add more events for 2023

-- Volunteers
INSERT INTO `volunteers` VALUES ('Emma', 'S.', 'Johnson', 'emma.johnson@example.com', 'http://www.greenearth.org', '111-222-3333', 'Teacher', 'F', 'bc04dcee-9d63-4ae5-97f9-2b9dceb1465b', '2023-02-15 13:20:00', '2023-02-15 13:20:00');
INSERT INTO `volunteers` VALUES ('Daniel', 'K.', 'Smith', 'daniel.smith@example.com', 'http://www.greenearth.org', '777-888-9999', 'IT Specialist', 'M', 'edf8e486-24cf-4ba9-8c98-c11402a3e16e', '2023-03-10 18:00:00', '2023-03-10 18:00:00');
INSERT INTO `volunteers` VALUES ('Sophia', 'M.', 'Williams', 'sophia.williams@example.com', 'http://www.greenearth.org', '444-555-6666', 'Graphic Designer', 'F', '4e8cc502-6e83-484f-b136-264d7512791f', '2023-04-05 11:30:00', '2023-04-05 11:30:00');
-- Add more volunteers for 2023

-- Event_Students
INSERT INTO `event_students` VALUES ('b3cefe2c-25d4-45c6-b684-78a7e8ecb523','0a1762da-18ab-44f5-9f3f-05721dcf88f5');
-- Add more event students for 2023
