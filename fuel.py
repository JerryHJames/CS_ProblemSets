            # Check the fraction to be sure it makes sense
            if numerator < 0 or denominator <= 0 or numerator > denominator:
                continue

            # Calculate the percentage
            percentage = round((numerator / denominator) * 100)

            # Handle special cases
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            # If it works, break out of the loop
            break

        # Either the split didn't work, int failed, or division by zero. Keep looping
        except (ValueError, ZeroDivisionError):
            pass
main()
