



--INSERT INTO [handyhub].[dbo].[services_servicecategory] ([name], [created_at], [created_by_id])
--VALUES('Gardening', GETDATE(), 1),
--    ('Snow Plough', GETDATE(), 1),
--    ('Plumbing', GETDATE(), 1),
--    ('Electrical', GETDATE(), 1),
--    ('Painting', GETDATE(), 1),
--    ('Carpentry', GETDATE(), 1),
--    ('Cleaning', GETDATE(), 1),
--    ('Pest Control', GETDATE(), 1),
--    ('Roofing', GETDATE(), 1);



---------This inserts into sub category srvices
---- Appliance Repair Subcategories
--INSERT INTO [handyhub].[dbo].[services_subcategory] ([name], [category_id])
--VALUES
--    ('Washing Machine Repair', 1),
--    ('Refrigerator Repair', 1),
--    ('Dishwasher Repair', 1),
--    ('Microwave Repair', 1);

---- Gardening Subcategories
--INSERT INTO [handyhub].[dbo].[services_subcategory] ([name], [category_id])
--VALUES
--    ('Lawn Mowing', 2),
--    ('Hedge Trimming', 2),
--    ('Planting & Landscaping', 2),
--    ('Weeding', 2);

---- Snow Plough Subcategories
--INSERT INTO [handyhub].[dbo].[services_subcategory] ([name], [category_id])
--VALUES
--    ('Driveway Clearing', 3),
--    ('Sidewalk Clearing', 3),
--    ('Roof Snow Removal', 3);

---- Plumbing Subcategories
--INSERT INTO [handyhub].[dbo].[services_subcategory] ([name], [category_id])
--VALUES
--    ('Leak Repair', 4),
--    ('Pipe Installation', 4),
--    ('Drain Cleaning', 4);

---- Electrical Subcategories
--INSERT INTO [handyhub].[dbo].[services_subcategory] ([name], [category_id])
--VALUES
--    ('Lighting Installation', 5),
--    ('Circuit Repair', 5),
--    ('Outlet Installation', 5);

---- Painting Subcategories
--INSERT INTO [handyhub].[dbo].[services_subcategory] ([name], [category_id])
--VALUES
--    ('Interior Painting', 6),
--    ('Exterior Painting', 6),
--    ('Fence Painting', 6);

---- Carpentry Subcategories
--INSERT INTO [handyhub].[dbo].[services_subcategory] ([name], [category_id])
--VALUES
--    ('Furniture Assembly', 7),
--    ('Custom Cabinetry', 7),
--    ('Door & Window Installation', 7);

---- Cleaning Subcategories
--INSERT INTO [handyhub].[dbo].[services_subcategory] ([name], [category_id])
--VALUES
--    ('House Cleaning', 8),
--    ('Office Cleaning', 8),
--    ('Carpet Cleaning', 8);

---- Pest Control Subcategories
--INSERT INTO [handyhub].[dbo].[services_subcategory] ([name], [category_id])
--VALUES
--    ('Rodent Control', 9),
--    ('Insect Control', 9),
--    ('Termite Treatment', 9);

---- Roofing Subcategories
--INSERT INTO [handyhub].[dbo].[services_subcategory] ([name], [category_id])
--VALUES
--    ('Roof Repair', 10),
--    ('Shingle Replacement', 10),
--    ('Gutter Installation', 10);





----This inserts into the service area table
----Delete from [handyhub].[dbo].[users_servicearea]
--INSERT INTO [handyhub].[dbo].[users_servicearea]
--    ([province], [city], [country], [is_active], [metro_city], [name])
--VALUES
---- Alberta (AB)
--('AB', 'Calgary', 'Canada', 1, 'Calgary', 'Calgary'),
--('AB', 'Airdrie', 'Canada', 1, 'Calgary', 'Airdrie'),
--('AB', 'Edmonton', 'Canada', 1, 'Edmonton', 'Edmonton'),
--('AB', 'Leduc', 'Canada', 1, 'Edmonton', 'Leduc'),
--('AB', 'Red Deer', 'Canada', 1, 'Red Deer', 'Red Deer'),
--('AB', 'Lethbridge', 'Canada', 1, 'Lethbridge', 'Lethbridge'),
--('AB', 'Grande Prairie', 'Canada', 1, 'Grande Prairie', 'Grande Prairie'),
--('AB', 'Medicine Hat', 'Canada', 1, 'Medicine Hat', 'Medicine Hat'),
--('AB', 'Fort McMurray', 'Canada', 1, 'Fort McMurray', 'Fort McMurray'),
--('AB', 'Spruce Grove', 'Canada', 1, 'Edmonton', 'Spruce Grove'),

