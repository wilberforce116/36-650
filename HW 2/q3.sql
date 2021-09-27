                                   Table "public.rdata"
 Column |         Type         | Collation | Nullable |              Default              
--------+----------------------+-----------+----------+-----------------------------------
 id     | integer              |           | not null | nextval('rdata_id_seq'::regclass)
 a      | character varying(5) |           | not null | 
 b      | character varying(5) |           | not null | 
 moment | date                 |           |          | '2020-01-01'::date
 x      | numeric(5,2)         |           |          | 
Indexes:
    "rdata_pkey" PRIMARY KEY, btree (id)
    "rdata_a_key" UNIQUE CONSTRAINT, btree (a)
    "rdata_b_key" UNIQUE CONSTRAINT, btree (b)
Check constraints:
    "rdata_x_check" CHECK (x > 0::numeric)