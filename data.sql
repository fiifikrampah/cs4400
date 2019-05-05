-- pw jsmith123
insert into allusers values ('james.smith', '1254737c076cf867dc53d60a0364f38e', 'Approved', 'James', 'Smith', 'Employee');
-- pw msmith456
insert into allusers values ('michael.smith', '173dafbc79fd0527ee13bcdd75ae37e1', 'Approved', 'Michael', 'Smith', 'Employee, Visitor');
-- pw rsmith789
insert into allusers values ('robert.smith', '5bb783f424929272aa2845165cf54727', 'Approved','Robert', 'Smith','Employee');
-- pw mgarcia123
insert into allusers values ('maria.garcia', 'cc0c3924b78d426700360b76db8b2403', 'Approved', 'Maria', 'Garcia', 'Employee, Visitor');
-- pw dsmith456
insert into allusers values ('david.smith', '07f4556478cb21b005f82051ef5ca3c8', 'Approved', 'David', 'Smith',  'Employee');
-- pw manager1
insert into allusers values ('manager1', 'c240642ddef994358c96da82c0361a58', 'Pending', 'Manager', 'One', 'Employee');
-- pw manager2
insert into allusers values ('manager2', '8df5127cd164b5bc2d2b78410a7eea0c', 'Approved', 'Manager', 'Two', 'Employee, Visitor');
-- pw manager3
insert into allusers values ('manager3', '2d3a5db4a2a9717b43698520a8de57d0', 'Approved', 'Manager', 'Three', 'Employee');
-- pw manager4
insert into allusers values ('manager4', 'e1ec6fc941af3ba79a4ac5242dd39735', 'Approved',  'Manager', 'Four', 'Employee, Visitor');
-- pw manager5
insert into allusers values ('manager5', '029cb1d27c0b9c551703ccba2591c334', 'Approved', 'Manager', 'Five', 'Employee, Visitor');
-- pw mrodriguez
insert into allusers values ('maria.rodriguez', '08ed5c4b5499407be0a438654984da36', 'Declined', 'Maria', 'Rodriguez','Visitor' );
-- pw msmith789
insert into allusers values ('mary.smith', 'b4e4e07c0df7185cb5df959a0074d45b', 'Approved', 'Mary', 'Smith', 'Visitor');
-- pw mhernandez
insert into allusers values ('maria.hernandez', '9acd33e5f3c729eeea08bbee68b62605', 'Approved', 'Maria', 'Hernandez', 'User');
-- pw staff1234
insert into allusers values ('staff1', '04d4b37015f6ba05077ae49776a76b95', 'Approved', 'Staff', 'One', 'Employee');
-- pw staff4567
insert into allusers values ('staff2', '3c20c4518381a51023bdd5eb2eb66977','Approved',  'Staff', 'Two',  'Employee, Visitor');
-- pw staff7890
insert into allusers values ('staff3', '308a4c22bebf60c77f158b103695d0ec', 'Approved',  'Staff', 'Three', 'Employee, Visitor');
-- pw user123456
insert into allusers values ('user1', '4da49c16db42ca04538d629ef0533fe8', 'Pending',  'User', 'One', 'User');
-- pw visitor123
insert into allusers values ('visitor1', '377656457556736de417e2f9d7fca8a1', 'Approved', 'Visitor', 'One', 'Visitor');


