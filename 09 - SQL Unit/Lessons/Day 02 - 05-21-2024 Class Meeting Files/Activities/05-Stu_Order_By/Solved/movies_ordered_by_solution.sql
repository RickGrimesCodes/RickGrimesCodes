-- Select Top 10 count of actors first names in descending order
SELECT first_name, COUNT(first_name) AS "actor count"
FROM actor
GROUP BY first_name
ORDER BY "actor count" DESC
LIMIT 10;

-- Select the average duration of movies by rating
SELECT rating, ROUND(AVG(rental_duration),2) AS "avg duration"
FROM film
GROUP BY rating
ORDER BY "avg duration";

-- Select average replace costs and length of movie by rating
SELECT rating, ROUND(AVG(replacement_cost),2) AS "avg cost", ROUND(AVG(length),2) as "avg length"
FROM film
GROUP BY rating
ORDER BY "avg length" DESC;

-- Select the count of countries
SELECT country.country, COUNT(country.country) AS "country count"
FROM city
JOIN country ON city.country_id = country.country_id
GROUP BY country.country
ORDER BY "country count" DESC;
