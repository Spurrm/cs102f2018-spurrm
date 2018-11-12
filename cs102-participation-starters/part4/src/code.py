import statistics
from collections import Counter

def calculate_mean(numbers_list):
    print(" Values", numbers_list)
    s_int = sum(numbers_list)
    N_int = len(numbers_list)
    # Calculate the mean
    mean_flt = s_int/N_int
    return mean_flt
#end of calculate_mean()

def calculate_median(numbers_list):
    #
    print(" calculate_mean()")
    N = len(numbers_list)
    numbers_list.sort()
    # Find the median
    if N % 2 == 0:
        # if N is even
        m1 = N/2
        m2 = (N/2) + 1
        # Convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median_int = (numbers_list[m1] + numbers_list[m2])/2
    else:
        m = (N+1)/2
        # Convert to integer, match position
        m = int(m) - 1
        median_int = numbers_list[m]
    return median_int
# end of median

def calculate_mode(numbers_list):
    print(" Values: ",numbers_list)
    c = Counter(numbers_list)
    mode_int = c.most_common(1) #print first most common
    return mode_int[0][0]
#end of calculate_mode()

def find_range(numbers_list):
    print(" Values: ",numbers_list)
    lowest_int = min(numbers_list)
    highest_int = max(numbers_list)
    # Find the range
    r_int = highest_int - lowest_int # find distance
    return lowest_int, highest_int, r_int
#end of find_range()

if __name__ == '__main__':
    # printing mean
    donations_list = [100, 60, 70, 900, 100,
    200, 500, 500, 503, 600, 1000, 1200]
    mean_flt = calculate_mean(donations_list)
    N_int = len(donations_list)
    print(' The mean of the {0} values is {1}'.format(N_int, mean_flt))
    # printing median
    print(" Data:",donations_list)
    median_int = calculate_median(donations_list)
    N = len(donations_list)
    print(' Median donation over the last {0} days is {1}'.format(len(donations_list), median_int))
    scores_list = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    print(" Set: ",scores_list)
    mode_int = calculate_mode(scores_list)
    print(" Mode: ",mode_int)
    lowest, highest, r = find_range(donations_list)
    print(' Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, r))
