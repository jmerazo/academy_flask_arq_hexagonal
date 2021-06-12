-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         5.6.51-log - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para academy_flask
CREATE DATABASE IF NOT EXISTS `academy_flask` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `academy_flask`;

-- Volcando estructura para tabla academy_flask.assistances
CREATE TABLE IF NOT EXISTS `assistances` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `session_id` int(11) NOT NULL,
  `assistance` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla academy_flask.assistances: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `assistances` DISABLE KEYS */;
REPLACE INTO `assistances` (`id`, `student_id`, `session_id`, `assistance`) VALUES
	(18, 12, 6, 1),
	(19, 12, 6, 1),
	(20, 12, 6, 1),
	(21, 12, 9, 1),
	(22, 12, 10, 1),
	(23, 12, 11, 1),
	(24, 12, 10, 1);
/*!40000 ALTER TABLE `assistances` ENABLE KEYS */;

-- Volcando estructura para tabla academy_flask.courses
CREATE TABLE IF NOT EXISTS `courses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `semester` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla academy_flask.courses: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
REPLACE INTO `courses` (`id`, `name`, `semester`) VALUES
	(8, 'Base de datos I', 6),
	(9, 'Base de datos II', 9),
	(10, 'Inteligencia Artificial', 10);
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;

-- Volcando estructura para tabla academy_flask.sessions
CREATE TABLE IF NOT EXISTS `sessions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `course_id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla academy_flask.sessions: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;
REPLACE INTO `sessions` (`id`, `date`, `start_time`, `end_time`, `course_id`) VALUES
	(10, '2021-05-03', '06:30:00', '10:45:00', 'Base de datos II'),
	(11, '2021-05-03', '06:30:00', '10:45:00', 'Base de datos I');
/*!40000 ALTER TABLE `sessions` ENABLE KEYS */;

-- Volcando estructura para tabla academy_flask.students
CREATE TABLE IF NOT EXISTS `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(45) NOT NULL,
  `names` varchar(45) NOT NULL,
  `lastnames` varchar(45) NOT NULL,
  `phone` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `semester` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `identificacion_estudiante_UNIQUE` (`uid`),
  UNIQUE KEY `email_estudiante_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla academy_flask.students: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
REPLACE INTO `students` (`id`, `uid`, `names`, `lastnames`, `phone`, `email`, `semester`) VALUES
	(12, '1120876453', 'Andrea Liliana', 'Baeza Saenz', '3203876543', 'andi1994sol@gmail.com', 10),
	(14, '1321321321', 'Camila', 'Gozzu', '3179875645', 'camila@gmail.com', 10),
	(19, '1123456712', 'Thiago', 'Baeza', '3179875645', 'thiagobaezam@gmail.com', 10),
	(21, '1124356234', 'Sara', 'Fajardo', '3179875645', 'sara@gmail.com', 10),
	(23, '96789654', 'Andrea', 'Lozano', '3179875645', 'andrealozano98@gmail.com', 9);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
