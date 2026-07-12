#!/usr/bin/python3

import invoice2data


def read_document(filename: str) -> list[str]:
	pass


def split_data(data_array: list[str]) -> dict:
	pass


def process_date(date: str):
	pass


def generate_summary():
	pass


def main():
	data = invoice2data.extract_data("invoices/invoice_Frank Carlisle_49474.pdf")
	print(data)




if __name__ == '__main__':
	main()