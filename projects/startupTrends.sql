/* Select all the rows to observe the data table*/
SELECT *
FROM startups;
/*Calculate the total number of companies in the table*/
SELECT COUNT(*)
FROM startups;
/*Calculate the total value of all the companies in the table*/
SELECT SUM(valuation)
FROM startups;
/*Find the highest amount raised by a startup during the Seed stage*/
SELECT MAX(raised)
FROM startups
WHERE stage = 'Seed';
/*Find the year the oldest company was founded*/
SELECT MIN(founded)
FROM startups; 
/*Find the average valuation*/
SELECT AVG(valuation)
FROM startups;
/*Find the average valuation in each category*/
SELECT category, AVG(valuation)
FROM startups
GROUP BY category;
/*Return the average valuation in each category. Round the average to two decimals.*/
SELECT category, ROUND(AVG(valuation),2)
FROM startups
GROUP BY category;
/*Return the average valuation in each category. Round the average to two decimal places and order the list from highest to lowest*/
SELECT category, ROUND(AVG(valuation),2) A
FROM startups
GROUP BY category
ORDER BY A;
/*Return the name of each category with the total number of companies that belong to it.*/
SELECT category, COUNT(category) B
FROM startups
GROUP BY category
ORDER BY B;
/*Return the name of each category with the total number of companies that belong to it. Filter the results to only show categories with more than three companies.*/
SELECT category, COUNT(category) B
FROM startups
GROUP BY category
HAVING B > 3
ORDER BY B;
/*What is the average size of a startup in each location?*/
SELECT location, ROUND(AVG(employees)) EmployeeNum
FROM startups
GROUP BY location
ORDER BY EmployeeNum DESC;
/*What is the average size of a startup in each location with average sizes above 500?*/
SELECT location, ROUND(AVG(employees)) EmployeeNum
FROM startups
GROUP BY location
HAVING EmployeeNum > 500
ORDER BY EmployeeNum DESC;
