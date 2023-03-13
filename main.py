import pack

date = pack.Date1(-1, 3, 12) # error case for year
date.display_date()

date_hours = pack.DateTime1(2023, 12, 12, 23, 33, 120) # error case for seconds
date_hours.display_date()

date_hours = pack.DateTime1(2023, 12, 12, 50, 33, 120) # error case for hours
date_hours.display_date()











