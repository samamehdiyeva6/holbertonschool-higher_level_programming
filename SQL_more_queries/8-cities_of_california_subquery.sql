-- djfksh
SELECT id, name FROM hbtn_0d_usa.cities WHERE cities.id=(SELECT id FROM states WHERE states.name='California' LIMIT 1) ORDER BY cities.id
