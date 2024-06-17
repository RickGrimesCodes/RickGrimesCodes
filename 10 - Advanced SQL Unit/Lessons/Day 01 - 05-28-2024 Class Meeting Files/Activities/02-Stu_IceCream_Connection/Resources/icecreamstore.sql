
--
-- Table structure for table `icecreamstore`
--

DROP TABLE IF EXISTS icecreamstore;

CREATE TABLE icecreamstore (
  ID SERIAL PRIMARY KEY,
  Flavors VARCHAR DEFAULT NULL,
  Quantities INT DEFAULT NULL,
  Price decimal DEFAULT NULL
);

--
-- Dumping data for table `icecreamstore`
--


INSERT INTO icecreamstore VALUES (1,'Vanilla',100,1.00),(2,'Chocolate',150,1.25),(3,'Strawberry',95,1.25),(4,'Rocky Road',50,1.50),(5,'Cookie Dough',75,1.50),(25,'testflavor',5,0.25);