insert into useremail values ('james.smith', 'jsmith@gmail.com');
insert into useremail values ('james.smith', 'jsmith@hotmail.com');
insert into useremail values ('james.smith', 'jsmith@gatech.edu');
insert into useremail values ('james.smith', 'jsmith@outlook.com');
insert into useremail values ('michael.smith', 'msmith@gmail.com');
insert into useremail values ('robert.smith', 'rsmith@hotmail.com');
insert into useremail values ('maria.garcia', 'mgarcia@yahoo.com');
insert into useremail values ('maria.garcia', 'mgarcia@gatech.edu');
insert into useremail values ('david.smith', 'dsmith@outlook.com');
insert into useremail values ('maria.rodriguez', 'mrodriguez@gmail.com');
insert into useremail values ('mary.smith', 'mary@outlook.com');
insert into useremail values ('maria.hernandez', 'mh@gatech.edu');
insert into useremail values ('maria.hernandez', 'mh123@gmail.com');
insert into useremail values ('manager1', 'm1@beltline.com');
insert into useremail values ('manager2', 'm2@beltline.com');
insert into useremail values ('manager3', 'm3@beltline.com');
insert into useremail values ('manager4', 'm4@beltline.com');
insert into useremail values ('manager5', 'm5@beltline.com');
insert into useremail values ('staff1', 's1@beltline.com');
insert into useremail values ('staff2', 's2@beltline.com');
insert into useremail values ('staff3', 's3@beltline.com');
insert into useremail values ('user1', 'u1@beltline.com');
insert into useremail values ('visitor1', 'v1@beltline.com');

insert into employee values ('james.smith', "000000001", '4043721234', '123 East Main Street', 'Rochester', 'NY', '14604', 'Admin');
insert into employee values ('michael.smith', "000000002", '4043726789', '350 Ferst Drive', 'Atlanta', 'GA', '30332', 'Staff');
insert into employee values ('robert.smith', "000000003", '1234567890', '123 East Main Street', 'Columbus', 'OH', '43215', 'Staff');
insert into employee values ('maria.garcia', "000000004", '7890123456', '123 East Main Street', 'Richland', 'PA', '17987', 'Manager');
insert into employee values ('david.smith', "000000005", '5124776435', '350 Ferst Drive', 'Atlanta', 'GA', '30332', 'Manager');
insert into employee values ('manager1', "000000006", '8045126767', '123 East Main Street', 'Rochester', 'NY', '14604', 'Manager');
insert into employee values ('manager2', "000000007", '9876543210', '123 East Main Street', 'Rochester', 'NY', '14604', 'Manager');
insert into employee values ('manager3', "000000008", '5432167890', '350 Ferst Drive', 'Atlanta', 'GA', '30332', 'Manager');
insert into employee values ('manager4', "000000009", '8053467565', '123 East Main Street', 'Columbus', 'OH', '43215', 'Manager');
insert into employee values ('manager5', "000000010", '8031446782', '801 Atlantic Drive', 'Atlanta', 'GA', '30332', 'Manager');
insert into employee values ('staff1', "000000011", '8024456765', '266 Ferst Drive Northwest', 'Atlanta', 'GA', '30332', 'Staff');
insert into employee values ('staff2', "000000012", '8888888888', '266 Ferst Drive Northwest', 'Atlanta', 'GA', '30332', 'Staff');
insert into employee values ('staff3', "000000013", '3333333333', '801 Atlantic Drive', 'Atlanta', 'GA', '30332', 'Staff');


insert into site values ('Piedmont Park', '400 Park Drive Northeast', '30306', "YES", 'manager2');
insert into site values ('Atlanta Beltline Center', '112 Krog Street Northeast', '30307', "NO", 'manager3');
insert into site values ('Historic Fourth Ward Park', '680 Dallas Street Northeast', '30308', "YES", 'manager4');
insert into site values ('Westview Cemetery', '1680 Westview Drive Southwest', '30310', "NO", 'manager5');
insert into site values ('Inman Park', '', '30307', "YES", 'david.smith');

