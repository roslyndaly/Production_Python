# Logging Exercise

Within this folder, there is a Python file `inventory_management.py` which is a simple inventory management system. This script handles basic actions like adding products, removing products, and checking inventory. There's no logging initially. Your task is to add appropriate logging to this script, with the following requirements:

- There is logging to a file and the console.
- The console logs every message, the file logs all messages apart from `DEBUG` messages.
- The format for all logs follows the following examples:

``` text
2024-12-09 15:32:40,907 - INFO - Inventory initialized.
2024-12-09 15:32:40,907 - INFO - Adding 10 of Laptop.
2024-12-09 15:32:40,907 - INFO - Added new item Laptop with quantity 10.
2024-12-09 15:32:40,908 - INFO - Adding 25 of Mouse.
2024-12-09 15:32:40,908 - INFO - Added new item Mouse with quantity 25.
2024-12-09 15:32:40,909 - INFO - Adding 15 of Keyboard.
2024-12-09 15:32:40,909 - INFO - Added new item Keyboard with quantity 15.
2024-12-09 15:32:40,909 - INFO - Removing 5 of Mouse.
2024-12-09 15:32:40,909 - DEBUG - Removed 5 of Mouse. New quantity: 20
2024-12-09 15:32:40,909 - INFO - Removing 10 of Keyboard.
2024-12-09 15:32:40,909 - DEBUG - Removed 10 of Keyboard. New quantity: 5
2024-12-09 15:32:40,911 - INFO - Removing 5 of Laptop.
2024-12-09 15:32:40,911 - DEBUG - Removed 5 of Laptop. New quantity: 5
```
