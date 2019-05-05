CREATE TABLE `allusers` (
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Status` enum('Approved','Pending','Declined') NOT NULL,
  `Firstname` varchar(255) NOT NULL,
  `Lastname` varchar(255) NOT NULL,
  `UserType` enum('User','Visitor','Employee','Employee, Visitor') NOT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `assignto` (
  `StaffUsername` varchar(255) NOT NULL DEFAULT 'NONE',
  `EventName` varchar(255) NOT NULL DEFAULT 'NONE',
  `StartDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `SiteName` varchar(255) NOT NULL DEFAULT 'NONE',
  PRIMARY KEY (`StaffUsername`,`EventName`,`StartDate`,`SiteName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `connect` (
  `SiteName` varchar(255) NOT NULL DEFAULT 'NONE',
  `TransitType` enum('MARTA','Bike','Bus') NOT NULL,
  `TransitRoute` varchar(255) NOT NULL DEFAULT 'NONE',
  PRIMARY KEY (`SiteName`,`TransitType`,`TransitRoute`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `employee` (
  `Username` varchar(255) NOT NULL DEFAULT 'NONE',
  `EmployeeID` varchar(9) DEFAULT 'NONE',
  `Phone` varchar(10) NOT NULL,
  `EmployeeAddress` varchar(255) NOT NULL DEFAULT 'NONE',
  `EmployeeCity` varchar(255) NOT NULL DEFAULT 'NONE',
  `EmployeeState` varchar(255) NOT NULL DEFAULT 'NONE',
  `EmployeeZipcode` varchar(5) NOT NULL,
  `EmployeeType` varchar(255) NOT NULL,
  PRIMARY KEY (`Username`),
  UNIQUE KEY `Phone_UNIQUE` (`Phone`),
  UNIQUE KEY `EmployeeID_UNIQUE` (`EmployeeID`),
  CONSTRAINT `Username` FOREIGN KEY (`Username`) REFERENCES `allusers` (`Username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `event` (
  `EventName` varchar(255) NOT NULL DEFAULT 'NONE',
  `StartDate` datetime NOT NULL,
  `SiteName` varchar(255) NOT NULL,
  `EndDate` datetime NOT NULL,
  `EventPrice` decimal(6,2) NOT NULL,
  `Capacity` int(11) NOT NULL,
  `MinStaffRequired` int(11) NOT NULL,
  `Description` text NOT NULL,
  PRIMARY KEY (`EventName`,`SiteName`,`StartDate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `site` (
  `SiteName` varchar(255) NOT NULL,
  `SiteAddress` varchar(255) NOT NULL DEFAULT 'NONE',
  `SiteZipcode` int(5) NOT NULL,
  `OpenEveryday` enum('Yes','No') NOT NULL,
  `ManagerUsername` varchar(255) NOT NULL DEFAULT 'NONE',
  PRIMARY KEY (`SiteName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `taketransit` (
  `Username` varchar(255) NOT NULL,
  `TransitType` enum('MARTA','Bike','Bus') NOT NULL,
  `TransitRoute` varchar(255) NOT NULL,
  `TransitDate` datetime NOT NULL,
  PRIMARY KEY (`TransitType`,`TransitDate`,`TransitRoute`,`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `transit` (
  `TransitType` varchar(255) NOT NULL,
  `TransitRoute` varchar(255) NOT NULL,
  `TransitPrice` double NOT NULL,
  PRIMARY KEY (`TransitType`,`TransitRoute`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `useremail` (
  `Username` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL DEFAULT 'NONE',
  UNIQUE KEY `Email_UNIQUE` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `visitevent` (
  `VisitorUsername` varchar(255) NOT NULL DEFAULT 'NONE',
  `EventName` varchar(255) NOT NULL DEFAULT 'NONE',
  `StartDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `SiteName` varchar(255) NOT NULL DEFAULT 'NONE',
  `VisitEventDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`VisitorUsername`,`EventName`,`StartDate`,`SiteName`,`VisitEventDate`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `visitsite` (
  `VisitorUsername` varchar(255) NOT NULL DEFAULT 'NONE',
  `SiteName` varchar(255) NOT NULL DEFAULT 'NONE',
  `VisitSiteDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`VisitorUsername`,`SiteName`,`VisitSiteDate`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `calendar` (
  `_date` date NOT NULL,
  PRIMARY KEY (`_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `tempmail` (
  `Email` varchar(255) NOT NULL,
  PRIMARY KEY (`Email`),
  UNIQUE KEY `Email_UNIQUE` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
