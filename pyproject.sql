-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 24, 2019 at 10:00 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `PYproject`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `studID` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `DOB` date NOT NULL,
  `gender` varchar(255) NOT NULL,
  `mobile` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`fname`, `lname`, `studID`, `address`, `DOB`, `gender`, `mobile`, `email`) VALUES
('sunny', 'bhagwat', '3445', 'chendani koliwada mithbandar road thane (E)', '2000-11-27', 'male', '8419947622', 'sunnybhagwat35@gmail.com'),
('shreyas', 'desai', '3446', 'Dnyaneshwar nagar thane (w)', '2001-08-30', 'male', '9867451950', 'shreyasdesai3013@gmail.com'),
('aatish', 'bhilare', '1246', 'balkum thane (w)', '2000-11-25', 'male', '8268211123', '92aatish@gmail.com'),
('jayesh', 'nandgaonkar', '2354', 'castle mill thane(W) ', '2000-09-10', 'male', '8652782873', 'jayeshnandgaonkar10@gmail.com'),
('mosh', 'williams', '7852', 'mumbai csmt (E)', '2096-09-03', 'male', '7589512365', 'mosh@gmail.com');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
