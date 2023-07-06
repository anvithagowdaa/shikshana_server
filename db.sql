/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - shikshana
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`shikshana` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `shikshana`;

/*Table structure for table `assignmentdata` */

DROP TABLE IF EXISTS `assignmentdata`;

CREATE TABLE `assignmentdata` (
  `id` int(255) NOT NULL auto_increment,
  `filename` varchar(255) default NULL,
  `titleofam` varchar(255) default NULL,
  `standard` varchar(255) default NULL,
  `timestamp` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `assignmentdata` */

insert  into `assignmentdata`(`id`,`filename`,`titleofam`,`standard`,`timestamp`) values (1,'static/files/assignment/IRJET-V9I3216.pdf','sdfsdf','1st','16-05-2023, 11:34:42'),(2,'static/files/assignment/latency.png','asdasd','2nd','16-05-2023, 11:35:03'),(3,'static/files/assignment/105-land.docx','adasdasd','1st','17-05-2023, 16:43:23'),(4,'static/files/assignment/AIarch.png','sdfsdfsdf','1st','17-05-2023, 16:43:49'),(5,'static/files/assignment/043-flowchart.png','sdfsdf','2nd','17-05-2023, 16:44:17'),(6,'static/files/assignment/IRJET-V9I3216.pdf','asdasdasd','2nd','17-05-2023, 16:44:41'),(7,'static/files/assignment/Implementation.docx','Subject1','1st','24-05-2023, 15:13:18'),(8,'https://forms.gle/8epSuBBvAgW2mqn49','fee form','1st','10-06-2023, 18:19:22'),(9,'https://docs.google.com/forms/d/e/1FAIpQLSeRL37COL9i3wxI1YbijCppXav9jSlT9fgAcjeG0aBOyK1jAA/viewform?usp=sf_link','Google','1st','12-06-2023, 10:17:06');

/*Table structure for table `chatdata` */

DROP TABLE IF EXISTS `chatdata`;

CREATE TABLE `chatdata` (
  `id` int(255) NOT NULL auto_increment,
  `chat` longtext,
  `username` varchar(255) default NULL,
  `std` varchar(255) default NULL,
  `time` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chatdata` */

insert  into `chatdata`(`id`,`chat`,`username`,`std`,`time`) values (1,'Hi how are you?','a','1st','12:32'),(2,'I am fine. What about you?','d','4th','12:33'),(3,'Kasa ahes','a','1st','14:05'),(4,'Mast ahe mi tu ?!','d','4th','14:30'),(5,'How old you are?','a','1st','14:32'),(6,'23 ','d','4th','14:33'),(7,'Your age','d','4th','14:33'),(8,'no no','d','4th','14:33'),(9,'Yash','a','1st','15:41'),(10,'Kasa ahes','a','1st','15:50'),(11,'ertert','a','1st','16:16'),(12,'Mayur kasa ahes','b','2nd','16:32'),(13,'Fine','a','1st','16:33'),(14,'Yash here !','yash','1st','16:49'),(15,'Fine now !','a','1st','17:56'),(16,'me admin ahe !','admin','none','18:09'),(17,'Baki sab thik','admin','none','18:26'),(18,'Kasa ahes','admin','none','18:27'),(19,'Mast ahe','a','1st','18:30'),(20,'Tu kasa ahes Admin','c','3rd','18:31'),(21,'Chan','admin','none','18:31'),(22,'Nice','a','1st','18:31'),(23,'Bye','a','1st','18:32'),(24,'Good morning Guys !','admin','none','10:38'),(25,'Good morning Teacher !','a','1st','10:39'),(26,'Good morning ?','c','3rd','10:39');

/*Table structure for table `elearningdata` */

DROP TABLE IF EXISTS `elearningdata`;

CREATE TABLE `elearningdata` (
  `id` int(255) NOT NULL auto_increment,
  `link` longtext,
  `filename` varchar(255) default NULL,
  `titleofam` varchar(255) default NULL,
  `standard` varchar(255) default NULL,
  `timestamp` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `elearningdata` */

insert  into `elearningdata`(`id`,`link`,`filename`,`titleofam`,`standard`,`timestamp`) values (1,'https://www.youtube.com/embed/MbLpZXIZZOg','static/files/elearning/105-land.docx','Yash','1st','18-05-2023, 18:06:26'),(2,'https://www.youtube.com/embed/CsOsmgUmT9U','static/files/elearning/eventlogo.png','dfgdfg','2nd','18-05-2023, 18:07:00'),(3,'https://www.youtube.com/embed/I18ba3MuaiY','static/files/elearning/Blockchain_for_Electronic_Health_Records.docx','Elearning','1st','24-05-2023, 15:14:32');

/*Table structure for table `submitedassignment` */

DROP TABLE IF EXISTS `submitedassignment`;

CREATE TABLE `submitedassignment` (
  `id` int(255) NOT NULL auto_increment,
  `username` varchar(255) default NULL,
  `standard` varchar(255) default NULL,
  `title` varchar(255) default NULL,
  `assignmentpath` varchar(255) default NULL,
  `marksobt` varchar(255) default '0',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `submitedassignment` */

insert  into `submitedassignment`(`id`,`username`,`standard`,`title`,`assignmentpath`,`marksobt`) values (1,'b','2nd','asdasd','static/files/submittedAssignment/AES_S-BOX_KEY_GENERATION.pdf','22'),(2,'g','2nd','asdasd','static/files/submittedAssignment/1241-768x591.png','0'),(3,'g','2nd','asdasdasd','static/files/submittedAssignment/eventlogo.png','55'),(4,'b','2nd','sdfsdf','static/files/submittedAssignment/buslogo.png','95'),(5,'a','1st','adasdasd','static/files/submittedAssignment/latency.png','0'),(6,'b','2nd','asdasdasd','static/files/submittedAssignment/synopsis_format.docx','100'),(7,'a','1st','Subject1','static/files/submittedAssignment/land.docx','90'),(8,'a','1st','Google','Marked','65'),(9,'yash','1st','fee form','Marked','95'),(10,'a','1st','fee form','Marked','1000');

/*Table structure for table `syllabusdata` */

DROP TABLE IF EXISTS `syllabusdata`;

CREATE TABLE `syllabusdata` (
  `id` int(255) NOT NULL auto_increment,
  `filename` varchar(255) default NULL,
  `titleofs` varchar(255) default NULL,
  `standard` varchar(255) default NULL,
  `timestamp` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `syllabusdata` */

insert  into `syllabusdata`(`id`,`filename`,`titleofs`,`standard`,`timestamp`) values (1,'static/files/syllabus/slider-image-1.jpg','Yash Salvi','1st','16-05-2023, 11:34:15'),(2,'static/files/syllabus/img-1.jpg','5th sem','1st','24-05-2023, 15:12:43');

/*Table structure for table `timetabledata` */

DROP TABLE IF EXISTS `timetabledata`;

CREATE TABLE `timetabledata` (
  `id` int(255) NOT NULL auto_increment,
  `filename` varchar(255) default NULL,
  `titleoftt` varchar(255) default NULL,
  `standard` varchar(255) default NULL,
  `timestamp` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `timetabledata` */

insert  into `timetabledata`(`id`,`filename`,`titleoftt`,`standard`,`timestamp`) values (1,'static/files/timetable/property1.jpg','Yash','1st','16-05-2023, 11:24:29'),(2,'static/files/timetable/CamScanner_04-06-2022_10.10.pdf','Yash Salvi','2nd','16-05-2023, 11:25:12'),(3,'static/files/timetable/heart_disease_Blackbook_Final.docx','yyyyy','1st','16-05-2023, 15:59:54'),(4,'static/files/timetable/bruce-mars.jpg','Exam','1st','24-05-2023, 15:12:01');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(255) NOT NULL auto_increment,
  `username` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `mobile` varchar(255) default NULL,
  `password` varchar(255) default NULL,
  `standard` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`id`,`username`,`email`,`mobile`,`password`,`standard`) values (1,'a','y@gmail.com','9372914050','a','1st'),(2,'b','yashsalvi1999@gmail.com','9372914050','b','2nd'),(3,'c','yashsalvi1999@gmail.com','9930090883','c','3rd'),(4,'d','yashsalvi1999@gmail.com','9930090883','d','4th'),(5,'e','yashsalvi1999@gmail.com','9930090883','e','5th'),(6,'g','yashsalvi1999@gmail.com','9930090883','g','2nd'),(7,'yash','yashsalvi1999@gmail.com','9372914050','y','1st');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
