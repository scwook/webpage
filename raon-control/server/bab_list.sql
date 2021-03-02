-- MySQL dump 10.16  Distrib 10.1.45-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: bab
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
-- Current Database: `bab`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `bab` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `bab`;

--
-- Table structure for table `bab_list`
--

DROP TABLE IF EXISTS `bab_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bab_list` (
  `menu` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `kind` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `tier` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bab_list`
--

LOCK TABLES `bab_list` WRITE;
/*!40000 ALTER TABLE `bab_list` DISABLE KEYS */;
INSERT INTO `bab_list` VALUES ('맥도날드','대전 대덕구 신탄진로 605','버거','low',1),('버거킹','세종특별자치시 한누리대로 1948 더스테이빌딩 1층','버거','low',1),('서브웨이','대전 유성구 관들1길 49','버거','low',1),('롯데리아','세종특별자치시 한누리대로 2009 1층','버거','low',1),('맘스터치','대전 유성구 관들1길 55','버거','low',1),('플레이버거','대전 유성구 전민로46번길 78','버거','midium',3),('프랭크버거','대전 유성구 유성대로 1728 1층','버거','low',3),('청춘식당','세종 한누리대로 2009 펠리체타워2 1층 108호','분식','low',1),('고봉민김밥','세종특별자치시 소담1로 12 지엘플렉스1상가 1층 105호','분식','low',1),('국수나무','세종특별자치시 한누리대로 2018 사이언스타워 104호','분식','low',1),('우에무라','대전 유성구 관들2길 5','일식','midium',1),('나마미돈카츠','대전 유성구 관평1로 52','일식','midium',1),('스바라시라멘','대전 유성구 테크노중앙로 54','일식','midium',1),('규카츠정','세종특별자치시 도움8로 91 3층 312호','일식','midium',2),('스시수','대전 유성구 테크노3로 65','일식','high',3),('오유미당','세종특별자치시 호려울로 45','일식','midium',2),('그남자의카츠','세종특별자치시 시청대로 219 시드니하트 503호','일식','midium',2),('소바공방','대전 유성구 엑스포로446번길 36 1층','일식','midium',2),('멘키타루','세종특별자치시 한누리대로 1948','일식','midium',2),('키햐아','세종특별자치시 금남면 금남구즉로 260 1층','일식','midium',2),('우쿠야','대전 유성구 와룡로 9 1층','일식','midium',2),('설어정','대전 유성구 문지로299번길 86-3 1층','양식','midium',2),('샤브마니아','대전 유성구 문지로299번길 94-3','일식','midium',2),('모던차이','대전 유성구 문지로299번길 86-5','중식','midium',2),('엉클부대찌개','세종특별자치시 한누리대로 1948','한식','midium',2),('라멘히로시','대전 유성구 전민로70번길 39 1층','일식','midium',3),('향미락','대전 유성구 유성대로1665번길 8-2','한식','midium',3),('메밀촌','대전 유성구 유성대로 1661-1','한식','midium',3),('좋은날','대전 유성구 엑스포로539번길 202-8','한식','midium',3),('홍기와쭈꾸미','대전 유성구 엑스포로539번길 284 1층','한식','midium',2),('마중','대전 유성구 관평1로 86','한식','midium',2),('시골촌','대전 유성구 관들4길 27','한식','midium',2),('항아리보쌈','대전 유성구 테크노중앙로 66','한식','midium',2),('황태어글탕','대전 유성구 테크노4로 94','한식','midium',2),('대복국수','대전 유성구 테크노중앙로 40','한식','midium',2),('쉑쉑버거','대전 서구 대덕대로 211 동관 1층','버거','high',4),('고등어밥상','세종특별자치시 장군면 월현윗길 38-7','한식','midium',3),('진본가','세종특별자치시 장군면 월현윗길 39-1 1층','한식','midium',3),('배부장찌개','세종특별자치시 소담1로 12','한식','midium',2),('슈니첼','대전 동구 철갑2길 16','양식','high',4),('역전우동','세종특별자치시 호려울로 51 1층 110호','한식','low',2),('세종복칼국수','세종특별자치시 금남면 신촌1길 3-4','한식','midium',2),('델루나','세종특별자치시 금남면 금남구즉로 336','간식','midium',3),('롤링핀','대전 유성구 관평2로 14','간식','high',3),('냄비요리연구소','대전 유성구 테크노중앙로 123','일식','midium',3),('아웃백','대전 유성구 테크노중앙로 123','양식','high',4),('만석장','대전 유성구 테크노중앙로 123','한식','midium',3),('도토리편백집','대전 유성구 테크노중앙로 123','일식','midium',3),('에그드랍','대전 유성구 테크노중앙로 123','간식','low',3),('계백집','대전 유성구 테크노중앙로 123','한식','midium',3),('퍼틴','대전 유성구 테크노중앙로 123','중식','midium',3),('간코','대전 유성구 테크노중앙로 123','일식','midium',3),('싸움의고수','세종특별자치시 갈매로 363 지하 1층 B114~116호','한식','low',2),('이웃','세종특별자치시 보듬4로 9 카림애비뉴1동 2층 11호','한식','midium',2),('순남시레기','세종특별자치시 보듬4로 9 카림에비뉴 2층 23호','한식','midium',2),('이삭토스트','대전 유성구 테크노3로 65 한신에스메카','버거','low',1),('숨쉬는순두부','세종특별자치시 국책연구원3로 12','한식','midium',2),('현대옥','대전 유성구 관평2로 22 1층','한식','low',2),('퀴즈노스','대전 유성구 테크노10로 31 101호','버거','low',2),('명품순두부','대전 유성구 테크노중앙로 65','한식','midium',2),('빠스타스세군도','세종특별자치시 새롬중앙로 63 세종온누리타워 1층 111호','양식','high',4),('무라텐','대전 유성구 반석동로40번길 90','일식','midium',4),('겐로쿠우동','대전 유성구 반석동로40번길 92-1','일식','midium',4),('낭만국수','대전 서구 둔산북로 36 1층 101호','한식','midium',4),('코메코메식당','세종특별자치시 한누리대로 1958 법조타운A 1층 117,118호','일식','midium',2),('이화수','대전 유성구 테크노중앙로 65 남정빌딩2차 101,102호','한식','midium',2),('초가집','세종특별자치시 한누리대로 2149 엔젤타워 2층 203,204호','한식','midium',2),('모락모락','세종특별자치시 절재로 194 중앙타운 118,119호','분식','midium',3),('시루향기','대전 유성구 테크노중앙로 54 남정빌딩 108,109,110호','한식','low',2);
/*!40000 ALTER TABLE `bab_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `history` (
  `mune` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `member` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-02 14:29:41
