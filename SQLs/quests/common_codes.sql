-- DDL FROM JH
CREATE TABLE `CAR_INFO` (
	`PK_CAR_ID`	VARCHAR(50)	NOT NULL,
	`CAR_NAME`	VARCHAR(255)	NULL,
	`FK_COMMON_CODES_COMPANY`	VARCHAR(50)	NULL,
	`FK_COMMON_CODES_YEARS`	VARCHAR(50)	NULL
);
CREATE TABLE `CAR_COMMON_CODES` (
	`FK_COMMON_CODES`	VARCHAR(50)	NOT NULL,
	`PART_NAME`	VARCHAR(255)	NULL,
	`NAME`	VARCHAR(255)	NULL
);
ALTER TABLE `CAR_INFO` ADD CONSTRAINT `PK_CAR_INFO` PRIMARY KEY (
	`PK_CAR_ID`
);
ALTER TABLE `CAR_COMMON_CODES` ADD CONSTRAINT `PK_COMMON_CODES` PRIMARY KEY (
	`FK_COMMON_CODES`
);

-- INSERT FROM CHATGPT
INSERT INTO CAR_INFO (PK_CAR_ID, CAR_NAME, FK_COMMON_CODES_COMPANY, FK_COMMON_CODES_YEARS)
VALUES
('PK_CAR_01', '소나타', 'FK_CP_01', 'FK_Y_01'),
('PK_CAR_02', '쏘렌토', 'FK_CP_02', 'FK_Y_02'),
('PK_CAR_03', '카마로', 'FK_CP_03', 'FK_Y_03'),
('PK_CAR_04', '3시리즈', 'FK_CP_04', 'FK_Y_04'),
('PK_CAR_05', 'E클래스', 'FK_CP_05', 'FK_Y_05'),
('PK_CAR_06', '소나타', 'FK_CP_01', 'FK_Y_02');

INSERT INTO CAR_COMMON_CODES (FK_COMMON_CODES, PART_NAME, NAME)
VALUES
('FK_CP_01', 'CP', '현대'),
('FK_CP_02', 'CP', '기아'),
('FK_CP_03', 'CP', '쉐보레'),
('FK_CP_04', 'CP', 'BMW'),
('FK_CP_05', 'CP', '벤츠'),
('FK_Y_01', 'YEAR', '2020'),
('FK_Y_02', 'YEAR', '2018'),
('FK_Y_03', 'YEAR', '2019'),
('FK_Y_04', 'YEAR', '2017'),
('FK_Y_05', 'YEAR', '2021');

-- JOIN
SELECT CAR_INFO.PK_CAR_ID, CAR_INFO.CAR_NAME,  CCC_CP.NAME, CCC_Y.NAME
FROM CAR_INFO
JOIN CAR_COMMON_CODES CCC_CP
ON CCC_CP.FK_COMMON_CODES = CAR_INFO.FK_COMMON_CODES_COMPANY
JOIN CAR_COMMON_CODES CCC_Y
ON CCC_Y.FK_COMMON_CODES = CAR_INFO.FK_COMMON_CODES_YEARS