---- British Columbia (BC)
--('BC', 'Vancouver', 'Canada', 1, 'Vancouver', 'Vancouver'),
--('BC', 'Victoria', 'Canada', 1, 'Victoria', 'Victoria'),
--('BC', 'Surrey', 'Canada', 1, 'Vancouver', 'Surrey'),
--('BC', 'Burnaby', 'Canada', 1, 'Vancouver', 'Burnaby'),
--('BC', 'Richmond', 'Canada', 1, 'Vancouver', 'Richmond'),
--('BC', 'Kelowna', 'Canada', 1, 'Kelowna', 'Kelowna'),
--('BC', 'Abbotsford', 'Canada', 1, 'Vancouver', 'Abbotsford'),

---- Manitoba (MB)
--('MB', 'Winnipeg', 'Canada', 1, 'Winnipeg', 'Winnipeg'),
--('MB', 'Brandon', 'Canada', 1, 'Brandon', 'Brandon'),

---- New Brunswick (NB)
--('NB', 'Fredericton', 'Canada', 1, 'Fredericton', 'Fredericton'),
--('NB', 'Moncton', 'Canada', 1, 'Moncton', 'Moncton'),
--('NB', 'Saint John', 'Canada', 1, 'Saint John', 'Saint John'),

---- Newfoundland and Labrador (NL)
--('NL', 'St. John\''s', 'Canada', 1, 'St. John\''s', 'St. John\''s'),

---- Nova Scotia (NS)
--('NS', 'Halifax', 'Canada', 1, 'Halifax', 'Halifax'),

---- Ontario (ON)
--('ON', 'Toronto', 'Canada', 1, 'Toronto', 'Toronto'),
--('ON', 'Ottawa', 'Canada', 1, 'Ottawa', 'Ottawa'),
--('ON', 'Mississauga', 'Canada', 1, 'Toronto', 'Mississauga'),
--('ON', 'Brampton', 'Canada', 1, 'Toronto', 'Brampton'),
--('ON', 'Hamilton', 'Canada', 1, 'Hamilton', 'Hamilton'),
--('ON', 'London', 'Canada', 1, 'London', 'London'),
--('ON', 'Kitchener', 'Canada', 1, 'Kitchener', 'Kitchener'),

---- Prince Edward Island (PE)
--('PE', 'Charlottetown', 'Canada', 1, 'Charlottetown', 'Charlottetown'),

---- Quebec (QC)
--('QC', 'Montreal', 'Canada', 1, 'Montreal', 'Montreal'),
--('QC', 'Quebec City', 'Canada', 1, 'Quebec City', 'Quebec City'),
--('QC', 'Laval', 'Canada', 1, 'Montreal', 'Laval'),
--('QC', 'Gatineau', 'Canada', 1, 'Ottawa', 'Gatineau'),

---- Saskatchewan (SK)
--('SK', 'Regina', 'Canada', 1, 'Regina', 'Regina'),
--('SK', 'Saskatoon', 'Canada', 1, 'Saskatoon', 'Saskatoon'),

---- Territories
---- Northwest Territories (NT)
--('NT', 'Yellowknife', 'Canada', 1, 'Yellowknife', 'Yellowknife'),

---- Nunavut (NU)
--('NU', 'Iqaluit', 'Canada', 1, 'Iqaluit', 'Iqaluit'),

---- Yukon (YT)
--('YT', 'Whitehorse', 'Canada', 1, 'Whitehorse', 'Whitehorse');
