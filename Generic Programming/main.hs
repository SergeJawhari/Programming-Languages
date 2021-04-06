import Data.Function (on)
import Data.List (sortBy)
import Data.List (sort)
import Data.Monoid
import Data.List
import Data.Ord

-- This class will take advantage of the Ord library, specifically the 'comparing' method to selectively decide which element in a list of tuples to compare and sort by.

-- List of numbers that are to be sorted.
numbersList = [645.41, 37.59, 76.41, 5.31, -34.23, 1.11, 1.10, 23.46, 635.47, -876.32, 467.83, 62.25]

-- List of people and their respective ages to be sorted in two different ways.
peopleList = [("Hal", 20), ("Susann", 31), ("Dwight", 19),("Kassandra", 21), ("Lawrence", 25),("Cindy", 22), ("Cory", 27), ("Mac", 19), ("Romana", 27), ("Doretha",32),("Danna", 20), ("Zara", 23), ("Rosalyn", 26), ("Risa", 24), ("Benny", 28),("Juan", 33), ("Natalie", 25)]

-- This is the method that the sortBy function will follow. This is from the Ord library and simply states that the first element in every tuple will be used for comparison, and sorted based on that element.
orderOfNames = comparing fst

-- This is the method that the sortBy function will follow. This is from the Ord library and simply states that the second element in every tuple will be used for comparison, and sorted based on that element, then the <> operator will 'append' that sort to another sort comparison, which means that after comparing the second element (snd), it will then compare all of the first elements in the tuple (fst).
orderOfAgesThenNames = flip (comparing snd) <> comparing fst

-- This is the notation for calling a main function.
main :: IO ()
main = do
  -- These two lines will print the list of numbers in sorted order.
  print "============= Numbers Sorted ============="
  print (showList (sort numbersList) "")

  print $ ' '

  -- These two lines will print the list of people in order of name.
  print "============= Names Sorted ============="
  print (showList (sortBy orderOfNames peopleList) "")

  print $ ' '

  -- These two lines will print the list of people in priority order of Age and then by Name, respectively.
  print "============= Sorted by priority of Age>Name ============="
  print (showList (sortBy orderOfAgesThenNames peopleList) "")