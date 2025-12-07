def validate_report(report):

    direction = 'increasing' if report_levels[0] < report_levels[-1] else 'decreasing'
    
    for i in range(len(report_levels) - 1):
        if report_levels[i] > report_levels[i + 1]:
            if direction == 'increasing':
                return False, i
            else:
                if report_levels[i] - report_levels[i + 1] > 0:
                    if report_levels[i] - report_levels[i + 1] < 4:
                        pass
                    else:
                        return False, i
                else:
                    return False, i
        else:
            if direction == 'decreasing':
                return False, i
            else:
                if report_levels[i + 1] - report_levels[i] > 0:
                    if report_levels[i + 1] - report_levels[i] < 4:
                        pass
                    else:
                        return False, i
                else:
                    return False, i
    
    return True, -1

def validate_direction(report):
    direction = None
    for i in range(len(report) - 1):
        if report[i] > report[i + 1]:
            if not direction:
                direction = 'decreasing'
            else:
                if direction != 'decreasing':
                    return False, i
        else:
            if not direction:
                direction = 'increasing'
            else:
                if direction != 'increasing':
                    return False, i
    return True, -1

def create_differences(report):
    differences = []
    for i in range(len(report) - 1):
        differences.append(report[i + 1] - report[i])
    return differences

def difference_validation(differences):
    test = [i for i in differences if i > 3 or i < -3]

    return test

def validate_range(differences, report, first_run = True):    
    
    # test for existence of 0, meaning sequential numbers
    if 0 in differences:
        if differences.count(0) > 1:
            return False
        
    test = difference_validation(differences)
    if len(test) > 1:
        return False
    if len(test) == 1:
        report = [i for i in report if differences.index(test[0]) + 1 != i]
        differences = create_differences(report)
        test = difference_validation(differences)
        if test:
            return False
        
    return True
            



if __name__ == '__main__':

    inputs_path = r"C:\Users\skyle\Documents\dev\AoC\2024\day2\input.txt"

    inputs = []
    with open(inputs_path, 'r', encoding='utf-8') as fo:
        inputs = [r.replace("\n", "") for r in fo.readlines()]

    safe_reports = []
    unsafe_reports = []

    for report in inputs:
        report_levels = report.split(' ')
        report_levels = [int(i) for i in report_levels]
        result, bad_index = validate_report(report_levels)
        if result:
            safe_reports.append(report)
        else:
            unsafe_reports.append(report)

    print(len(safe_reports))

    direction_safe_reports = []
    safe_reports = []
    unsafe_reports = []

    for report in inputs:
        report_levels = report.split(' ')
        report_levels = [int(i) for i in report_levels]

        differences = create_differences(report_levels)
        result = validate_range(differences, report_levels)

    print(len(safe_reports))
    for report in unsafe_reports:
        print(report)