#!/usr/bin/python3

import os
import re
import pdftotext


def read_document(filename: str) -> list[str]:
	pass


def split_data(data_array: list[str]) -> dict:
	pass


def process_date(date: str):
	pass


def generate_summary():
	pass


def main():

	with open("invoices/invoice_Frank Carlisle_49474.pdf", "rb") as invoice_file:
		invoice_text = pdftotext.PDF(invoice_file)
	invoice_number = re.search("[#]\\s\\d{5}", invoice_text[0])
	invoice_date = re.search("\\D{3}\\s\\d{2}\\s\\d{4}", invoice_text[0])
	invoice_total_amount = re.search("Total:\\s+\\$([\\d]+,[\\d]+\\.\\d{2})", invoice_text[0])

	print(invoice_number.group())
	print(invoice_date.group())
	print(invoice_total_amount.group())


if __name__ == '__main__':
	main()