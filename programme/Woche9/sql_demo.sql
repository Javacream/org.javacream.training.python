INSERT INTO PEOPLE (id, lastname, firstname) VALUES(1, 'Sawitzki', 'Rainer')
INSERT INTO ADDRESSES (id, city, street) VALUES (1, 'München', 'Marienplatz')
INSERT INTO COMPANIES (id, company_name) VALUES (1, 'Javacream')
INSERT INTO EMPLOYEES (person_id, company_id) VALUES (1, 1)

SELECT * FROM PEOPLE
SELECT * FROM PEOPLE WHERE ID = 1

UPDATE PEOPLE SET firstname = 'Klaus' WHERE lastname='Sawitzki'
DELETE FROM PEOPLE WHERE ID = 42