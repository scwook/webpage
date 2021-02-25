-- MySQL dump 10.16  Distrib 10.1.45-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: shift
-- ------------------------------------------------------
-- Server version	10.1.45-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `shift`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `shift` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `shift`;

--
-- Table structure for table `detail`
--

DROP TABLE IF EXISTS `detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `detail` (
  `schedule` int(11) DEFAULT NULL,
  `todo` varchar(256) DEFAULT NULL,
  KEY `schedule` (`schedule`),
  CONSTRAINT `detail_ibfk_1` FOREIGN KEY (`schedule`) REFERENCES `schedule` (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detail`
--

LOCK TABLES `detail` WRITE;
/*!40000 ALTER TABLE `detail` DISABLE KEYS */;
INSERT INTO `detail` VALUES (1,'ECR Repeatability Test'),(1,'ECR Beam Current Test'),(2,'Beam Transport to LEBT'),(2,'Beam Transport to MEBT'),(3,'Timing and FPS Interlock Test'),(4,'Pulse Beam Test'),(4,'250us Pulse Beam to MEBT'),(4,'Beam Steering Test'),(5,'Main Control Room Test'),(7,'RFQ-MEBT Integration Test');
/*!40000 ALTER TABLE `detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule`
--

DROP TABLE IF EXISTS `schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schedule` (
  `number` int(11) NOT NULL AUTO_INCREMENT,
  `fromDate` varchar(255) NOT NULL,
  `toDate` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule`
--

LOCK TABLES `schedule` WRITE;
/*!40000 ALTER TABLE `schedule` DISABLE KEYS */;
INSERT INTO `schedule` VALUES (1,'2021-01-05','2021-01-06','Beam Commissioning'),(2,'2021-01-11','2021-01-12','Beam Commissioning'),(3,'2021-01-19','2021-01-19','Main Control Test'),(4,'2021-01-25','2021-01-27','Beam Commissioning'),(5,'2021-02-09','2021-02-09','Beam Commissioning'),(6,'2021-01-01','2021-01-02','Beam Test'),(7,'2021-02-23','2021-02-23','Beam Test');
/*!40000 ALTER TABLE `schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shifter`
--

DROP TABLE IF EXISTS `shifter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shifter` (
  `schedule` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `team` varchar(256) DEFAULT NULL,
  `desk` int(11) DEFAULT NULL,
  `seat` int(11) DEFAULT NULL,
  `leader` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shifter`
--

LOCK TABLES `shifter` WRITE;
/*!40000 ALTER TABLE `shifter` DISABLE KEYS */;
INSERT INTO `shifter` VALUES (1,'Chung, Yeon Sei','Beam Transport',4,3,1),(1,'Kim, Gi Dong','Beam Transport',4,0,0),(1,'Kwon, Jangwon','Beam Transport',4,1,0),(1,'Lim, EunHun','Beam Transport',4,2,0),(1,'Kim, Hyung Jin','Beam Transport',4,0,0),(1,'Heo, JeongIl','Beam ransport',4,4,0),(1,'Mun, Seokho','Beam Transport',4,5,0),(1,'Park, Burm Sik','Beam Transport',2,6,0),(1,'Son, Changwook','Accelerator Control',1,1,0),(1,'Park, MiJeong','Accelerator Control',1,2,0),(1,'Lee, SangIl','Accelerator Control',1,3,0),(1,'Seol, Kyung Tae','SCRF',3,1,0),(1,'Lee, DoYoon','SCRF',3,2,0),(1,'Son, KiTaek','SCRF',3,3,0),(2,'Chung, Yeon Sei','Beam Transport',4,3,1),(2,'Kim, Gi Dong','Beam Transport',4,0,0),(2,'Kwon, Jangwon','Beam Transport',4,1,0),(2,'Lim, EunHun','Beam Transport',4,2,0),(2,'Kim, Hyung Jin','Beam Transport',4,0,0),(2,'Heo, JeongIl','Beam ransport',4,4,0),(2,'Mun, Seokho','Beam Transport',4,5,0),(2,'Park, Burm Sik','Beam Transport',2,6,0),(2,'Son, Changwook','Accelerator Control',1,1,0),(2,'Park, MiJeong','Accelerator Control',1,2,0),(2,'Lee, SangIl','Accelerator Control',1,3,0),(2,'Seol, Kyung Tae','SCRF',3,1,0),(2,'Lee, DoYoon','SCRF',3,2,0),(2,'Son, KiTaek','SCRF',3,3,0),(3,'Son, Changwook','Accelerator Control',1,1,0),(3,'Lee, SangIl','Accelerator Control',1,3,1),(3,'Choi, Yong Jun','Accelerator Control',1,2,0),(4,'Chung, Yeon Sei','Beam Transport',4,3,1),(4,'Kim, Gi Dong','Beam Transport',4,0,0),(4,'Kwon, Jangwon','Beam Transport',4,1,0),(4,'Lim, EunHun','Beam Transport',4,2,0),(4,'Kim, Hyung Jin','Beam Transport',4,0,0),(4,'Heo, JeongIl','Beam ransport',4,4,0),(4,'Mun, Seokho','Beam Transport',4,5,0),(4,'Park, Burm Sik','Beam Transport',2,6,0),(4,'Son, Changwook','Accelerator Control',1,1,0),(4,'Park, MiJeong','Accelerator Control',1,2,0),(4,'Lee, SangIl','Accelerator Control',1,3,0),(4,'Seol, Kyung Tae','SCRF',3,1,0),(4,'Lee, DoYoon','SCRF',3,2,0),(4,'Son, KiTaek','SCRF',3,3,0),(5,'Chung, Yeon Sei','Beam Transport',4,3,1),(5,'Kim, Gi Dong','Beam Transport',4,0,0),(5,'Woo, Hyung Joo','Beam Transport',4,0,0),(5,'Kwon, Jangwon','Beam Transport',4,1,0),(5,'Lim, EunHun','Beam Transport',4,2,0),(5,'Kim, Hyung Jin','Beam Transport',4,0,0),(5,'Heo, JeongIl','Beam ransport',4,4,0),(5,'Mun, Seokho','Beam Transport',4,5,0),(5,'Park, MiJeong','Accelerator Control',1,2,0),(7,'Chung, Yeon Sei','Beam Transport',4,3,1),(7,'Kim Gi Dong','Beam Transport',4,0,0),(7,'Kwon, Jangwon','Beam Transport',4,1,0),(7,'Lim, EunHun','Beam Transport',4,2,0),(7,'Kim, Hyung Jin','Beam Transport',4,0,0),(7,'Heo, JeongIl','Beam Transport',4,4,0),(7,'Mun, Seokho','Beam Transport',4,5,0),(7,'Park, Burm Sik','Beam Transport',2,6,0),(7,'Son, Changwook','Accelerator Control',1,1,0);
/*!40000 ALTER TABLE `shifter` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-25 13:36:54
