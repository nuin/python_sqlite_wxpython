CREATE TABLE sample (
  idsample INTEGER PRIMARY KEY AUTOINCREMENT,
  identification TEXT NULL,
  date DATE NULL,
  sampletype INTEGER UNSIGNED NULL,
  source INTEGER UNSIGNED NULL,
  cryotubes INTEGER UNSIGNED NULL,
  pathology BOOL NULL,
  rnaex BOOL NULL,
  dnaex BOOL NULL,
  comments LONGTEXT NULL,
  refs LONGTEXT NULL,
  nitrogen TEXT NULL,
  surgery INTEGER UNSIGNED NULL
);

CREATE TABLE bac (
  idbac INTEGER PRIMARY KEY AUTOINCREMENT,
  date DATE NULL,
  clone TEXT NULL,
  source TEXT NULL,
  location TEXT NULL,
  start INTEGER UNSIGNED NULL,
  endpos INTEGER UNSIGNED NULL,
  gene TEXT NULL,
  genelink TEXT NULL,
  dnaex TEXT NULL,
  validation BOOL NULL,
  pcr BOOL NULL,
  refs TEXT NULL
);

CREATE TABLE sampletype (
  idtype INTEGER PRIMARY KEY AUTOINCREMENT,
  sample_idsample INTEGER UNSIGNED NOT NULL,
  stype TEXT NULL,
  INDEX sampletype_FKIndex1(sample_idsample),
  FOREIGN KEY(sample_idsample)
    REFERENCES sample(idsample)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE suspension (
  idsuspension INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  sample_idsample INTEGER UNSIGNED NOT NULL,
  date DATE NULL,
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
  ref TEXT NULL,
  PRIMARY KEY(idsuspension),
  INDEX suspension_FKIndex1(sample_idsample),
  FOREIGN KEY(sample_idsample)
    REFERENCES sample(idsample)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE source (
  idsource INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  sample_idsample INTEGER UNSIGNED NOT NULL,
  name TEXT NULL,
  PRIMARY KEY(idsource),
  INDEX source_FKIndex1(sample_idsample),
  FOREIGN KEY(sample_idsample)
    REFERENCES sample(idsample)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE dna (
  iddna INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  sample_idsample INTEGER UNSIGNED NOT NULL,
  date DATE NULL,
  concentration FLOAT NULL,
  tubes INTEGER UNSIGNED NULL,
  location INTEGER UNSIGNED NULL,
  exmethod TEXT NULL,
  rnase BOOL NULL,
  refs TEXT NULL,
  PRIMARY KEY(iddna),
  INDEX dna_FKIndex1(sample_idsample),
  FOREIGN KEY(sample_idsample)
    REFERENCES sample(idsample)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE glycerol (
  idglycerol INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  bac_idbac INTEGER UNSIGNED NOT NULL,
  date DATE NULL,
  freezer INTEGER UNSIGNED NULL,
  box INTEGER UNSIGNED NULL,
  row_2 INTEGER UNSIGNED NULL,
  PRIMARY KEY(idglycerol),
  INDEX glycerol_FKIndex1(bac_idbac),
  FOREIGN KEY(bac_idbac)
    REFERENCES bac(idbac)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);

CREATE TABLE rna (
  idrna INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  sample_idsample INTEGER UNSIGNED NOT NULL,
  date DATE NULL,
  extraction BOOL NULL,
  tubes INTEGER UNSIGNED NULL,
  exmethod INTEGER UNSIGNED NULL,
  dnase BOOL NULL,
  refs TEXT NULL,
  PRIMARY KEY(idrna),
  INDEX rna_FKIndex1(sample_idsample),
  FOREIGN KEY(sample_idsample)
    REFERENCES sample(idsample)
      ON DELETE NO ACTION
      ON UPDATE NO ACTION
);