insert into event values ('Piedmont Park', 'Eastside Trail', '2019-02-04', '2019-02-05', 0, 99999, 1, 'A combination of multi-use trail and linear green space, the Eastside Trail was the first finished section of the Atlanta BeltLine trail in the old rail corridor. The Eastside Trail, which was funded by a combination of public and private philanthropic sources, runs from the tip of Piedmont Park to Reynoldstown. More details at https://beltline.org/explore-atlanta-beltline-trails/eastside-trail/');
insert into event values ('Inman Park', 'Eastside Trail', '2019-02-04', '2019-02-05', 0, 99999, 1, 'A combination of multi-use trail and linear green space, the Eastside Trail was the first finished section of the Atlanta BeltLine trail in the old rail corridor. The Eastside Trail, which was funded by a combination of public and private philanthropic sources, runs from the tip of Piedmont Park to Reynoldstown. More details at https://beltline.org/explore-atlanta-beltline-trails/eastside-trail/');
insert into event values ('Inman Park', 'Eastside Trail', '2019-03-01', '2019-03-02', 0, 99999, 1, 'A combination of multi-use trail and linear green space, the Eastside Trail was the first finished section of the Atlanta BeltLine trail in the old rail corridor. The Eastside Trail, which was funded by a combination of public and private philanthropic sources, runs from the tip of Piedmont Park to Reynoldstown. More details at https://beltline.org/explore-atlanta-beltline-trails/eastside-trail/');
insert into event values ('Historic Fourth Ward Park', 'Eastside Trail', '2019-02-13', '2019-02-14', 0, 99999, 1, 'A combination of multi-use trail and linear green space, the Eastside Trail was the first finished section of the Atlanta BeltLine trail in the old rail corridor. The Eastside Trail, which was funded by a combination of public and private philanthropic sources, runs from the tip of Piedmont Park to Reynoldstown. More details at https://beltline.org/explore-atlanta-beltline-trails/eastside-trail/');
insert into event values ('Westview Cemetery', 'Westside Trail', '2019-02-18', '2019-02-21', 0, 99999, 1, 'The Westside Trail is a free amenity that offers a bicycle and pedestrian-safe corridor with a 14-foot-wide multi-use trail surrounded by mature trees and grasses thanks to Trees Atlanta’s Arboretum. With 16 points of entry, 14 of which will be ADA-accessible with ramp and stair systems, the trail provides numerous access points for people of all abilities. More details at: https://beltline.org/explore-atlanta-beltline-trails/westside-trail/');
insert into event values ('Inman Park', 'Bus Tour', '2019-02-01', '2019-02-02', 25, 6, 2, 'The Atlanta BeltLine Partnership’s tour program operates with a natural gas-powered, ADA accessible tour bus funded through contributions from 10th & Monroe, LLC, SunTrust Bank Trusteed Foundations–Florence C. and Harry L. English Memorial Fund and Thomas Guy Woolford Charitable Trust, and AGL Resources');
insert into event values ('Inman Park', 'Bus Tour', '2019-02-08', '2019-02-10', 25, 6, 2, 'The Atlanta BeltLine Partnership’s tour program operates with a natural gas-powered, ADA accessible tour bus funded through contributions from 10th & Monroe, LLC, SunTrust Bank Trusteed Foundations–Florence C. and Harry L. English Memorial Fund and Thomas Guy Woolford Charitable Trust, and AGL Resources');
insert into event values ('Inman Park', 'Private Bus Tour', '2019-02-01', '2019-02-02', 40, 4, 1, 'Private tours are available most days, pending bus and tour guide availability. Private tours can accommodate up to 4 guests per tour, and are subject to a tour fee (nonprofit rates are available). As a nonprofit organization with limited resources, we are unable to offer free private tours. We thank you for your support and your understanding as we try to provide as many private group tours as possible. The Atlanta BeltLine Partnership’s tour program operates with a natural gas-powered, ADA accessible tour bus funded through contributions from 10th & Monroe, LLC, SunTrust Bank Trusteed Foundations–Florence C. and Harry L. English Memorial Fund and Thomas Guy Woolford Charitable Trust, and AGL Resources');
insert into event values ('Inman Park', 'Arboretum Walking Tour', '2019-02-08', '2019-02-11', 5, 5, 1, 'Official Atlanta BeltLine Arboretum Walking Tours provide an up-close view of the Westside Trail and the Atlanta BeltLine Arboretum led by Trees Atlanta Docents. The one and a half hour tours step off at at 10am (Oct thru May), and 9am (June thru September). Departure for all tours is from Rose Circle Park near Brown Middle School. More details at: https://beltline.org/visit/atlanta-beltline-tours/#arboretum-walking');
insert into event values ('Atlanta Beltline Center', 'Official Atlanta BeltLine Bike Tour', '2019-02-09', '2019-02-14', 5, 5, 1, 'These tours will include rest stops highlighting assets and points of interest along the Atlanta BeltLine. Staff will lead the rides, and each group will have a ride sweep to help with any unexpected mechanical difficulties.');

