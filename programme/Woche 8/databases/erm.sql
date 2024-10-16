CREATE TABLE ADDRESSES (id INTEGER PRIMARY KEY, city VARCHAR(32), street VARCHAR(128))
CREATE TABLE PEOPLE (id INTEGER, lastname VARCHAR(32), firstname VARCHAR(32), address_id INTEGER, PRIMARY KEY(id), FOREIGN KEY (address_id) REFERENCES ADDRESSES(id))
CREATE TABLE COMPANIES (id INTEGER, company_name VARCHAR(32), PRIMARY KEY(id))
CREATE TABLE EMPLOYEES (person_id INTEGER, company_id INTEGER, PRIMARY KEY (person_id, company_id), FOREIGN KEY (person_id) REFERENCES PEOPLE(id), FOREIGN KEY (company_id) REFERENCES COMPANIES(id))

