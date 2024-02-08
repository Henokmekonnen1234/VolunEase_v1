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
INSERT INTO `event_students` VALUES ('207a5bee-8cd6-4adb-b441-e45da22da133','b1a5eecc-2f84-4a87-97e8-e6695c04b16a'),('682c723e-51a0-4cc8-876d-999bde5180e2','b1a5eecc-2f84-4a87-97e8-e6695c04b16a'),('207a5bee-8cd6-4adb-b441-e45da22da133','e1077263-74d2-4423-83a3-2b1220854e85'),('682c723e-51a0-4cc8-876d-999bde5180e2','e1077263-74d2-4423-83a3-2b1220854e85');
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
  `description` varchar(500) NOT NULL,
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
INSERT INTO `events` VALUES ('Food Drive','Community Center','2024-02-20 12:00:00','2024-02-20 18:00:00','food_drive_image.jpg','4e8cc502-6e83-484f-b136-264d7512791f',21600,'Help us collect food for those in need!','207a5bee-8cd6-4adb-b441-e45da22da133','2024-02-05 14:21:41','2024-02-05 14:21:41'),('Food Drive','Community Center','2024-02-20 12:00:00','2024-02-20 18:00:00','food_drive_image.jpg','4e8cc502-6e83-484f-b136-264d7512791f',6,'Help us collect food for those in need!','682c723e-51a0-4cc8-876d-999bde5180e2','2024-02-05 14:23:38','2024-02-05 14:23:38');
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
  `description` varchar(500) NOT NULL,
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
INSERT INTO `organizations` VALUES ('John Doe','john.doe@example.com','$2b$12$6LqSPDdooN2aLCjDUDEBiOO.PDVL7VfHF.42Ev9cGzC/.NqhRzr2G','123-456-7890','profile_image_url_1.jpg','http://www.johndoe.com','123 Main Street, Cityville','legal_doc_url_1.pdf','A brief description about John Doe.','4e8cc502-6e83-484f-b136-264d7512791f','2024-02-05 09:56:34','2024-02-05 09:56:34'),('Jane Smith','jane.smith@example.com','$2b$12$PllpJKqLpL2LIUtPODd2Z.7BmQzgeOo6AvDDNpBjUf5Kn8fqe3KZ.','987-654-3210','profile_image_url_2.jpg','http://www.janesmith.com','456 Oak Avenue, Townsville','legal_doc_url_2.pdf','A brief description about Jane Smith.','edf8e486-24cf-4ba9-8c98-c11402a3e16e','2024-02-05 09:56:57','2024-02-05 09:56:57');
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
INSERT INTO `volunteers` VALUES ('John','Robert','Doe','john.doe@example.com','profile_image_url_1.jpg','123-456-7890','Software Engineer','M','4e8cc502-6e83-484f-b136-264d7512791f','b1a5eecc-2f84-4a87-97e8-e6695c04b16a','2024-02-05 12:01:43','2024-02-05 12:01:43'),('Jane','A.','Smith','jane.smith@example.com','profile_image_url_2.jpg','987-654-3210','Marketing Specialist','F','4e8cc502-6e83-484f-b136-264d7512791f','e1077263-74d2-4423-83a3-2b1220854e85','2024-02-05 12:03:15','2024-02-05 12:03:15');
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

-- Dump completed on 2024-02-08 11:28:21
