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


def command_invalid_owner(owner, min_chars=3, max_chars=32):
    return 'Invalid owner "{}" _(must be double-quoted, between {} - {} chars and normal text chars)_'.format(
        owner, min_chars, max_chars)


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


def lookup_no_details_found(plate):
    return '`/car {}` lookup: No details found...'.format(plate)


comment_no_plate_found = "No plates were found. Try `/car [license plate]` " \
                         "if _you_ can OCR a license plate from that image."


def found_with_details(plate, details, prefix, confidence=None):
    model = details.get('model') or '-'
    car_brand = details.get('brand') or '-'

    # Optional fields:
    owner = _get_owner_from_details(details)
    price = details.get('price')
    acceleration = details.get('acceleration')
    # apk = details.get('apk')
    # bpm = details.get('bpm')
    message = "{prefix}, it's a <https://autorapport.finnik.nl/kenteken/{plate}|*{car_brand} {model}*>!".format(prefix=prefix ,plate=plate, model=model, car_brand=car_brand)

    if confidence:
        message += " _({confidence:.1f}%)_".format(confidence=confidence)

    if owner:
        message += "\n:person_raising_hand: {owner}".format(owner=owner)
    else:
        message += "\n:person_shrugging: _(`/car tag` to add the owner)_"

    if price:
        if isinstance(price, int):
            price = '€ {:,d}'.format(price).replace(',', '.')
        message += "\n💶 {price}".format(price=price)

    if acceleration:
        if acceleration < 7:
            message += "\n0-100: {acceleration} sec :rocket:".format(acceleration=acceleration)
        elif acceleration < 10:
            message += "\n0-100: {acceleration} sec :racing_car:".format(acceleration=acceleration)
        elif acceleration < 12:
            message += "\n0-100: {acceleration} sec :red_car:".format(acceleration=acceleration)
        elif acceleration < 15:
            message += "\n0-100: {acceleration} sec :blue_car:".format(acceleration=acceleration)
        else:
            message += "\n0-100: {acceleration} sec :motorized_wheelchair:".format(acceleration=acceleration)

    return message


def comment_found_no_details(plate, confidence):
    return 'I found *{plate}* _(confidence {confidence:.1f})_, but no extra info associated with it...'.format(
        plate=plate, confidence=confidence)


def comment_found_but_skipping(plate, confidence, threshold, is_valid):
    if not is_valid:
        return "Skipping licence plate '{plate}', it's NOT a valid NL pattern _(confidence {confidence:.2f})_".format(
            plate=plate, confidence=confidence)

    return "Skipping licence plate '{plate}', too low confidence ({confidence:.2f} < {threshold:.2f})".format(
        plate=plate, confidence=confidence, threshold=threshold)

