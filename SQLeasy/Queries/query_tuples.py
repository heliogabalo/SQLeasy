sql = """
  INSERT INTO teacher (teacher_id, first_name, last_name, language_1, language_2, dob, tax_id, phone_no)
  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

deafult_val = [
    (7, 'Hunk', 'Dodson', 'ENG', None, '1991-12-23', 11111, '+09812734098'),
    (8, 'Funk', 'Bolson', 'EKR', 'ENG', '1491-15-16', 22222, '+09219014098')
]


## id is always null, omit them.
#
# or ... use INSERT INTO dummy_table VALUES
#                      (tuples_here),
#                      (tuples_here),
#                      (tuples_here);
# Integer values as defined the telephone field, it doesn't accept white
# separated numbers(661 12 12 12) <= wrong.
# Remember that you are passing PYTHON STRUCTURES!
val = [
(None, 'Sobime', 'c/Sant Josep 123 Pg. Ind. EL PLA', 'Fabricación grifería', 'dummy_notes', 936660689, 1),
(None, 'Distribuciones Delfín García', 'desconocida', 'Mayoristas snacks', 'dummy_notes dummy_notes', 937906304, 0),
(None, 'Pneumática Leopoldo', 'Plaza del Vapor 174 P.I Les Guixeres', 'compresores', 'dummy_notes', 937906304, 1),
(None, 'equalec', 'c/Electrónica 12 P.I. Les Guixeres', 'E. Quadres i Autom.', 'dummy_notes', 933810842, 1),
(None, 'LabProcess', 'c/Electrónica 23 P.I. Les Guixeres', 'www.labproceses', 'dummy_notes dummy_notes', 935406033, 1),
(None, 'vink plastics', 'c/Bosquerons 3 nave 1', 'Plásticos', 'dummy_notes', 935683961, 1),
(None, 'Ana Campoy', 'Plaza del Vapor 5-6C. P.I Les Guixeres', 'Craltech Electrónica', 'dummy_notes', 936093706, 1),
(None, 'Envasados Torner', 'c/Cobalt 40 Nau', 'Envasados a terceros', 'dummy_notes', 934801690, 1)
]


# (NULL, 'dummy_name', 'dummy_address', 'dummy_industry', 'dummy_notes', 'dummy_telephone', BOOLEAN)
