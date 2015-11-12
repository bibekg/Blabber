#!/usr/bin/python
import sentence_generator

def main(): 
    test = sentence_generator.sentence_generator("txt/harrypotter.txt", 3)
    print(test.generate_sentence(40))

if __name__ == "__main__":
    main()