insert into transit values ('MARTA', 'Blue', 2.00);
insert into transit values ('Bus', '152', 2.00);
insert into transit values ('Bike', 'Relay', 1.00);

insert into connect values ('Inman Park', 'MARTA', 'Blue');
insert into connect values ('Piedmont Park', 'MARTA', 'Blue');
insert into connect values ('Historic Fourth Ward Park', 'MARTA', 'Blue');
insert into connect values ('Westview Cemetery', 'MARTA', 'Blue');
insert into connect values ('Inman Park', 'Bus', '152');
insert into connect values ('Piedmont Park', 'Bus', '152');
insert into connect values ('Historic Fourth Ward Park', 'Bus', '152');
insert into connect values ('Piedmont Park', 'Bike', 'Relay');
insert into connect values ('Historic Fourth Ward Park', 'Bike', 'Relay');

insert into taketransit values ('manager2', 'MARTA', 'Blue', '2019-03-20');
insert into taketransit values ('manager2', 'Bus', '152', '2019-03-20');
insert into taketransit values ('manager3', 'Bike', 'Relay', '2019-03-20');
insert into taketransit values ('manager2', 'MARTA', 'Blue', '2019-03-21');
insert into taketransit values ('maria.hernandez', 'Bus', '152', '2019-03-20');
insert into taketransit values ('maria.hernandez', 'Bike', 'Relay', '2019-03-20');
insert into taketransit values ('manager2', 'MARTA', 'Blue', '2019-03-22');
insert into taketransit values ('maria.hernandez', 'Bus', '152', '2019-03-22');
insert into taketransit values ('mary.smith', 'Bike', 'Relay', '2019-03-23');
insert into taketransit values ('visitor1', 'MARTA', 'Blue', '2019-03-21');

insert into assignto values ('michael.smith', 'Eastside Trail', '2019-02-04', 'Piedmont Park');
insert into assignto values ('staff1', 'Eastside Trail', '2019-02-04', 'Piedmont Park');
insert into assignto values ('robert.smith','Eastside Trail', '2019-02-04', 'Inman Park');
insert into assignto values ('staff2', 'Eastside Trail', '2019-02-04', 'Inman Park');
insert into assignto values ('staff1', 'Eastside Trail', '2019-03-01', 'Inman Park');
insert into assignto values ('michael.smith', 'Eastside Trail', '2019-02-13', 'Historic Fourth Ward Park');
insert into assignto values ('staff1', 'Westside Trail', '2019-02-18', 'Westview Cemetery');
insert into assignto values ('staff3', 'Westside Trail', '2019-02-18', 'Westview Cemetery');
insert into assignto values ('michael.smith', 'Bus Tour', '2019-02-01', 'Inman Park');
insert into assignto values ('staff2', 'Bus Tour', '2019-02-01', 'Inman Park');
insert into assignto values ('robert.smith', 'Bus Tour', '2019-02-08', 'Inman Park');
insert into assignto values ('michael.smith', 'Bus Tour', '2019-02-08', 'Inman Park');
insert into assignto values ('robert.smith', 'Private Bus Tour', '2019-02-01', 'Inman Park');
insert into assignto values ('staff3', 'Arboretum Walking Tour', '2019-02-08', 'Inman Park');
insert into assignto values ('staff1', 'Official Atlanta BeltLine Bike Tour', '2019-02-09', 'Atlanta BeltLine Center');

