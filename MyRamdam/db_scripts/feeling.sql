CREATE TABLE feelings(
		feel_id int,
		feeling text);

CREATE OR REPLACE
	FUNCTION get_feeling(in int, out text)
	RETURNS text as

$BODY$
		select feeling from feelings
		where feel_id = $1;

$BODY$
language 'sql';


CREATE OR REPLACE
	FUNCTION add_feeling(p_feel_id int, p_feeling text)
	RETURNS text as

$BODY$
	declare
		v_feel_id int;
	begin
		select into v_feel_id feel_id from feelings
		where feel_id = p_feel_id;

		if v_feel_id isnull then
			insert into feelings(feel_id, feeling) values (p_feel_id, p_feeling);
			return 'OK';
		else
			return 'Feeling already exists';
		end if;
	end;
$BODY$
language 'plpgsql'