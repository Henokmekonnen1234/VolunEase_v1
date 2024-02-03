-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: volunease_db
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_students` (
  `event_id` varchar(60) NOT NULL,
  `volun_id` varchar(60) NOT NULL,
  `part_time` float DEFAULT NULL,
  PRIMARY KEY (`event_id`,`volun_id`),
  KEY `volun_id` (`volun_id`),
  CONSTRAINT `event_students_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `events` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `event_students_ibfk_2` FOREIGN KEY (`volun_id`) REFERENCES `volunteers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_students`
--

LOCK TABLES `event_students` WRITE;
/*!40000 ALTER TABLE `event_students` DISABLE KEYS */;
/*!40000 ALTER TABLE `event_students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events` (
  `title` varchar(255) NOT NULL,
  `place` varchar(255) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `org_id` varchar(60) NOT NULL,
  `description` varchar(500) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_date` datetime NOT NULL,
  `updated_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `description` (`description`),
  UNIQUE KEY `id` (`id`),
  KEY `org_id` (`org_id`),
  CONSTRAINT `events_ibfk_1` FOREIGN KEY (`org_id`) REFERENCES `organizations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organizations`
--

DROP TABLE IF EXISTS `organizations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_no` (`phone_no`),
  UNIQUE KEY `website` (`website`),
  UNIQUE KEY `description` (`description`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organizations`
--

LOCK TABLES `organizations` WRITE;
/*!40000 ALTER TABLE `organizations` DISABLE KEYS */;
INSERT INTO `organizations` VALUES ('Jane Smith','jane.smith@example.com','$2b$12$2gy1sN48reWEIUo7ZPjlYOR5IlHQgtNqN9H7qDoaIdVv0l2eriFR2','987-654-3210','profile_image_url_2.jpg','http://www.janesmith.com','456 Oak Avenue, Townsville','legal_doc_url_2.pdf','A brief description about Jane Smith.','b897c92f-3281-424f-b3cf-3119913f505e','2024-02-03 10:07:59','2024-02-03 10:07:59'),('John Doe','john.doe@example.com','$2b$12$r2l8TcYyRs1QRquehK19z.YnVcaxnVlV.NzOq8za030dcmkug1nRa','123-456-7890','profile_image_url_1.jpg','http://www.johndoe.com','123 Main Street, Cityville','legal_doc_url_1.pdf','A brief description about John Doe.','dc46bb1f-c49b-4199-953a-0ff7c51a2d31','2024-02-03 10:07:05','2024-02-03 10:07:05');
/*!40000 ALTER TABLE `organizations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `volunteers`
--

DROP TABLE IF EXISTS `volunteers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_no` (`phone_no`),
  UNIQUE KEY `id` (`id`),
  KEY `org_id` (`org_id`),
  CONSTRAINT `volunteers_ibfk_1` FOREIGN KEY (`org_id`) REFERENCES `organizations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `volunteers`
--

LOCK TABLES `volunteers` WRITE;
/*!40000 ALTER TABLE `volunteers` DISABLE KEYS */;
INSERT INTO `volunteers` VALUES ('Alice','M.','Williams','alice.williams@example.com','profile_image_url_4.jpg','111-222-3333','Graphic Designer','F','dc46bb1f-c49b-4199-953a-0ff7c51a2d31','0c13f6b9-4937-420e-9c6f-2de3d108a3ea','2024-02-03 10:15:37','2024-02-03 10:15:37'),('David','J.','Anderson','david.anderson@example.com',NULL,'333-444-5555','Sales Representative','M','b897c92f-3281-424f-b3cf-3119913f505e','32971f31-8338-43cd-bc7d-bc301f8d0217','2024-02-03 10:16:57','2024-02-03 10:16:57'),('Charlie','L.','Davis','charlie.davis@example.com',NULL,'444-555-6666','Project Manager','M','dc46bb1f-c49b-4199-953a-0ff7c51a2d31','4080d760-675e-4535-98b7-d41ec881dd61','2024-02-03 10:15:57','2024-02-03 10:15:57'),('Frank','P.','Young','frank.young@example.com','profile_image_url_7.jpg','999-000-1111','Architect','M','b897c92f-3281-424f-b3cf-3119913f505e','6ca5370e-c6ae-430c-ba28-94969d8906e6','2024-02-03 10:17:21','2024-02-03 10:17:21'),('Grace','N.','Thomas','grace.thomas@example.com','profile_image_url_6.jpg','666-777-8888','Data Analyst','F','b897c92f-3281-424f-b3cf-3119913f505e','7826806d-18b3-4189-ae64-7fe3639ff455','2024-02-03 10:17:09','2024-02-03 10:17:09'),('Eva','K.','Miller','eva.miller@example.com','profile_image_url_5.jpg','777-888-9999','HR Specialist','F','b897c92f-3281-424f-b3cf-3119913f505e','909acf75-30b1-4ad1-a718-e5648ef7a956','2024-02-03 10:16:45','2024-02-03 10:16:45'),('Helen','R.','Moore','helen.moore@example.com',NULL,'222-333-4444','Customer Support','F','b897c92f-3281-424f-b3cf-3119913f505e','a68711a1-4175-4624-9474-d7d4442d0ff1','2024-02-03 10:17:33','2024-02-03 10:17:33'),('Jane','A.','Smith','jane.smith@example.com','profile_image_url_2.jpg','987-654-3210','Marketing Specialist','F','dc46bb1f-c49b-4199-953a-0ff7c51a2d31','acaec3e2-980f-4b01-966b-41fbe1b45e8b','2024-02-03 10:14:37','2024-02-03 10:14:37'),('Bob','E.','Johnson','bob.johnson@example.com','profile_image_url_3.jpg','555-123-4567','Accountant','M','dc46bb1f-c49b-4199-953a-0ff7c51a2d31','cf4cd905-fb5f-4857-9fa5-f9bf30458949','2024-02-03 10:15:19','2024-02-03 10:15:19'),('John','Robert','Doe','john.doe@example.com','profile_image_url_1.jpg','123-456-7890','Software Engineer','M','dc46bb1f-c49b-4199-953a-0ff7c51a2d31','d648dfcc-f082-4bf3-a09c-34ac130427a9','2024-02-03 10:14:07','2024-02-03 10:14:07');
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

-- Dump completed on 2024-02-03 13:40:55
