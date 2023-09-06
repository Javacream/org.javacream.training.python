def count_all_words(text):
    return len(text.split(" "))

def count_all_unique_words(text):
    all_words = text.split(" ")
    unique_words = set()
    for word in all_words:
        unique_words.add(word)
    return len(unique_words)

def count_all_unique_words_ignore_case(text):
    all_words = text.split(" ")
    unique_words = set()
    for word in all_words:
        unique_words.add(word.lower())
    return len(unique_words)

def main():
    text = """
    python PYTHON PYThon Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[34]

    Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[35][36]

    Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[37] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[38]

    Python consistently ranks as one of the most popular programming languages.[39][40][41][42]

    History

    The designer of Python, Guido van Rossum, at OSCON 2006
    Main article: History of Python
    Python was conceived in the late 1980s[43] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[44] capable of exception handling and interfacing with the Amoeba operating system.[13] Its implementation began in December 1989.[45] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's "benevolent dictator for life", a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker.[46] In January 2019, active Python core developers elected a five-member Steering Council to lead the project.[47][48]

    Python 2.0 was released on 16 October 2000, with many major new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support.[49] Python 3.0, released on 3 December 2008, with many of its major features backported to Python 2.6.x[50] and 2.7.x. Releases of Python 3 include the 2to3 utility, which automates the translation of Python 2 code to Python 3.[51]

    Python 2.7's end-of-life was initially set for 2015, then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.[52][53] No further security patches or other improvements will be released for it.[54][55] Currently only 3.8 and later are supported (2023 security issues were fixed in e.g. 3.7.17, the final 3.7.x release[56]). In 2021, Python 3.9.2 and 3.8.8 were expedited[57] as all versions of Python (including 2.7[58]) had security issues leading to possible remote code execution[59] and web cache poisoning.[60]

    In 2022, Python 3.10.4 and 3.9.12 were expedited[61] and 3.8.13, because of many security issues.[62] When Python 3.9.13 was released in May 2022, it was announced that the 3.9 series (joining the older series 3.8 and 3.7) would only receive security fixes in the future.[63] On September 7, 2022, four new releases were made due to a potential denial-of-service attack: 3.10.7, 3.9.14, 3.8.14, and 3.7.14.[64][65]

    As of November 2022, Python 3.11 is the stable release. Notable changes from 3.10 include increased program execution speed and improved error reporting.[66]

    Since 27 June 2023, Python 3.8 is the oldest supported version of Python (albeit in the 'security support' phase), due to Python 3.7 reaching end-of-life.[67]

    The first release candidate of Python 3.12 was offered on 6 August 2023.


    """

    print(count_all_words(text))
    print(count_all_unique_words(text))
    print(count_all_unique_words_ignore_case(text))    

main()