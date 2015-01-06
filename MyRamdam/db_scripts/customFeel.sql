create table customFeel(
    cfeel_id serial primary key,
    cfeel_name text,
    feelID_FK serial references feelings (feel_id),
);


--HOW TO USE:
-- SELECT get_leanfeel(1);

create or replace function get_leanfeel(in int, out int) 
	returns setof record as

$$ 
    select feelID_FK from customFeel
		where cfeel_id = $1;
$$
	language 'sql';


--HOW TO USE:
-- SELECT add_custfeel('incomplete', 2);

create or replace function add_custfeel(p_cfeel_name text, p_teamname2feelID_FK int) 
returns text as

$$
declare
  v_cfeel_id int; 
begin
  select into v_cfeel_id cfeel_id from customFeel
	where cfeel_name = p_cfeel_name and feelID_FK = p_feelID_FK

	if v_id isnull then
		insert into customFeel(cfeel_name, feelID_FK) 
					values
					(p_cfeel_name, p_feelID_FK)
    	return 'Ok';
    else
    	update customFeel
    	set cfeel_name = p_cfeel_name, feelID_FK = p_feelID_FK
    		where cfeel_id = v_cfeel_id
    	return 'Ok';
    endif;
  end;
$$
    language 'plpgsql';
    
	
