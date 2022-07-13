""""
Hasana Parker
CS51a: Assignment 6
February 28th, 2022

For extra credit I made a recursive triangle made out of triangles.
"""

# ___________________________________
# Warming up: list

from turtle import *


def concat_strings(list_of_strings):
    """
    This function takes a list of strings as a parameter and uses recursion to add all items of the list to a single
    string.
    :param list_of_strings: (list) Takes any list of strings
    :return: Returns a string with all items of the list
    """
    if list_of_strings == []:
        return ""

    else:
        return list_of_strings[0] + " " + concat_strings(list_of_strings[1:])  # adds the zeroth index and then
        # concatenates it with a space and the remainder of the list.


def length(some_list):
    """
    This function calculates the length of a list using recursion.
    :param some_list: (list) Any list
    :return: the length of the list
    """

    if some_list == []:
        return 0
    else:
        return 1 + length(some_list[1:])  # by setting it at 1, the value of the index isn't stored but only counted


def rec_count(list, value):
    """
    This function takes a list and a value as parameters and counts how many times the value occurs in the list.
    :param list: (list) takes any list of integers
    :param value: (int) any integer
    :return: returns the amount of times the value occurs in the list.
    """
    if list == []:
        return 0
    else:
        count = rec_count(list[1:], value)  # setting count as a value, that checks the entire list to see if the value
        # is present within
        if list[0] == value:  # if the value is in the list
            return count + 1  # add to the count each time the value is in the list
        else:
            return count + 0  # don't count if value not in list


def remove_spaces(string):
    """
    This function takes a string as an input and removes all the spaces from the sting.
    :param string: (str) any string
    :return: returns a string with no white spaces in between words
    """
    if string == "":
        return ""

    else:
        if string[0] == " ":  # checks the first index because each time the recursive function runs a new value will be
            # index 0
            return remove_spaces(string[1:])  # brings the next value without keeping the one that was just evaluated

        else:
            return string[0] + remove_spaces(string[1:])  # if there isn't a space add it to the string.


# ___________________________________
# Recursive Turtle


def draw_h(x, y, length):
    """
    This function helps to draw H's.
    :param x: (int) X coordinate of H
    :param y: (int) y coordinate of H
    :param length: (int) the length of the H

    """
    setheading(0)
    forward(length)
    right(90)
    forward((length/2))
    backward(length)
    pu()
    goto(x, y)
    pd()
    left(90)
    setheading(180)
    forward(length)
    right(90)
    forward((length / 2))
    backward(length)

# draw_H(0, 0, 50)


def recursive_H(x, y, l, levels):
    """
    This function draws H's recursively.
    :param x: (int) x-coordinate of H
    :param y: (int) y- coordinate of H
    :param l: (int) Length of the H
    :param levels: (int) the number of times the function runs recursively
    :return: none
    """
    pu()
    goto(x, y)
    pd()
    speed(0)

    if levels == 0:
        dot()  # makes the dots at the end of drawing the H.

    else:
        draw_h(x, y, l) # calling the draw h function to help with the recursion
        recursive_H(x - l, y + l/2, l/2, levels - 1)  # subtract a level each time so that the function knows when
        # to stop
        recursive_H(x - l, y - l/2, l/2, levels - 1)
        recursive_H(x + l, y + l/2, l/2, levels - 1)
        recursive_H(x + l, y - l/2, l/2, levels - 1)


# recursive_H(0, 0, 100, 3)


def draw_sq(x, y, side_length, color):
    """
    This function draws squares.
    :param x: (int) x-coordinate of square
    :param y: (int) y-coordinate of square
    :param side_length: (int) side length of the square
    :param color: (float) effects the hues of the blues
    :return: none
    """
    pu()
    goto(x, y)
    pd()
    setheading(0)  # setting the direction of the turtle
    fillcolor(color)
    begin_fill()

    for i in range(4):
        forward(side_length)
        left(360 / 4)

    end_fill()


# draw_sq(0, 0, 100, "blue")


def stairs(x, y, side_length, blueness):
    """
    This function draws stairs out of squares.
    :param x: (int) x-coordinate of square
    :param y:(int) y-coordinate of a square
    :param side_length: (int) length of the side of the square
    :param blueness: (float) affects the shades of green and red
    :return: none
    """
    speed(0)

    if side_length > 3:
        color = (blueness, blueness, 1)  # makes it so the color changes each time around
        draw_sq(x, y, side_length, color)
        stairs(x, y + side_length, side_length/2, blueness * .6)  # blueness * .6  decreasing the shade of green and red
        stairs(x + side_length, y, side_length / 2, blueness * .6)


# stairs(0, 0, 100, 0.8)


def draw_triangle(x, y, side_length, color):
    """
    The function makes triangles.
    :param x: (int) x coordinate of triangle
    :param y: (int) y coordinate of triangle
    :param color: (string) sets the fillcolor of the triangle
    :param side_length: (int) side length of equilateral triangle
    """
    penup()
    goto((x, y))
    setheading(180)
    pendown()

    fillcolor(color)
    begin_fill()
    for i in range(3):     # range is 3 to make the code run 3 times, and draw all sides of the triangle.
        forward(side_length)
        right(120)
    end_fill()


def triangle_recursion(x, y, side_length, redness):
    """
    This functions draws a triangle out of triangles recursively
    :param x: (int) x-coordinate of the triangle
    :param y: (int) y-coordinate of triangle
    :param side_length: (int) side length of the triangle
    :param redness: (float) affects the hues of green and blue
    :return: none
    """

    if side_length > 3:
        color = (1, redness, redness)
        draw_triangle(x, y, side_length, color) # calling on the color variable, which decrease by .6 each time
        # through the recursive function
        triangle_recursion(x, y + side_length, side_length / 2, redness * .6)  # divide side length by two to make each
        # triangle smaller through the recursive function
        triangle_recursion(x + side_length, y, side_length / 2, redness * .6)


# triangle_recursion(0, 0, 50, 0.8)

# exitonclick()


