import os, sys
import win32print


printer_name = win32print.GetDefaultPrinter()
"""
printer_name = win32print.GetPrinterDriverDirectory()
print(type(printer_name))
print(printer_name)"""
#
# raw_data could equally be raw PCL/PS read from
#  some print-to-file operation
#
"""
if sys.version_info >= (3,):
  raw_data = bytes ("This is a test", "utf-8")
else:
  raw_data = "This is a test"

raw_data = bytes ("This is a test", "utf-8")
hPrinter = win32print.OpenPrinter (printer_name)
print("prenter connection openned")
try:
  hJob = win32print.StartDocPrinter (hPrinter, 1, ("test of raw data", None, "RAW"))
  try:
    print("document printer started")
    win32print.StartPagePrinter (hPrinter)
    print("page printer started")
    win32print.WritePrinter (hPrinter, raw_data)
    print("writing to printer")
    win32print.EndPagePrinter (hPrinter)
    print("page printer ended")
  finally:
    print("document printer ended")
    win32print.EndDocPrinter (hPrinter)
finally:
  print("prenter connection closed")
  win32print.ClosePrinter (hPrinter)
"""
