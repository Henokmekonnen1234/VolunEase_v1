-- MySQL dump 10.13  Distrib 5.7.42, for Linux (x86_64)
--
-- Host: localhost    Database: volunease_db
-- ------------------------------------------------------
-- Server version	5.7.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `event_students`
--

DROP TABLE IF EXISTS `event_students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event_students` (
  `event_id` varchar(60) NOT NULL,
  `volun_id` varchar(60) NOT NULL,
  PRIMARY KEY (`event_id`,`volun_id`),
  KEY `volun_id` (`volun_id`),
  CONSTRAINT `event_students_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `events` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `event_students_ibfk_2` FOREIGN KEY (`volun_id`) REFERENCES `volunteers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_students`
--

LOCK TABLES `event_students` WRITE;
/*!40000 ALTER TABLE `event_students` DISABLE KEYS */;
INSERT INTO `event_students` VALUES ('19c03232-6bda-4085-b505-5027ab831048','3fbb375a-51df-4c5a-9ce4-4f21baef6a23'),('a3119c55-7990-4758-af19-4631e1668bc1','3fbb375a-51df-4c5a-9ce4-4f21baef6a23'),('19c03232-6bda-4085-b505-5027ab831048','562211a4-7326-4c54-856d-d0064b2ab0e1'),('a3119c55-7990-4758-af19-4631e1668bc1','562211a4-7326-4c54-856d-d0064b2ab0e1'),('19c03232-6bda-4085-b505-5027ab831048','a35538ad-70ce-47ee-a2b1-b6c30bbdec52'),('b94ecb8c-a244-4c2c-b14a-44e325c18731','a35538ad-70ce-47ee-a2b1-b6c30bbdec52'),('207a5bee-8cd6-4adb-b441-e45da22da133','b1a5eecc-2f84-4a87-97e8-e6695c04b16a'),('d6e1a7e0-7528-4eb4-8312-1d95a6821347','c25810a0-a109-499b-87eb-9804754565bc'),('d6e1a7e0-7528-4eb4-8312-1d95a6821347','cfa7bd0c-6717-4c7d-b385-6c75877d89b9'),('207a5bee-8cd6-4adb-b441-e45da22da133','e1077263-74d2-4423-83a3-2b1220854e85');
/*!40000 ALTER TABLE `event_students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events` (
  `title` varchar(255) NOT NULL,
  `place` varchar(255) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `org_id` varchar(60) NOT NULL,
  `part_time` float DEFAULT NULL,
  `description` varchar(1000) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_date` datetime NOT NULL,
  `updated_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `org_id` (`org_id`),
  CONSTRAINT `events_ibfk_1` FOREIGN KEY (`org_id`) REFERENCES `organizations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES ('Community Cleanup Food Drive ','addis ababa, Ethiopia','2024-02-21 09:59:00','2024-02-21 21:01:00','','bc04dcee-9d63-4ae5-97f9-2b9dceb1465b',11.0333,'Description: Description: Join us for a community cleanup event!','19c03232-6bda-4085-b505-5027ab831048','2024-02-10 15:58:10','2024-02-10 15:58:10'),('Food Drive','addis Ababa, Ethiopia','2024-02-20 12:00:00','2024-02-20 18:00:00','','bc04dcee-9d63-4ae5-97f9-2b9dceb1465b',21600,'Description: Help us collect food for those in need!','207a5bee-8cd6-4adb-b441-e45da22da133','2024-02-05 14:21:41','2024-02-05 14:21:41'),('Workshop on Environmental Awareness','Community Hall','2024-02-11 09:22:00','2024-02-11 23:58:00','C:\\fakepath\\Screenshot from 2024-02-06 18-01-40.png','4e8cc502-6e83-484f-b136-264d7512791f',14.6,'Learn about environmental issues and conservation!','a3119c55-7990-4758-af19-4631e1668bc1','2024-02-10 15:54:11','2024-02-10 15:54:11'),('Tech Conference 2024','Convention Center','2024-02-13 07:24:00','2024-02-13 11:00:00','C:\\fakepath\\newwww.png','bc04dcee-9d63-4ae5-97f9-2b9dceb1465b',3.6,'Exciting tech conference featuring keynote speakers, workshops, and networking opportunities.','b94ecb8c-a244-4c2c-b14a-44e325c18731','2024-02-12 10:19:32','2024-02-12 10:19:32'),('Tree Planting','Greenbelt Area','2024-02-16 00:29:00','2024-02-20 13:30:00','C:\\fakepath\\newwww.png','bc04dcee-9d63-4ae5-97f9-2b9dceb1465b',109.017,'Contribute to the environment by participating in our tree planting event. Let\'s make our city greener together!','d6e1a7e0-7528-4eb4-8312-1d95a6821347','2024-02-11 18:27:05','2024-02-11 18:27:05');
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organizations`
--

DROP TABLE IF EXISTS `organizations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `organizations` (
  `name` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(255) NOT NULL,
  `phone_no` varchar(30) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `website` varchar(128) NOT NULL,
  `address` varchar(255) NOT NULL,
  `legal_document` varchar(255) DEFAULT NULL,
  `description` varchar(1000) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_date` datetime NOT NULL,
  `updated_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organizations`
--

LOCK TABLES `organizations` WRITE;
/*!40000 ALTER TABLE `organizations` DISABLE KEYS */;
INSERT INTO `organizations` VALUES ('John Doe','john.doe@example.com','$2b$12$6LqSPDdooN2aLCjDUDEBiOO.PDVL7VfHF.42Ev9cGzC/.NqhRzr2G','123-456-7890','profile_image_url_1.jpg','http://www.johndoe.com','123 Main Street, Cityville','legal_doc_url_1.pdf','A brief description about John Doe.','4e8cc502-6e83-484f-b136-264d7512791f','2024-02-05 09:56:34','2024-02-05 09:56:34'),('CareEplepsiy Ethiopia','bob.johnson@example.com','$2b$12$iIVcihpZt8iYT/KIyzn6A.nkLlCWwszXMyGtBjIbt5IYlpdn6Aq9m','555-123-4567','','http://127.0.0.1:5000/register','dsfnaewfhwefuhwefuihwie','','The @app.route decorator that I used to declare this view function looks a little bit different than the previous ones. In this case I have a dynamic component in it, which is indicated as the <username> URL component that is surrounded by < and >.','bc04dcee-9d63-4ae5-97f9-2b9dceb1465b','2024-02-08 20:43:25','2024-02-08 20:43:25'),('Mekedoniya','jane.smith@example.com','$2b$12$ZDZcgylpZ6FmoKb8cxXVE.1K6ALzQQshgIB8PH1CqzAN3WLfnAw6C','987-654-3210','','http://www.janesmith.com','456 Oak Avenue, Townsville','','The @app.route decorator that I used to declare this view function looks a little bit different than the previous ones. In this case I have a dynamic component in it, which is indicated as the <username> URL component that is surrounded by < and >. When a route has a dynamic component, Flask will accept any text in that portion of the URL, and will invoke the view function with the actual text as an argument. For example, if the client browser requests URL /user/susan, the view function is going to be called with the argument username set to \'susan\'. This view function is only going to be accessible to logged-in users, so I have added the @login_required decorator from Flask-Login.','edf8e486-24cf-4ba9-8c98-c11402a3e16e','2024-02-05 09:56:57','2024-02-05 09:56:57');
/*!40000 ALTER TABLE `organizations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `volunteers`
--

DROP TABLE IF EXISTS `volunteers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `volunteers` (
  `first_name` varchar(255) NOT NULL,
  `mid_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(128) NOT NULL,
  `image` varchar(255) DEFAULT NULL,
  `phone_no` varchar(30) NOT NULL,
  `occupation` varchar(50) NOT NULL,
  `gender` varchar(2) NOT NULL,
  `org_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_date` datetime NOT NULL,
  `updated_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `org_id` (`org_id`),
  CONSTRAINT `volunteers_ibfk_1` FOREIGN KEY (`org_id`) REFERENCES `organizations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `volunteers`
--

LOCK TABLES `volunteers` WRITE;
/*!40000 ALTER TABLE `volunteers` DISABLE KEYS */;
INSERT INTO `volunteers` VALUES ('Charlie','L.','Davis','charlie.davis@example.com','C:\\fakepath\\images_1.jpeg','444-555-6666','Project Manager','M','4e8cc502-6e83-484f-b136-264d7512791f','0a1762da-18ab-44f5-9f3f-05721dcf88f5','2024-02-10 15:45:14','2024-02-10 15:45:14'),('David','henok','Anderson','david.anderson@example.com','C:\\fakepath\\newwww.png','333-444-5555','Project Manager','M','4e8cc502-6e83-484f-b136-264d7512791f','0efaedfc-0ea3-4456-af6c-0f78f61283b7','2024-02-10 15:52:50','2024-02-10 15:52:50'),('Alice','M.','Williams','alice.williams@example.com','C:\\fakepath\\Screenshot from 2024-02-06 18-01-40.png','111-222-3333','Graphic Designer','F','4e8cc502-6e83-484f-b136-264d7512791f','3fbb375a-51df-4c5a-9ce4-4f21baef6a23','2024-02-10 15:43:34','2024-02-10 15:43:34'),('Frank','P.','Young','frank.young@example.com','C:\\fakepath\\newwww.png','999-000-1111','Architect','M','4e8cc502-6e83-484f-b136-264d7512791f','562211a4-7326-4c54-856d-d0064b2ab0e1','2024-02-08 21:35:51','2024-02-08 21:35:51'),('Bob','E.','Johnson','bob.johnson@example.com','C:\\fakepath\\Screenshot from 2024-02-06 18-01-40.png','555-123-4567','Accountant','M','4e8cc502-6e83-484f-b136-264d7512791f','7926c72c-2936-41bb-a5d1-7eb4cb9063e1','2024-02-10 15:40:04','2024-02-10 15:40:04'),('John','Robert','Doe','john.doe@example.com','C:\\fakepath\\newwww.png','123-456-7890','Accountant','M','bc04dcee-9d63-4ae5-97f9-2b9dceb1465b','a35538ad-70ce-47ee-a2b1-b6c30bbdec52','2024-02-12 10:11:35','2024-02-12 10:11:35'),('John','Robert','Doe','john.doe@example.com','profile_image_url_1.jpg','123-456-7890','Software Engineer','M','4e8cc502-6e83-484f-b136-264d7512791f','b1a5eecc-2f84-4a87-97e8-e6695c04b16a','2024-02-05 12:01:43','2024-02-05 12:01:43'),('Grace','N.','Thomas','grace.thomas@example.com','C:\\fakepath\\Screenshot from 2024-02-06 18-01-40.png','666-777-8888','Data Analyst','F','bc04dcee-9d63-4ae5-97f9-2b9dceb1465b','c25810a0-a109-499b-87eb-9804754565bc','2024-02-11 18:05:09','2024-02-11 18:05:09'),('Helen','R.','Moore','helen.moore@example.com','C:\\fakepath\\newwww.png','222-333-4444','Customer Support','F','bc04dcee-9d63-4ae5-97f9-2b9dceb1465b','cfa7bd0c-6717-4c7d-b385-6c75877d89b9','2024-02-11 18:02:43','2024-02-11 18:02:43'),('Eva','K.','Miller','eva.miller@example.com','C:\\fakepath\\images.jpeg','777-888-9999','HR Specialist','F','4e8cc502-6e83-484f-b136-264d7512791f','d9a51774-9994-41ad-9cab-c49e7bc99801','2024-02-10 15:49:48','2024-02-10 15:49:48'),('Jane','A.','Smith','jane.smith@example.com','profile_image_url_2.jpg','987-654-3210','Marketing Specialist','F','4e8cc502-6e83-484f-b136-264d7512791f','e1077263-74d2-4423-83a3-2b1220854e85','2024-02-05 12:03:15','2024-02-05 12:03:15');
/*!40000 ALTER TABLE `volunteers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-13 16:34:47
