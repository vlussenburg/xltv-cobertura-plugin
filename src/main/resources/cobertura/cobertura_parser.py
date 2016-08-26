import json
#from parser.xunit import throw_if_some_failed, parse_last_modified, parse_junit_test_results, open_file

def cobertura_validate_files(files):
    if not (len(files) == 1 and str(files[0]).endswith("cobertura.xml")):
        raise NameError("Expection a single cobertura.xml, got: '%s'" % str(files))

def cobertura_iterate_test_cases(file):
    """
    Iterate all test cases found in `file`.
    :param file:
    :return: a list/iterator of tuples (test case node, test hierarchy path)
    """
    with open_file(file) as data_file:
        features = json.load(data_file)
        for feature in features:
            for element in feature.get("elements", []):
                if element["type"] == 'scenario':
                    yield (element, (feature['name'], element['name'], str(element['line'])))


def cobertura_duration(splitResult):
    steps = splitResult["steps"]
    duration = 0
    for step in steps:
        duration = duration + long(step["result"].get("duration", 0))

    return int(duration / 1000000)

def cobertura_result(scenario):
    return "PASSED"

def cobertura_last_modified(file):
    return file.lastModified()

def main(files, result_holder):
    cobertura_validate_files(files)

    last_modified = parse_last_modified(files, extract_last_modified=cobertura_last_modified)

    print 'LAST MOD', last_modified, test_run_historian.isKnownKey(str(last_modified))
    if not test_run_historian.isKnownKey(str(last_modified)):
        events = []
        print 'built run with events', events
    else:
        events = []

    # Result holder should contain a list of test runs. A test run is a list of events

    result_holder.result = [events] if events else []

try:
    main(files, result_holder)
except NameError:
    print "Could not find files or result_holder - running in test mode?"

