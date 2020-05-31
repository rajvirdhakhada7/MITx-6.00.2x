from ps1_partition import get_partitions

limit = 15
cows = {'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3, 'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}

if sum(w > limit for w in cows.values()) != 0:
    print("Solution Doesn't exists")
    #return [[]]


rej_trip = []
#final_lst = []
no_of_trip = len(cows) + 1
for partition in get_partitions(cows):
    print('partition : ', partition)
    print('parti len : ', len(partition))
    if len(partition) < no_of_trip:
        for trip in partition:
            #print(trip)
            if trip in rej_trip:
                print(f"{trip} is in rejection list")
                break
            trip_w = sum(cows[cow] for cow in trip)
            print(trip_w)
            if trip_w > limit:
                print(f"{trip} exeed weight limit, adding it in rejection list")
                rej_trip.append(trip)
                break
        no_of_trip = len(partition)
        final_lst = partition
print(final_lst)