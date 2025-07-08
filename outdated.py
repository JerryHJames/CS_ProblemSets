def main():
    # List of month names for conversion
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    # Keep asking until we get a valid date
    while True:
        try:
            # Get date input from user
            date_input = input("Date: ").strip()

            # Check if it's in MM/DD/YYYY format (contains slashes)
            if "/" in date_input:
                # Split by slash and try to parse
                parts = date_input.split("/")
                if len(parts) != 3:
                    continue  # Not exactly 3 parts, invalid

                month, day, year = parts

                # Convert to integers and validate
                month = int(month)
                day = int(day)
                year = int(year)

                # Validate ranges
                if month < 1 or month > 12:
                    continue  # Invalid month
                if day < 1 or day > 31:
                    continue  # Invalid day

            # Check if it's in "Month DD, YYYY" format (contains comma)
            elif "," in date_input:
                # Split by comma first to separate year
                parts = date_input.split(",")
                if len(parts) != 2:
                    continue  # Should be exactly 2 parts when split by comma

                # Get the year part and clean it up
                year = int(parts[1].strip())

                # Split the first part by space to get month and day
                month_day_part = parts[0].strip().split()
                if len(month_day_part) != 2:
                    continue  # Should be exactly month and day

                month_name, day = month_day_part

                # Convert month name to number using index + 1
                if month_name not in months:
                    continue  # Invalid month name
                month = months.index(month_name) + 1

                # Convert day to integer and validate
                day = int(day)
                if day < 1 or day > 31:
                    continue  # Invalid day

            else:
                # Doesn't match either format
                continue

            # If we got here, we have valid month, day, year
            # Format and output in ISO 8601 format (YYYY-MM-DD)
            print(f"{year}-{month:02d}-{day:02d}")
            break

        except ValueError:
            # Conversion to int failed or other parsing error
            # Just continue to prompt again
            continue

main()
