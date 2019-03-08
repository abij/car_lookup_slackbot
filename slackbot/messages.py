
def _get_owner_from_details(details, default="-"):
    result = default
    if details.get('owner_slackid') is not None:
        result = '<@{}>'.format(details.get('owner_slackid'))
    elif details.get('owner_name') is not None:
        result = details.get('owner_name')
    return result


lookup_no_details_found = 'No details found...'


def lookup_found_with_details(kenteken, details):
    car_type = details.get('handelsbenaming') or '-'
    car_brand = details.get('merk') or '-'
    owner = _get_owner_from_details(details)
    apk = details.get('vervaldatum_apk') or '-'
    price = details.get('catalogusprijs') or '-'

    return '''Lookup of {kenteken}: *{car_type}* of brand *{car_brand}*
    > • Owner: {owner}
    > • Price: {price} 
    > • APK expires: {apk}'''.format(kenteken=kenteken, car_type=car_type, car_brand=car_brand,
                                     owner=owner, price=price, apk=apk)


comment_no_plate_found = "No plates were found. Try `/kenteken [license plate]` " \
                         "if _you_ can OCR a license plate from that image."


def comment_found_with_details(plate, confidence, details):
    car_type = details.get('handelsbenaming') or '-'
    car_brand = details.get('merk') or '-'
    owner = _get_owner_from_details(details)
    apk = details.get('vervaldatum_apk') or '-'
    price = details.get('catalogusprijs') or '-'

    return ''':mega: Found licence plate *{plate}* _(confidence {confidence:.2f})_!
    It's a *{car_type}* of brand *{car_brand}*
    > • Owner: {owner}
    > • Price: {price} 
    > • APK expires: {apk}'''.format(plate=plate, confidence=confidence, car_type=car_type,
                                     owner=owner, car_brand=car_brand, price=price, apk=apk)


def comment_found_no_details(plate, confidence):
    return 'I found *{plate}* _(confidence {confidence:.2f})_, but no extra info associated with it...'.format(
        plate=plate, confidence=confidence)


def comment_found_but_skipping(kenteken, confidence, is_valid):
    if is_valid:
        msg_pattern = "is valid NL pattern"
    else:
        msg_pattern = "is NOT a valid NL pattern"

    return "Skipping licence plate '{kenteken}', low confidence ({confidence:.2f}) and {msg_pattern}.".format(
        kenteken=kenteken, confidence=confidence, msg_pattern=msg_pattern)
