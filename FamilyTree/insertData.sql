INSERT INTO Person VALUES(1000,6,0,0,"Grandpa","Thurlow","M",1001,"",0,"","");
INSERT INTO Person VALUES(1001,6,0,0,"Grandma","Thurlow","F",1000,"",0,"","");
INSERT INTO Person VALUES(1002,5,1000,1001,"Florence May","Thurlow","F",1005,"MayPlatt.jpg",1952,"","");
INSERT INTO Person VALUES(1003,6,0,0,"Grandpa","Platt","M",1004,"",0,"","");
INSERT INTO Person VALUES(1004,6,0,0,"Grandma","Platt","F",1003,"",0,"","");
INSERT INTO Person VALUES(1005,5,1003,1004,"Lawrence","Platt","M",1002,"1006.jpg",1952,"","");
INSERT INTO Person VALUES(1006,4,1006,1003,"Topsy","Walker","F",1007,"",0,"","");
INSERT INTO Person VALUES(1007,4,0,0,"Sydney","Walker","M",1006,"",0,"","2020");
INSERT INTO Person VALUES(1008,4,1005,1002,"John","Platt","M",1016,"JohnPlatt.jpg",1952,"Oct 1922","May 2010");
INSERT INTO Person VALUES(1009,3,1008,1016,"David","Platt","M",1010,"DavidPlatt.JPG",2013,"Aug 1953","");
INSERT INTO Person VALUES(1010,3,0,0,"Eileen","Boyle","F",1009,"",0,"Mar 2014","");
INSERT INTO Person VALUES(1011,2,1009,1010,"Jessica","Platt","F",1012,"",0,"Apr 1983","");
INSERT INTO Person VALUES(1012,2,0,0,"Paul","Mooney","M",1011,"",0,"Dec 1983","");
INSERT INTO Person VALUES(1013,2,1009,1010,"Christopher","Platt","M",0,"",0,"Nov 1985","");
INSERT INTO Person VALUES(1014,1,1012,1011,"Patrick","Mooney","M",0,"",0,"Mar 2014","");
INSERT INTO Person VALUES(1015,1,1012,1011,"Jason","Mooney","M",0,"",0,"Mar 2016","");
INSERT INTO Person VALUES(1016,4,0,0,"Rita","Wilkins","F",1008,"RitaPlatt.jpg",1952,"Aug 1929","Jun 2008");
INSERT INTO Person VALUES(1017,5,1000,1001,"Grace","Thurlow","F",0,"RitaPlatt.jpg",1952,"Aug 1929","Jun 2008");


INSERT INTO PersonChild VALUES(1005,1006);
INSERT INTO PersonChild VALUES(1005,1008);
INSERT INTO PersonChild VALUES(1012,1014);
INSERT INTO PersonChild VALUES(1012,1015);
INSERT INTO PersonChild VALUES(1011,1014);
INSERT INTO PersonChild VALUES(1011,1015);
INSERT INTO PersonChild VALUES(1009,1011);
INSERT INTO PersonChild VALUES(1009,1013);
INSERT INTO PersonChild VALUES(1010,1011);
INSERT INTO PersonChild VALUES(1010,1013);
INSERT INTO PersonChild VALUES(1008,1009);
INSERT INTO PersonChild VALUES(1016,1009);
INSERT INTO PersonChild VALUES(1003,1005);
INSERT INTO PersonChild VALUES(1004,1005);




