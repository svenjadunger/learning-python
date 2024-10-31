fellowship = ['gandalf', 'aragorn', 'frodo', 'sam', 'merry', 'pippin', 'gimli', 'legolas', 'boromir']
hobbits = ['frodo', 'sam', 'pippin', 'merry']

print('saruman' in fellowship)
print(fellowship[0] == 'gandalf')
print(fellowship[2:7] == hobbits)
print('sam' in fellowship and 'sam' in hobbits)
print(fellowship[-3] == 'sam' or hobbits[-3] == 'sam')