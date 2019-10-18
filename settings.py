def init(): #!do not forget to call in main !
    global COLUMNS
    global ROWS
    global BOXSIDE
    COLUMNS = int(input("How many columns (Default: 30) ? ") or "30")
    ROWS = int(input("How many rows (Default : 30) ? ") or "30")
    BOXSIDE = 20