
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


CREATE TABLE IF NOT EXISTS `contract` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `identifier` varchar(50) NOT NULL,
  `contractor_title` varchar(250) NOT NULL,
  `value` int(11) NOT NULL DEFAULT '0',
  `begin_date` date NOT NULL,
  `end_date` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`contractor_title`),
  UNIQUE KEY `contract_num` (`identifier`),
  KEY `begin_date_end_date` (`begin_date`,`end_date`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='Directory of contractors who maintaining equipment.';


/*!40000 ALTER TABLE `contract` DISABLE KEYS */;
INSERT INTO `contract` (`id`, `identifier`, `contractor_title`, `value`, `begin_date`, `end_date`) VALUES
	(1, 'B-1243', 'Simple Hardware', 14000, '2018-01-01', '2018-06-25'),
	(2, 'A-555', 'Ice Ice Baby', 120000, '2018-01-01', '2018-12-31'),
	(3, 'C-954', 'Best Pros', 10000, '2018-01-20', '2018-07-20');
/*!40000 ALTER TABLE `contract` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
