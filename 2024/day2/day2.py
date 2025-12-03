def validate_report(report):
    report_levels = report.split(' ')
    report_levels = [int(i) for i in report_levels]

    direction = 'increasing' if report_levels[0] < report_levels[1] else 'decreasing'
    
    for i in range(len(report_levels) - 1):
        if report_levels[i] > report_levels[i + 1]:
            if direction == 'increasing':
                return False
            else:
                if report_levels[i] - report_levels[i + 1] > 0:
                    if report_levels[i] - report_levels[i + 1] < 4:
                        pass
                    else:
                        return False
                else:
                    return False
        else:
            if direction == 'decreasing':
                return False
            else:
                if report_levels[i + 1] - report_levels[i] > 0:
                    if report_levels[i + 1] - report_levels[i] < 4:
                        pass
                    else:
                        return False
                else:
                    return False
    
    return True

def part2(report):
    report_levels = report.split(' ')
    report_levels = [int(i) for i in report_levels]

    direction = 'increasing' if report_levels[0] < report_levels[1] else 'decreasing'
    
    bad_report = False
    for i in range(len(report_levels) - 1):
        if report_levels[i] > report_levels[i + 1]:
            if direction == 'increasing':
                return False
            else:
                if report_levels[i] - report_levels[i + 1] > 0:
                    if report_levels[i] - report_levels[i + 1] < 4:
                        pass
                    else:
                        if not bad_report:
                            bad_report = True
                        else:
                            return False
                else:
                    if not bad_report:
                        bad_report = True
                    else:
                        return False
        else:
            if direction == 'decreasing':
                return False
            else:
                if report_levels[i + 1] - report_levels[i] > 0:
                    if report_levels[i + 1] - report_levels[i] < 4:
                        pass
                    else:
                        if not bad_report:
                            bad_report = True
                        else:
                            return False
                else:
                    if not bad_report:
                        bad_report = True
                    else:
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
        if validate_report(report):
            safe_reports.append(report)
        else:
            unsafe_reports.append(report)

    print(len(safe_reports))

    safe_reports = []

    for report in inputs:
        if part2(report):
            safe_reports.append(report)
        else:
            unsafe_reports.append(report)

    print(len(safe_reports))
    print(unsafe_reports)