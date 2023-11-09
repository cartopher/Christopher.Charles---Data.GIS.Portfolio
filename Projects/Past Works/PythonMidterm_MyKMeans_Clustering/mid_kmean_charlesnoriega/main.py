import os
import libs

directoryPath = 'C:/Users/cchar/PycharmProjects/pythonProject/pythonProject/mid_kmean_charlesnoriega/output/'

inputPath = 'C:/Users/cchar/PycharmProjects/pythonProject/pythonProject/mid_kmean_charlesnoriega/data/'
# dataFile = 'aggregation.csv'
dataFile = 's1.txt'
# separator = ','
separator = '\t'

if os.path.isdir(directoryPath):
    print("Directory already exists")
else:
    print("Creating directory for you")
    os.mkdir(directoryPath)


def main():
    print("python main function")

    # for k in range(5, 11, 2):  # aggregation.csv 5, 7, 9
    for k in range(10, 25, 5):   # s1.txt 10, 15, 20
        myTestMeans = libs.MyKmeans(k)
        myTestMeans.read_xy_from_file(inputPath + dataFile, separator)
        myTestMeans.initialize_centroid()

        flag_terminate = False
        count = 0
        while flag_terminate == False:
            count += 1
            myTestMeans.assign_clust_number()
            flag_terminate = myTestMeans.update_centroid()
            if flag_terminate == True:
                print("Stable centroids achieved after " + str(count) + " iterations")

            # plot_clust_points(myTestMeans,pt_size=10,centroid_size=100)
            myTestMeans.save_clust_points_csv(directoryPath)
            libs.save_clust_points_img(myTestMeans, directoryPath, pt_size=30)


if __name__ == '__main__':
    main()
'''''
# g
Pros:
The algorithm is adaptable, simple to implement and modify, and scales to large data sets (s1.txt)
Cons: From what I can tell from the KMeans 20 OutImage, groups appear to have varying densities; 
adding more groups would make it more difficult for the algorithm to perform better, 
which is a significant disadvantage. Additionally, centroids are difficult to distinguish within groups, 
and does not seem effective in pinpoint outliers.
'''''
