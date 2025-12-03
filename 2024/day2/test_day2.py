import pytest

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

def test_part2_single_report():
    report = '80 80 81 80 82 83 84 88'

    result = part2(report)

    assert result