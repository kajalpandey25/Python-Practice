Python Lists =>
. Lists are ordered collection of data items.
. They store multiple items in a single variable.
. List items are separated by commas and enclosed within square brackets [].
. Lists are changeable meaning we can alter them after creation.

Example 1:
lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

o/p:
[1, 2, 2, 3, 5, 4, 6]
['Red', 'Green', 'Blue']

Example 2:
details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)

o/p:
['Abhijeet', 18, 'FYBScIT', 9.8]
As we can see, a single list can contain items of different data types.



-------------------------------------------------------

List Index =>
Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.

Example:
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]


Accessing list items =>
We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give "Green" and so on...

Positive Indexing:
As we have seen that list items have index, as such we can access items using these indexes.

Example: