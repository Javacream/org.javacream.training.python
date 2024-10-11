CREATE TABLE ADDRESSES (id number primary key, city varchar(32), street varchar(128))
CREATE TABLE PEOPLE (id number, lastname varchar(32), firstname varchar(32), address_id number, PRIMARY KEY(id), FOREIGN KEY (address_id) REFERENCES (ADDRESSES(id)))

