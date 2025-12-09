# Data Analysis
# Author: Carl Dicioco
# 24 November
# Analyse the NYC Central Park weather data from 1869–2022


def main():
    filename = "data/nyccentralpark.csv"

    num_data_points = 0
    total_rainfall = 0.0
    total_tmin = 0.0

    june_tmax_total = 0.0
    june_count = 0

    with open(filename, "r") as file:
        next(file)

        for line in file:
            parts = line.strip().split(",")

            date_str = parts[0]
            prcp_str = parts[1]
            tmin_str = parts[4]
            tmax_str = parts[5]

            num_data_points += 1

            if prcp_str == "":
                rainfall = 0.0
            else:
                rainfall = float(prcp_str)
            total_rainfall += rainfall

            if tmin_str != "":
                tmin_f = float(tmin_str)
                total_tmin += tmin_f

            # June TMAX
            # date format is YYYY-MM-DD -> month is at positions [5:7]
            month = date_str[5:7]
            if month == "06" and tmax_str != "":
                june_tmax_total += float(tmax_str)
                june_count += 1

    average_rainfall = total_rainfall / num_data_points

    avg_tmin_fahr = total_tmin / num_data_points
    avg_tmin_cels = (avg_tmin_fahr - 32) * 5 / 9

    if june_count > 0:
        avg_june_tmax = june_tmax_total / june_count
    else:
        avg_june_tmax = 0.0

    print(f"Number of data points: {num_data_points}")
    print(f"average rainfall (inches): {average_rainfall:.2f}")
    print(f"average minimum temperature (F): {avg_tmin_fahr:.2f}")
    print(f"average minimum temperature (C): {avg_tmin_cels:.2f}")
    print(f"average June maximum temperature (F): {avg_june_tmax:.2f}")


if __name__ == "__main__":
    main()
