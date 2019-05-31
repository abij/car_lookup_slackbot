def _get_owner_from_details(details, default=None):
    result = default
    if details.get('owner_slackid') is not None:
        return '<@{}>'.format(details.get('owner_slackid'))
    elif details.get('owner_name') is not None:
        return details.get('owner_name')
    return result


command_car_usage = 'Lookup car details including the owner (if known):\n' \
                    '`AA-12-BB`  _(dashes are optional)_\n' \
                    '`tag AA-12-BB` _(register your car)_\n' \
                    '`tag AA-12-BB @slackid` _(register someone else)_\n' \
                    '`tag AA-12-BB "Jack Sparrow"` _(register someone on name)_\n' \
                    '`untag AA-12-BB` _(remove this entry)_\n' \

command_tag_usage = 'Register or unregister the owner of a car:\n' \
                ' `tag AA-12-BB`  _(you are the owner)_\n' \
                ' `tag AA-12-BB @thatguy`  _(or someone else with a slack handle)_\n' \
                ' `tag AA-12-BB "The great pirate"`  _(or a quoted string defining the owner)_\n' \
                ' `untag AA-12-BB`  _(removes this car)_'


def command_invalid_owner(owner):
    return 'Invalid owner "{}" _(must be double-quoted, between 3 - 32 chars and normal text chars)_'.format(owner)


def command_invalid_usage(nr_arguments):
    return 'Invalid nr of arguments. Expects at most 3, given {}.\nUsage:\n{}'.format(
        nr_arguments, command_car_usage)


def command_invalid_licence_plate(text):
    return 'Input ({}) does not look like a valid licence plate (NL-patterns)'.format(text)


def command_tag_added(plate, user_id=None, owner=None):
    if owner:
        return 'Added {} to "{}"'.format(plate, owner)
    else:
        return 'Added {} to <{}>'.format(plate, user_id)


def command_untag(plate):
    return 'Removed the licence plate {}'.format(plate)


lookup_no_details_found = 'No details found...'


def lookup_found_with_details(plate, details):
    car_type = details.get('handelsbenaming') or '-'
    car_brand = details.get('merk') or '-'
    owner = _get_owner_from_details(details) or '- _(Use `/car tag` to add the owner)_'
    apk = details.get('vervaldatum_apk') or '-'
    price = details.get('catalogusprijs') or '-'
    acceleration = details.get('acceleration') or '-'

    if isinstance(price, int):
        price = '€ {:,d}'.format(price).replace(',', '.')

    return '''Lookup of {plate}: *{car_brand} {car_type}*
     • Owner: {owner}
     • Price: {price} 
     • 0-100: {acceleration}
     • APK expires: {apk}'''.format(plate=plate, car_type=car_type, car_brand=car_brand,
                                    owner=owner, price=price, acceleration=acceleration, apk=apk)


comment_no_plate_found = "No plates were found. Try `/car [license plate]` " \
                         "if _you_ can OCR a license plate from that image."


def comment_found_with_details(plate, confidence, details):
    car_type = details.get('handelsbenaming') or '-'
    car_brand = details.get('merk') or '-'
    owner = _get_owner_from_details(details) or '- _(Use `/car tag` to add the owner)_'
    apk = details.get('vervaldatum_apk') or '-'
    price = details.get('catalogusprijs') or '-'
    acceleration = details.get('acceleration') or '-'

    if isinstance(price, int):
        price = '€ {:,d}'.format(price).replace(',', '.')

    return ''':mega: Found *{plate}*, it's a *{car_brand} {car_type}*! _(confidence {confidence:.2f})_
     • Owner: {owner}
     • Price: {price} 
     • 0-100: {acceleration}
     • APK expires: {apk}'''.format(plate=plate, confidence=confidence, car_type=car_type,
                                    owner=owner, car_brand=car_brand, price=price, acceleration=acceleration, apk=apk)


def comment_found_no_details(plate, confidence):
    return 'I found *{plate}* _(confidence {confidence:.2f})_, but no extra info associated with it...'.format(
        plate=plate, confidence=confidence)


def comment_found_but_skipping(plate, confidence, threshold, is_valid):
    if not is_valid:
        return "Skipping licence plate '{plate}', it's NOT a valid NL pattern _(confidence {confidence:.2f})_".format(
            plate=plate, confidence=confidence)

    return "Skipping licence plate '{plate}', too low confidence ({confidence:.2f} < {threshold:.2f})".format(
        plate=plate, confidence=confidence, threshold=threshold)

