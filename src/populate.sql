
BEGIN;

INSERT INTO expenses (name,amount,category,date,added,comment,user_owner) VALUES ('test1',112,'Entertainment','2022-10-07',NOW(),'test add', 1);
INSERT INTO expenses (name,amount,category,date,added,comment,user_owner) VALUES ('test2',420,'Hobbies','2022-10-07',NOW(),'test add2', 1);
INSERT INTO expenses (name,amount,category,date,added,comment,user_owner) VALUES ('test3',333,'Other','2022-10-07',NOW(),'test add3', 1);
INSERT INTO expenses (name,amount,category,date,added,comment,user_owner) VALUES ('test4',12,'Groceries','2022-10-07',NOW(),'test add4', 1);
INSERT INTO expenses (name,amount,category,date,added,comment,user_owner) VALUES ('test5',27,'Bills','2022-10-07',NOW(),'test add5', 1);
INSERT INTO expenses (name,amount,category,date,added,comment,user_owner) VALUES ('test6',378,'Bills','2022-10-07',NOW(),'test add6', 1);

COMMIT;