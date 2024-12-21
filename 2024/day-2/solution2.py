def report_is_safe(report):
	growth = report[0] - report[1]

	for x in range(1, len(report)):
		diff = report[x-1] - report[x]

		if diff * growth < 0:
			return False

		if diff < 0:
			diff *= -1

		if not 1 <= diff <= 3:
			return False
	return True

safe_reports = 0

with open("input", "r") as file:
	for reports in file:
		report = [ int(x) for x in reports.split() ]
		if report_is_safe(report):
			safe_reports += 1
		else:
			for x in range(0, len(report)):
				report_copy = report[:]
				report_copy.pop(x)
				if report_is_safe(report_copy):
					safe_reports += 1
					break

print(safe_reports)
