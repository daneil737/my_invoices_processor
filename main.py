#!/usr/bin/python3

import os
import re
import pdftotext


def read_document_to_pdf(filename: str) -> str:
	with open(filename, "rb") as invoice_file:
		invoice_text = pdftotext.PDF(invoice_file)

	return invoice_text

def split_data(invoice_text: str) -> dict:
	invoice_number = re.search("[#]\\s\\d{4,5}", invoice_text[0])
	invoice_date = re.search("\\D{3}\\s\\d{2}\\s\\d{4}", invoice_text[0])
	invoice_total_amount = re.search("Total:\\s+\\$([\\d]*,?[\\d]+\\.\\d{2})", invoice_text[0])
	try:
		invoice_number = invoice_number.group().replace(" ", "")
	except AttributeError:
		invoice_number = ""

	try:
		invoice_date = process_date(invoice_date.group())
	except AttributeError:
		invoice_date = ""

	try:
		invoice_total_amount = invoice_total_amount.group().split("$")[-1].replace(",", "")
	except AttributeError:
		invoice_total_amount = ""
	
	return {
		"invoice_number" : invoice_number,
		"invoice_date" : invoice_date,
		"invoice_total_amount" : invoice_total_amount 
	}


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


def generate_invoice_summary(invoice_data: dict) -> str:
	return f"{invoice_data['invoice_number']},{invoice_data['invoice_date']},{invoice_data['invoice_total_amount']}"


def generate_csv_summary():
	with open("output.csv", "w") as invoice_summary_file:
		invoice_summary_file.write("invoice number, invoice data, invoice total amount\n")
		for invoice_file in os.listdir("./invoices"):
			invoice_text = read_document_to_pdf(f"./invoices/{invoice_file}")
			invoice_data = split_data(invoice_text)
			invoice_summary_file.write(f"{generate_invoice_summary(invoice_data)}\n")


def main():
	# invoice_text = read_document_to_pdf("invoices/invoice_Frank Carlisle_49474.pdf")
	generate_csv_summary()


if __name__ == '__main__':
	main()