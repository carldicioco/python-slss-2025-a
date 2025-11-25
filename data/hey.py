# Data Analysis
# Author: Carl Dicioco
#
# Analyse the NYC Central Park weather data from 1869-2022
def main():
    filename = "data/nyccentralpark.csv"
    num_data_points = 0
    total_rainfall = 0
    with open(filename, "r") as file:
        next(file)
        for line in file:
            parts = line.strip().split(",")
            prcp_str = parts[1]
            if prcp_str == "":
                rainfall = 0.0
            else:
                rainfall = float(prcp_str)
            total_rainfall += rainfall
            num_data_points += 1
    average_rainfall = total_rainfall / num_data_points
    print(f"number of data points: {num_data_points}")
    print(f"average rainfall (inches): {average_rainfall:.2f}")


if __name__ == "__main__":
    main()
