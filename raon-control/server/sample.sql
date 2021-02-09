INSERT INTO schedule(fromDate,toDate,title) values
('2021-02-08','2021-02-09','Beam Commissioning'),
('2021-02-17','2021-02-18','Beam Commissioning'),
('2021-02-23','2021-02-23','Beam Commissioning'),
('2021-02-25','2021-02-26','Beam Commissioning');

INSERT INTO detail values(6,'Beam Transport to LEBT'),(6,'Beam Transport to MEBT');
INSERT INTO shifter values(6, 'Chung, Yeon Sei','Beam Transport',3,1,1),
(6, 'Kim, Gi Dong','Beam Transport',3,2,0),
(6, 'Kwon, Jangwon','Beam Transport',3,3,0),
(6, 'Kim, Hyung Jin, Jangwon','Beam Transport',3,4,0),
(6, 'Jin, Hyun Chang','Beam Physics',4,1,0),
(6, 'Jang, Ji Ho','Beam Physics',4,2,0),
(6, 'Son, Changwook','Accelerator Control',1,1,0),
(6, 'Park, MiJeong','Accelerator Control',1,2,0),
(6, 'Lee, SangIl','Accelerator Control',1,3,0);


INSERT INTO detail values(7,'Timing and FPS Test');
INSERT INTO shifter values(7, 'Son, Changwook','Accelerator Control',4,1,0),
(7, 'Park, MiJeong','Accelerator Control',4,2,1),
(7, 'Lee, SangIl','Accelerator Control',4,3,0),
(7, 'Kim, YongHak','Accelerator Control',4,4,0),
(7, 'Choi, Yong Jun','Accelerator Control',4,5,0);

INSERT INTO detail values(8,'Pulse Beam Test'),(8,'250us Pluse Beam to MEBT'),(8,'Beam Steering');
INSERT INTO shifter values(8, 'Chung, Yeon Sei','Beam Transport',3,1,1),
(8, 'Kim, Gi Dong','Beam Transport',3,2,0),
(8, 'Kim, Hyung Jin, Jangwon','Beam Transport',3,4,0),
(8, 'Park, Burm Sik','Beam Transport',3,5,0),
(8, 'Woo, Hyung Joo','Beam Transport',3,6,0),
(8, 'Kwon, Jangwon','Beam Transport',3,3,0),
(8, 'Jin, Hyun Chang','Beam Physics',4,1,0),
(8, 'Jang, Ji Ho','Beam Physics',4,2,0),
(8, 'Son, Changwook','Accelerator Control',1,1,0),
(8, 'Park, MiJeong','Accelerator Control',1,2,0),
(8, 'Lee, SangIl','Accelerator Control',1,3,0),
(8, 'Kim, YongHak','Accelerator Control',2,1,0),
(8, 'Choi, Yong Jun','Accelerator Control',2,2,0),
(8, 'Seol, Kyung Tae','SCRF',4,3,0),
(8, 'Lee, DoYoon','SCRF',4,4,0),
(8, 'Son, KiTaek','SCRF',4,5,0);