insert into visitevent values ('mary.smith', 'Bus Tour', '2019-02-01','Inman Park', '2019-02-01');
insert into visitevent values ('maria.garcia', 'Bus Tour', '2019-02-01','Inman Park',  '2019-02-02');
insert into visitevent values ('manager2', 'Bus Tour', '2019-02-01','Inman Park',  '2019-02-02');
insert into visitevent values ('manager4', 'Bus Tour', '2019-02-01','Inman Park',  '2019-02-01');
insert into visitevent values ('manager5', 'Bus Tour', '2019-02-01','Inman Park',  '2019-02-02');
insert into visitevent values ('staff2', 'Bus Tour', '2019-02-01', 'Inman Park',  '2019-02-02');
insert into visitevent values ('mary.smith', 'Westside Trail', '2019-02-18','Westview Cemetery',  '2019-02-19');
insert into visitevent values ('mary.smith', 'Private Bus Tour', '2019-02-01','Inman Park',  '2019-02-01');
insert into visitevent values ('mary.smith', 'Private Bus Tour', '2019-02-01', 'Inman Park', '2019-02-02');
insert into visitevent values ('mary.smith', 'Official Atlanta BeltLine Bike Tour', '2019-02-09','Atlanta BeltLine Center',  '2019-02-10');
insert into visitevent values ('mary.smith', 'Arboretum Walking Tour', '2019-02-08', 'Inman Park', '2019-02-10');
insert into visitevent values ('mary.smith', 'Eastside Trail', '2019-02-04','Piedmont Park',  '2019-02-04');
insert into visitevent values ('mary.smith', 'Eastside Trail', '2019-02-13','Historic Fourth Ward Park',  '2019-02-13');
insert into visitevent values ('mary.smith', 'Eastside Trail', '2019-02-13','Historic Fourth Ward Park',  '2019-02-14');
insert into visitevent values ('visitor1', 'Eastside Trail', '2019-02-13', 'Historic Fourth Ward Park', '2019-02-14');
insert into visitevent values ('visitor1', 'Official Atlanta BeltLine Bike Tour', '2019-02-09','Atlanta BeltLine Center',  '2019-02-10');
insert into visitevent values ('visitor1', 'Westside Trail', '2019-02-18', 'Westview Cemetery',  '2019-02-19');

insert into visitsite values ('mary.smith', 'Inman Park', '2019-02-01');
insert into visitsite values ('mary.smith', 'Inman Park', '2019-02-02');
insert into visitsite values ('mary.smith', 'Inman Park', '2019-02-03');
insert into visitsite values ('mary.smith', 'Atlanta BeltLine Center', '2019-02-01');
insert into visitsite values ('mary.smith', 'Atlanta BeltLine Center', '2019-02-10');
insert into visitsite values ('mary.smith', 'Historic Fourth Ward Park', '2019-02-02');
insert into visitsite values ('mary.smith', 'Piedmont Park', '2019-02-02');
insert into visitsite values ('visitor1', 'Piedmont Park', '2019-02-11');
insert into visitsite values ('visitor1', 'Atlanta BeltLine Center', '2019-02-13');
insert into visitsite values ('visitor1', 'Historic Fourth Ward Park', '2019-02-11');
insert into visitsite values ('visitor1', 'Westview Cemetery', '2019-02-06');
insert into visitsite values ('visitor1', 'Inman Park', '2019-02-01');
insert into visitsite values ('visitor1', 'Piedmont Park', '2019-02-01');
insert into visitsite values ('visitor1', 'Atlanta BeltLine Center', '2019-02-09');