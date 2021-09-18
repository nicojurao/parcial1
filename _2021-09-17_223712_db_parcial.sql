/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/ db_parcial /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE db_parcial;

DROP TABLE IF EXISTS users;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `nombre` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contraseña` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
INSERT INTO users(id,nombre,email,contraseña) VALUES(1,'NICOLAS','NICOJURAO@GMAIL.COM','Nicojur@o98'),(2,'joselito','josefo.marino@es','ratata123'),(3,'camilin','jortajota@.es','33333'),(4,'nico','nicojurao@gmail.com','nicojurao98');