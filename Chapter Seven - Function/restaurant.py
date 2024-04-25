greeting =" Hello wecome to this restaurant"
guests= greeting + "\nhow many people are in your dinner group?"
welcome=int(input(guests))
if welcome >= 8:
    print("you’ll have to wait for a table.")
else:
    print("report that their table is ready")