[![Build Status](https://travis-ci.org/rrsw/46-simple-python-exercises.svg?branch=master)](https://travis-ci.org/rrsw/46-simple-python-exercises)

# 46-simple-python-exercises

Torbjörn Lager's 46 Simple Python Exercises

>This is version 0.45 of a collection of simple Python exercises constructed (but in many cases only found and collected) by Torbjörn Lager (torbjorn.lager@ling.gu.se). Most of them involve characters, words and phrases, rather than numbers, and are therefore suitable for students interested in language rather than math.

Description found [here](http://easyprog99.blogspot.com/2017/02/46-simple-python-exercises.html).

Goal is to complete at least 4 exercises a week in order to continue practicing Python programming and to continue improving.

## Table of Contents

- [Exercise list](#exercise-list)
- [Prerequisites](#prerequisites)
- [Test](#test)
- [Acknowledgements](#acknowledgements)
- [Contributing](#contributing)

## Exercise list

|ex. 01-10|ex. 11-20|ex. 21-30|ex. 31-40|ex. 41-46|
|:---|:---|:---|:---|:---|
|[01 max](srcs/ex01.py)|[11 generate_n_chars](srcs/ex11.py)|[21 char_freq](srcs/ex21.py)|  |  |
|[02 max_of_three](srcs/ex02.py)|[12 histogram](ex12.py)|[22 caesar_cipher](srcs/ex22.py)|  |  |
|[03 len](srcs/ex03.py)|[13 max_in_list](srcs/ex13.py)|[23 correct](srcs/ex23.py)|  |  |
|[04 vowel](srcs/ex04.py)|[14 words_to_len](srcs/ex14.py)|[24 3sg_form](srcs/ex24.py)|  |  |
|[05 translate](srcs/ex05.py)|[15 longest_word](srcs/ex15.py)|[25 ing_form](srcs/ex25.py)|  |  |
|[06 sum+multiply](srcs/ex06.py)|[16 filter_long_words](srcs/ex16.py)|  |  |  |
|[07 reverse](srcs/ex07.py)|[17 phrase_palindrome](srcs/ex17.py)|  |  |  |
|[08 palindrome](srcs/ex08.py)|[18 pangram](srcs/ex18.py)|  |  |  |
|[09 member](srcs/ex09.py) |[19 beer](srcs/ex19.py)|  |  |  |
|[10 overlapping](srcs/ex10.py)|[20 translate](srcs/ex20.py)|  |  |  |


### Prerequisites

* Python (Python 3.3 or greater, or Python 2.7)
* I also test my code in [IPython](https://ipython.org/install.html) during writing process.

### Test

I wrote some automated tests for each exercise. My tests are quite simple for the moment. Don't hesitate to use them. You may need to modifiy the python test files if your layout, your function names and your source file names are different than mine.

Below is my project layout:

```
├── __init__.py
├── .travis.yml			# travis config
├── srcs			# directory to group all the source files
│   ├── __init__.py
│   ├── ex01.py			# one file per exercise
│   ├── ex02.py
│   ├── ex03.py
│   └── ...
└── tests			# directory to group all the test files
    ├── __init__.py
    ├── test_01.py		# one test file per exercise file
    ├── test_02.py
    ├── test_03.py
    └── ...
```

## Acknowledgements

The original collection was constructed, but also found and collected by [Torbjörn Lager](https://www.gu.se/english/about_the_university/staff/?languageId=100001&userId=xlagto).

## Contributing

I may not find the best solutions. Feel free to submit a pull request, issue or suggestion.
