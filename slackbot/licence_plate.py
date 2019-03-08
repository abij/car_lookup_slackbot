import re

# based on https://github.com/openalpr/openalpr/blob/master/runtime_data/postprocess/eu.patterns
nl_valid_patterns = [re.compile(r'[A-Z]{2}\d{4}'),
                     re.compile(r'\d{4}[A-Z]{2}'),
                     re.compile(r'\d{2}[A-Z]{2}\d{2}'),
                     re.compile(r'[A-Z]{2}[A-Z]{2}'),
                     re.compile(r'[A-Z]{4}\d{2}'),
                     re.compile(r'\d{2}[A-Z]{4}'),
                     re.compile(r'\d{2}[A-Z]{3}\d'),
                     re.compile(r'\d[A-Z]{3}\d{2}'),
                     re.compile(r'[A-Z]{2}\d{3}[A-Z]'),
                     re.compile(r'[A-Z]\d{3}[A-Z]{2}'),
                     re.compile(r'[A-Z]{3}\d{2}[A-Z]'),
                     re.compile(r'[A-Z]\d{2}[A-Z]{3}'),
                     re.compile(r'\d[A-Z]{2}\d{3}'),
                     re.compile(r'\d{3}[A-Z]{2}\d')]


def normalize(plate):
    return plate.strip().replace('-', '').upper()


def is_valid(plate):
    plate = normalize(plate)
    if len(plate) != 6:
        return False

    for p in nl_valid_patterns:
        if re.match(p, plate):
            return True

    return False
