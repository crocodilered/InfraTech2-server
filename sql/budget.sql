
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


CREATE TABLE IF NOT EXISTS `budget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `begin_date` date NOT NULL COMMENT 'Begin of budget period.',
  `end_date` date NOT NULL COMMENT 'End of budget period.',
  `value` int(11) NOT NULL DEFAULT '0' COMMENT 'Value of budget.',
  PRIMARY KEY (`id`),
  UNIQUE KEY `begin_date_end_date` (`begin_date`,`end_date`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='Directory of budgets for equipment maintanance.';


/*!40000 ALTER TABLE `budget` DISABLE KEYS */;
INSERT INTO `budget` (`id`, `begin_date`, `end_date`, `value`) VALUES
	(1, '2018-01-01', '2018-12-31', 10000);
/*!40000 ALTER TABLE `budget` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
