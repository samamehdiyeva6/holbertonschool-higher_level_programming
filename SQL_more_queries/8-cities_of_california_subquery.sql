-- djfksh
SELECT id, name FROM cities WHERE cities.state_id=(SELECT id FROM states WHERE states.name='California' LIMIT 1) ORDER BY cities.id
