-- djfksh
SELECT cities.id, cities.name, states.name FROM cities WHERE cities.state_id=SELECT id FROM states ORDER BY cities.id
