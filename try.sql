-- Active: 1670048003557@@127.0.0.1@3306

BEGIN TRANSACTION;

CREATE TABLE
    subjects(
        year INT NOT NULL,
        subject_id TEXT PRIMARY KEY NOT NULL,
        subject TEXT NOT NULL,
        hours INT NOT NULL,
        staff_id TEXT NOT NULL,
        LAB INT NOT NULL
    );

INSERT INTO subjects
VALUES (
        1,
        'DP-2',
        'Developmental Psychology – II',
        5,
        'NAC',
        0
    );

INSERT INTO subjects
VALUES (
        1,
        'GP-2',
        'General Psychology – II',
        5,
        'RUK',
        0
    );

INSERT INTO subjects
VALUES (
        1,
        'PS-1',
        'Psychological Statistics - I',
        5,
        'SRS',
        0
    );

INSERT INTO subjects VALUES(1,'TAM-1','TAMIL',6,'LANG-1',0);

INSERT INTO subjects VALUES(1,'ENG-1','ENGLISH',6,'LANG-2',0);

INSERT INTO subjects
VALUES (
        1,
        'EP-1',
        'Experimental Psychology: Practical-I ',
        3,
        'VAO',
        1
    );

INSERT INTO subjects
VALUES (
        2,
        'AP-1',
        'Abnormal Psychology-I',
        5,
        'KRT',
        0
    );

INSERT INTO subjects VALUES(2,'RM','Research Methodology',5,'NAC',0);

INSERT INTO subjects
VALUES (
        2,
        'LAP',
        'Legal Aspects of Psychology',
        5,
        'SRS',
        0
    );

INSERT INTO subjects VALUES(2,'TAM-2','TAMIL',5,'LANG-1',0);

INSERT INTO subjects VALUES(2,'LANG-2','ENGLISH',5,'LANG-2',0);

INSERT INTO subjects
VALUES (
        2,
        'EP-3',
        'Experimental Psychology: Practical-III',
        3,
        'KAN',
        1
    );

INSERT INTO subjects
VALUES (
        2,
        'EDC:IS',
        'Information Security',
        2,
        'EDC',
        0
    );

INSERT INTO subjects
VALUES (
        3,
        'FMCS',
        'Fundamentals of Marketing and Consumer Behavior',
        5,
        'RUK',
        0
    );

INSERT INTO subjects
VALUES (
        3,
        'FC',
        'Fundamentals of Counselling',
        5,
        'ANU',
        0
    );

INSERT INTO subjects
VALUES (
        3,
        'FHP',
        'Fundamentals of Health Psychology',
        5,
        'KAA',
        0
    );

INSERT INTO subjects
VALUES (
        3,
        'PEC',
        'Psychology of Exceptional Children',
        5,
        'KAN',
        0
    );

INSERT INTO subjects
VALUES (
        3,
        'RP',
        'Rehabilitation Psychology',
        5,
        'VAO',
        0
    );

INSERT INTO subjects
VALUES (
        3,
        'EP-5',
        'Experimental Psychology: Practical – V: Case Analysis',
        5,
        'KRT',
        1
    );

INSERT INTO subjects
VALUES (
        4,
        'OB',
        'Organizational Behavior',
        5,
        'ANU',
        0
    );

INSERT INTO subjects VALUES(4,'CP','Clinical Psychology',5,'RUK',0);

INSERT INTO subjects
VALUES (
        4,
        'PTD',
        'Psychological Testing & Diagnosis',
        5,
        'KAA',
        0
    );

INSERT INTO subjects
VALUES (
        4,
        'BM',
        'Behavior Modification',
        5,
        'VAO',
        0
    );

INSERT INTO subjects
VALUES (
        4,
        'PA',
        'Psychological Assessment: Practical II',
        5,
        'SRS',
        1
    );

INSERT INTO subjects VALUES(4,'EDC:CS','Cyber Security',5,'EDC',0);

INSERT INTO subjects
VALUES (
        5,
        'OB-2',
        'Organizational Behavior - II',
        5,
        'NAC',
        0
    );

INSERT INTO subjects
VALUES (
        5,
        'MCB',
        'Marketing & Consumer Behavior',
        5,
        'KAN',
        0
    );

INSERT INTO subjects
VALUES (
        5,
        'CS',
        'Counseling Psychology',
        5,
        'KRT',
        0
    );

INSERT INTO subjects VALUES(5,'HP','Health Psychology',4,'ANU',0);

INSERT INTO subjects VALUES(5,'CA','Case Analysis',3,'KAA',1);

INSERT INTO subjects
VALUES (
        5,
        'EDC:PS',
        'Professional Skills',
        4,
        'EDC',
        0
    );

INSERT INTO subjects
VALUES (
        5,
        'EDC:HRM',
        'Human Resource Management',
        4,
        'EDC',
        0
    );

CREATE TABLE
    staffs(
        staff_id TEXT PRIMARY KEY NOT NULL,
        staff_name TEXT NOT NULL,
        subject_id TEXT NOT NULL
    );

INSERT INTO staffs VALUES('NAC','Naachimuthu','DP-2|RM|OB-2');

INSERT INTO staffs VALUES('RUK','Rukmani','GP-2|FMCS|CP');

INSERT INTO staffs VALUES('SRS','Saraswathi','LAP|PS-1|LAB:PA');

INSERT INTO staffs VALUES('KAN','Kanchana','PEC|MCB|LAB:EP-3');

INSERT INTO staffs VALUES('KRT','Karthikeyan','AP-1|LAB:EP-5|CS');

INSERT INTO staffs VALUES('ANU','Anu','OB|FC|HP');

INSERT INTO staffs VALUES('VAO','vaodehi','LAB:EP-1|RP|BM');

INSERT INTO staffs VALUES('KAA','Kaalakeyan','FHP|PTD|LAB:CA');

INSERT INTO staffs
VALUES (
        'EDC',
        'other dpt',
        'EDC:IS|EDC:CS|EDC:PS|EDC:HRM'
    );

COMMIT;