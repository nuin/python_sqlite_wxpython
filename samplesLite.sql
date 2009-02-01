CREATE TABLE sample (
  idsample INTEGER UNSIGNED NOT NULL PRIMARY KEY,
  identification TEXT NULL,
  sdate DATE NULL,
  sampletype INTEGER UNSIGNED NULL,
  source INTEGER UNSIGNED NULL,
  cryotubes INTEGER UNSIGNED NULL,
  pathology BOOL NULL,
  rnaex BOOL NULL,
  dnaex BOOL NULL,
  comments TEXT NULL,
  refs LONGTEXT NULL,
  nitrogen TEXT NULL,
  surgery INTEGER UNSIGNED NULL
);

CREATE TABLE bac (
  idbac INTEGER UNSIGNED NOT NULL PRIMARY KEY,
  sdate DATE NULL,
  clone TEXT NULL,
  source TEXT NULL,
  location TEXT NULL,
  startpos INTEGER UNSIGNED NULL,
  endpos INTEGER UNSIGNED NULL,
  gene TEXT NULL,
  genelink TEXT NULL,
  dnaex TEXT NULL,
  validation BOOL NULL,
  pcr BOOL NULL,
  refs LONGTEXT NULL
);

CREATE TABLE sampletype (
  idtype INTEGER UNSIGNED NOT NULL PRIMARY KEY,
  sample_idsample INTEGER UNSIGNED NOT NULL,
  stype TEXT NULL,
  FOREIGN KEY(sample_idsample) REFERENCES sample(idsample)
);

CREATE TABLE suspension (
  idsuspension INTEGER UNSIGNED NOT NULL PRIMARY KEY,
  sample_idsample INTEGER UNSIGNED NOT NULL,
  sdate DATE NULL,
  susptype TEXT NULL,
  nitrogen BOOL NULL,
  nitrogeninfo TEXT NULL,
  colcemid TIME NULL,
  tubes INTEGER UNSIGNED NULL,
  location TEXT NULL,
  metaphase BOOL NULL,
  sky BOOL NULL,
  karyotype TEXT NULL,
  dna BOOL NULL,
  rna BOOL NULL,
  refs LONGTEXT NULL,
  FOREIGN KEY(sample_idsample) REFERENCES sample(idsample)
);

CREATE TABLE source (
  idsource INTEGER UNSIGNED NOT NULL PRIMARY KEY,
  sample_idsample INTEGER UNSIGNED NOT NULL,
  name TEXT NULL,
  FOREIGN KEY(sample_idsample)
    REFERENCES sample(idsample)
);

CREATE TABLE dna (
  iddna INTEGER UNSIGNED NOT NULL PRIMARY KEY,
  sample_idsample INTEGER UNSIGNED NOT NULL,
  sdate DATE NULL,
  concentration FLOAT NULL,
  tubes INTEGER UNSIGNED NULL,
  location INTEGER UNSIGNED NULL,
  exmethod TEXT NULL,
  rnase BOOL NULL,
  refs LONGTEXT NULL,
  FOREIGN KEY(sample_idsample)
    REFERENCES sample(idsample)

);

CREATE TABLE glycerol (
  idglycerol INTEGER UNSIGNED NOT NULL PRIMARY KEY,
  bac_idbac INTEGER UNSIGNED NOT NULL,
  sdate DATE NULL,
  freezer INTEGER UNSIGNED NULL,
  box INTEGER UNSIGNED NULL,
  row_2 INTEGER UNSIGNED NULL,
  FOREIGN KEY(bac_idbac)
    REFERENCES bac(idbac)
);

CREATE TABLE rna (
  idrna INTEGER UNSIGNED NOT NULL PRIMARY KEY,
  sample_idsample INTEGER UNSIGNED NOT NULL,
  sdate DATE NULL,
  extraction BOOL NULL,
  tubes INTEGER UNSIGNED NULL,
  exmethod INTEGER UNSIGNED NULL,
  dnase BOOL NULL,
  refs LONGTEXT NULL,
  FOREIGN KEY(sample_idsample)
    REFERENCES sample(idsample)
);


