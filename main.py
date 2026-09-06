#!/usr/bin/python3

import os
import re
import pdftotext
import logging
from datetime import datetime


# Creates file containing logs from script run
def start_logging():
	logger = logging.getLogger(__name__)
	time = datetime.now().strftime("%d.%m.%y_%H:%M")
	logging.basicConfig(filename=f'invoice_processor_{time}.log', level=logging.INFO)
	logger.info('Logging started')
	return logger

# Opens document and reads it into string
def read_document_to_pdf(filename: str) -> str:
	with open(filename, "rb") as invoice_file:
		invoice_text = pdftotext.PDF(invoice_file)
	invoice_processor_logger.info(f"invoice file {filename} loaded successfully")
	return invoice_text

# Reads invoice data using regex
def split_data(invoice_text: str) -> dict:

	# searches for # followed by space and 4 or 5 digit number
	invoice_number = re.search("[#]\\s\\d{4,5}", invoice_text[0])

	# searches for date in mmm dd yyyy format
	# 3 letters, space, 1 or 2 digits, space and 4 digits
	invoice_date = re.search("\\D{3}\\s\\d{1,2},?\\s\\d{4}", invoice_text[0])

	# searches for "Total", then any amount of blank characters, dollar sign, any number of digits,
	# possible comma, at least 1 digit, decimal point and 2 digits

	# BUG: NEEDS FIX FOR AMOUNT 1,000,000.00 AND MORE
	
	invoice_total_amount = re.search("Total:\\s+\\$([\\d]*,?[\\d]+\\.\\d{2})", invoice_text[0])
	
	try:
		invoice_number = invoice_number.group().replace(" ", "")
	except AttributeError:
		invoice_processor_logger.error("Script did not manage to read invoice number")
		invoice_number = ""

	try:
		invoice_date = process_date(invoice_date.group())
	except AttributeError:
		invoice_processor_logger.error("Script did not manage to read invoice date")
		invoice_date = ""

	try:
		invoice_total_amount = invoice_total_amount.group().split("$")[-1].replace(",", "")
	except AttributeError:
		invoice_processor_logger.error("Script did not manage to read total amount")
		invoice_total_amount = ""
	
	return {
		"invoice_number" : invoice_number,
		"invoice_date" : invoice_date,
		"invoice_total_amount" : invoice_total_amount 
	}

# Converts date abbreviation to mm format
def process_date(date: str) -> str:
	[month, day, year] = date.split(" ")
	month_names = {
		"Jan" : "01",
		"Feb" : "02",
		"Mar" : "03",
		"Apr" : "04",
		"May" : "05",
		"Jun" : "06",
		"Jul" : "07",
		"Aug" : "08",
		"Sep" : "09",
		"Oct" : "10",
		"Nov" : "11",
		"Dec" : "12",
	}
	return f"{day}.{month_names[month]}.{year}"

# Creates csv entry containing invoice number, date and total amount billed
def generate_invoice_summary(invoice_data: dict) -> str:
	return f"{invoice_data['invoice_number']},{invoice_data['invoice_date']},{invoice_data['invoice_total_amount']}"

# Creates summary file, then fills it with entries for each one 
def create_invoices_repport():
	with open("output.csv", "w") as invoice_summary_file:
		invoice_summary_file.write("invoice number, invoice data, invoice total amount\n")
		for invoice_file in os.listdir("./invoices"):
			invoice_text = read_document_to_pdf(f"./invoices/{invoice_file}")
			invoice_data = split_data(invoice_text)
			invoice_summary_file.write(f"{generate_invoice_summary(invoice_data)}\n")


def main():
	global invoice_processor_logger
	invoice_processor_logger = start_logging()
	create_invoices_repport()


if __name__ == '__main__':
	main()
