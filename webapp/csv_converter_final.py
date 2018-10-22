import sys
import re
import csv



def load_from_resort_csv_file(csv_file_name):
	csv_file = open(csv_file_name, encoding='utf-8')
	reader = csv.reader(csv_file)

	date_status_list = []
	date_status = {}

	for row in reader:

		date_list_strings = row[0].split("-")
		day = day_converter(date_list_strings[0])
		month = month_converter(date_list_strings[1])
		year = year_converter(date_list_strings[2])
		date_string_final = year + month + day



		twenty_four_hr_snowfall = take_off_cm(row[1])
		snowfall_to_date = take_off_cm(row[2])
		base_depth = take_off_cm(row[3])


		date_status = {'date': date_string_final, '24_hr_snowfall': twenty_four_hr_snowfall, 'snowfall_to_date': snowfall_to_date, 'base_depth': base_depth}


		date_status_list.append(date_status)
	return date_status_list


def take_off_cm(cm_string):
	new_string = cm_string.split(" ")
	string_without_cm = new_string[0]
	return string_without_cm


def day_converter(day_string):
	if len(day_string) == 1:
		day = "0" + day_string
	else:
		day = day_string
	return day

def year_converter(year_string):
	year_int = int(year_string) + 2000
	output_year = str(year_int)
	return output_year

def month_converter(month_string):
	month_string = month_string.lower()
	month_dict = {"jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05", "jun": "06", "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12"}
	month_output = month_dict[month_string]
	return month_output



def save_new_resort_csv_file(date_status_list, csv_file_name):
	output_file = open(csv_file_name, 'w', encoding='utf-8')
	writer = csv.writer(output_file)
	for date in date_status_list:
		new_date_status_row = [date['date'], date['24_hr_snowfall'], date['snowfall_to_date'], date['base_depth']]
		writer.writerow(new_date_status_row)
	output_file.close()

if __name__ == '__main__':
	jackson_hole = load_from_resort_csv_file("Jackson_Hole.csv")
	telluride = load_from_resort_csv_file("Telluride.csv")
	whistler_blackcomb = load_from_resort_csv_file("Whistler_Blackcomb.csv")
	snowbird = load_from_resort_csv_file("Snowbird.csv")

	save_new_resort_csv_file(jackson_hole, 'Jackson_Hole_Final.csv')
	save_new_resort_csv_file(telluride, 'Telluride_Final.csv')
	save_new_resort_csv_file(whistler_blackcomb, "Whistler_Final.csv")
	save_new_resort_csv_file(snowbird, "Snowbird_Final.csv")
