# What is 7 to the power of 4?

print(7 ** 4)

# Split this string:
# s = “Hi there Sam!”
# into a list and replace Sam with dad.
s = 'Hi there Sam!'
s2 = 'Hello there! How are you Sam?'
print(s2.replace('Sam', 'dad'))
print(s.replace('Sam', 'dad'))

# Given the variables:
# planet = “Earth”
# diameter = 12742
# Use .format() to print the following string:
# The diameter of Earth is 12742 kilometers.

planet = 'Earth'
diameter = 12742
print('The diameter of {} is {} kilometers.'.format(planet, diameter))
print(f'The diameter of {planet} is {diameter} kilometers.')

# Given this nested list, use indexing to grab the word “hello”
# lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(lst[3][1][2][0])

# Given this nested dictionary grab the word “hello”. Be prepared, this will be annoying/tricky
# d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d = {
    'k1': [
        1, 2, 3, {
            'tricky': [
                'oh', 'man', 'inception', {
                    'target': [
                        1, 2, 3, 'hello'
                    ]
                }
            ]
        }
    ]
}
print(d['k1'][3]['tricky'][3]['target'][3])

# What is the main difference between a tuple and a list? Intentionally generate an error by changing a tuple value.
lst = [1, 2, 3]
lst[0] = 1

tpl = (1, 2, 3)
# tpl[0] = 1  # Throws error

# Create a function that grabs the email website domain from a string in the form:
# super_user@gmail.com
# So for example, passing “super_user@gmail.com” would return: gmail.com

s = 'super_user@gmail.com'
print(s.split('@')[1])

# Create a basic function that returns True if the word 'car' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word car, but do account for capitalization.
# Create a function that counts the number of times the word “car” occurs in a string. Again ignore edge cases.
# Example:
# countCar('This car runs faster than the other car dude!')
# 2

s = 'This car runs faster than the other car dude!'
print(s.count('car'))

# Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:
# seq = ['soup','dog','salad','cat','great']
# should be filtered down to:
# ['soup','salad']

seq = ['soup', 'dog', 'salad', 'cat', 'great']
filter_seq = filter(lambda x: x.startswith('s'), seq)
new_seq = []
for word in filter_seq:
    new_seq.append(word)

print(new_seq)

# list comprehension
new_seq = [x for x in filter(lambda x: x.startswith('s'), seq)]
print(new_seq)

print(max([1, 2, 3]))


# lambda x: x.startswith('s')  # the same as filter_function
def filter_function(x):
    return x.startswith('s')


new_seq = [x for x in filter(filter_function, seq)]
print(f'Filter list with function: {new_seq}')


def fnc():
    print('Hi!')


fnc()
fnc()

print(filter_function('sandra'))
print(filter_function('salamandra'))
print(filter_function('kot'))


from lesson_4 import count_animals
print(count_animals('pies, kot, lew'))
