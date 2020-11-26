
--DROP TABLE IF EXISTS city;

select * from city;

CREATE TABLE city (
    city_id SERIAL PRIMARY KEY,
    city_name VARCHAR(100),
	city_country VARCHAR(100),
	city_population NUMERIC(9,0),
    city_hemisphere VARCHAR(100)
);
--DROP TABLE IF EXISTS athletes;
CREATE TABLE athletes(
   athlete_id SERIAL PRIMARY KEY,
   athlete_first_name VARCHAR(255),
   athlete_last_name VARCHAR(255),
   athlete_birthplace INT,
   athlete_sex VARCHAR(1), 	
   CONSTRAINT fk_city
      FOREIGN KEY(athlete_id)
	  REFERENCES city(city_id)
);
select * from athletes;
select * from city;


INSERT INTO city (city_name, city_country, city_population, city_hemisphere)
VALUES('Sao Paulo' , 'Brazil', 12110000, 'S');
INSERT INTO city (city_name, city_country, city_population, city_hemisphere)
VALUES('Toronto' , 'Canada', 2732000, 'N');

INSERT INTO athletes (athlete_first_name, athlete_last_name, athlete_birthplace,athlete_sex)
VALUES ('Neymar', 'Silva', 1, 'M'), ('Natalie', 'Spooner', 2, 'F');


-- a: Insert a new city to include, id: 3, name: Tokyo, Country: Japan, Population: 9,2 million, Hemisphere: North.
INSERT INTO city (city_name, city_country, city_population, city_hemisphere)
VALUES('Tokyo' , 'Japan', 9200000, 'N');

-- b: Update Tokyo population to 9,73 million.
UPDATE city
SET city_population = 9730000  
WHERE city_name = 'Tokyo';

-- c: Query the city table for the cities in the northern hemispher and with population greater than 10 million.
select * from city where city_population > 10000000 AND city_hemisphere = 'N';

-- d: Query the city table for the sum of the populations of cities in the northern hemisphere.
SELECT city_hemisphere, SUM (city_population) FROM city WHERE city_hemisphere='N' GROUP BY city_hemisphere;

-- e: Query for athletes first name, last name and birth place.
select athlete_first_name, athlete_last_name, athlete_birthplace from athletes;

-- f: Query for all athletes who were born in the southern hemisphere.
select athlete_first_name, athlete_last_name FROM city INNER JOIN athletes on city_id=athlete_birthplace  where city_hemisphere='S';  

-- g: Query for female athletes born in a city with population over 5 million.
select athlete_first_name, athlete_last_name, city_name FROM city INNER JOIN athletes on city_id=athlete_birthplace 
where city_population > 5000000 AND athlete_sex = 'F'

-- h: Query for the athlete born in a city that has the highestpopulation.
select athlete_first_name, athlete_last_name, city_name FROM city INNER JOIN athletes on city_id=athlete_birthplace 
where city_population = (SELECT MAX(city_population)FROM city);