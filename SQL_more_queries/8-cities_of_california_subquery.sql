-- djfksh
SELECT id, name from hbtn_0d_usa.cities cities.id=(SELECT id from states WHERE states.name='California' LIMIT 1) ORDER BY cities.id
