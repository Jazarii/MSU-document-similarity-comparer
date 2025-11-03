'''
 # Will break long strings into units of three(MMXXV)
'''


'''
A function which will read in the transcript from a file.
'''
def transcript_reader (filename, transcript_or_notes):
    main_txt_file_name_here = ""
    transcript = ""
    main_txt_file_name_here = filename
    'dont forget to add the file extension'
    try:
        with open(main_txt_file_name_here):
            print("\n")
    except FileNotFoundError:
        print("\n\nThe file name is wrong or it's not in the same folder as this program. Restart the program and try again.")
    if (transcript_or_notes == 1):
        with open(main_txt_file_name_here, encoding = "utf-8") as unread_txt:
            '''
            if your file is in a different encoding language (has curly quotes or
            something) then change the encoding
            '''
            transcript = unread_txt.read()
            print("ORIGINAL TRANSCRIPT")
    else:
        with open(main_txt_file_name_here, encoding = "utf-8") as unread_txt:
            '''
            if your file is in a different encoding language (has curly quotes or
            something) then change the encoding
            '''
            transcript = unread_txt.read()
            print("ORIGINAL NOTES")
    print(transcript)
        
    return transcript


'''
A function which will take the transcript and scrub it of all non-letter
characters. It also decapitalizes all capital letters.
'''
def transcript_scrubber (dirty_transcript, transcript_length):
    scrubbed_transcript = ""
    letter_made_lowercase = 'A'
    word_counter = 0
    new_length = 0
    'a counter for moving through the transcript letter by letter'
    while word_counter < transcript_length:
        if (dirty_transcript[word_counter] >= 'a' and dirty_transcript[word_counter] <= 'z'):
            scrubbed_transcript += dirty_transcript[word_counter]
        elif (dirty_transcript[word_counter] >= 'A' and dirty_transcript[word_counter] <= 'Z'):
            letter_made_lowercase = dirty_transcript[word_counter].lower()
            scrubbed_transcript += letter_made_lowercase
        elif (dirty_transcript[word_counter] >= '0' and dirty_transcript[word_counter] <= '9'):
            scrubbed_transcript += dirty_transcript[word_counter]
        elif (dirty_transcript[word_counter] == ' ' and dirty_transcript[word_counter - 1] != ' '):
            scrubbed_transcript += ' '
        elif (dirty_transcript[word_counter] == '\n'):
            scrubbed_transcript += ' '
        word_counter += 1

    new_length = len(scrubbed_transcript)
    if (scrubbed_transcript[new_length - 1] == ' '):
        print(scrubbed_transcript[new_length - 1])
        scrubbed_transcript = scrubbed_transcript[:-1]
    '''
    to prevent extra spaces from getting in if the document ends with a weird
    character
    '''
        
    return scrubbed_transcript


'''
A function which will take the transcript and turn it into a list of all
three-word pairs. Each entry in the list is a list itself with three entries,
one for each word in the three-word pair.
'''
def transcript_concatenater (unconcatenated_transcript, transcript_length):
    word_trio = []
    'a group of three words to be added to the concatenated_transcript'
    number_of_words_in_the_trio = 0
    'how many words the word trio has currently'
    concatenated_transcript = []
    assembled_word = ""
    '''
    the word that the function is currently forming by reading characters
    in from the transcript
    '''
    word_counter = 0
    'a counter for moving through the transcript letter by letter'
    while word_counter < transcript_length:
        if (number_of_words_in_the_trio == 3):
            concatenated_transcript.append(word_trio)
            word_trio = [word_trio[1], word_trio[2]]
            number_of_words_in_the_trio = 2
        if (unconcatenated_transcript[word_counter] == ' '):
            word_trio.append(assembled_word)
            number_of_words_in_the_trio += 1
            assembled_word = ""
        else:
            assembled_word += unconcatenated_transcript[word_counter]
        word_counter += 1
    word_trio.append(assembled_word)
    concatenated_transcript.append(word_trio)
    'since the while loop wont catch the last trio'
            
    return concatenated_transcript

'''
A function which will run the transcript through the reader, get its length,
then run it through the scrubber and the concaenater.
'''
def transcript_processor ():
    transcript_filename = ""
    concatenated_transcript = []
    number_of_three_word_pairs = 0
    '''
    the number of three-word pairs can seem confusing since intuitively it
    should be the number of words / 3 right? Not so. Actually, since we want to
    look at whether any string of three words is duplicated, rather than just
    those in sequential order one-after-the-other, we have to make a trio of
    each successive word. For example, if we had the sentence: "You are riding
    the bus there", the trios would be [you are riding], [are riding the],
    [riding the bus], and [the bus there]. Thus, the number of trios is always
    equal to the number of words, - 2.
    '''
    clean_transcript = ""
    transcript_length = 0
    concatonated_word_count = 0
    transcript_filename = transcript_filename_getter ()
    transcript_with_unreadable_characters = transcript_reader (transcript_filename, 1)
    transcript_length = len(transcript_with_unreadable_characters)
    print("ORIGINAL TRANSCRIPT LENGTH")
    'refers to number of characters'
    print(transcript_length)
    
    clean_transcript = transcript_scrubber (transcript_with_unreadable_characters, transcript_length) 
    transcript_length = len(clean_transcript)
    'updating the length between operations'
    clean_transcript = transcript_scrubber (clean_transcript, transcript_length)
    '''
    first clean deletes any extra spaces and weird characters, second clean
    gets rid of the extra space caused by isolated deleted characters
    '''
    print("CLEAN TRANSCRIPT")
    print(clean_transcript)
    transcript_length = len(clean_transcript)
    print("CLEAN TRANSCRIPT LENGTH")
    'refers to number of characters'
    print(transcript_length)
    
    concatenated_transcript = transcript_concatenater (clean_transcript, transcript_length)
    print("CONCATENATED TRANSCRIPT")
    print(concatenated_transcript)
    number_of_three_word_pairs = len(concatenated_transcript)
    concatonated_word_count = number_of_three_word_pairs + 2
    '''
    see the explanation under number_of_three_word_pairs if youre curious
    about this
    '''
    print("CONCATENATED TRANSCRIPT WORD COUNT")
    print(concatonated_word_count)
    print("CONCATENATED TRANSCRIPT NUMBER OF THREE-WORD PAIRS")
    print(number_of_three_word_pairs)

    return concatenated_transcript


'''
A function which will run the notes through the reader, get its length, then run
it through the scrubber and the concaenater.
'''
def notes_processor ():
    notes_filename = ""
    concatenated_notes = []
    number_of_three_word_pairs = 0
    '''
    the number of three-word pairs can seem confusing since intuitively it
    should be the number of words / 3 right? Not so. Actually, since we want to
    look at whether any string of three words is duplicated, rather than just
    those in sequential order one-after-the-other, we have to make a trio of
    each successive word. For example, if we had the sentence: "You are riding
    the bus there", the trios would be [you are riding], [are riding the],
    [riding the bus], and [the bus there]. Thus, the number of trios is always
    equal to the number of words, - 2.
    '''
    clean_notes = ""
    notes_length = 0
    concatonated_word_count = 0
    notes_filename = notes_filename_getter ()
    notes_with_unreadable_characters = transcript_reader (notes_filename, 0)
    notes_length = len(notes_with_unreadable_characters)
    print("ORIGINAL NOTES LENGTH")
    'refers to number of characters'
    print(notes_length)
    
    clean_notes = transcript_scrubber (notes_with_unreadable_characters, notes_length)
    notes_length = len(clean_notes)
    'updating the length between operations'
    clean_notes = transcript_scrubber (clean_notes, notes_length)
    '''
    first clean deletes any extra spaces and weird characters, second clean
    gets rid of the extra space caused by isolated deleted characters
    '''
    print("CLEAN NOTES")
    print(clean_notes)
    notes_length = len(clean_notes)
    print("CLEAN NOTES LENGTH")
    'refers to number of characters'
    print(notes_length)
    
    concatenated_notes = transcript_concatenater (clean_notes, notes_length)
    print("CONCATENATED NOTES")
    print(concatenated_notes)
    number_of_three_word_pairs = len(concatenated_notes)
    concatonated_word_count = number_of_three_word_pairs + 2
    '''
    see the explanation under number_of_three_word_pairs if youre curious
    about this
    '''
    print("CONCATENATED NOTES WORD COUNT")
    print(concatonated_word_count)
    print("CONCATENATED NOTES NUMBER OF THREE-WORD PAIRS")
    print(number_of_three_word_pairs)

    return concatenated_notes


'''
A function which compares the concatenated transcript and the concatenated notes
and finds the percentage of word trios in the concatenated notes which are
identical to at least one word trio in the concatenated transcript.
'''
def comparer (concatenated_transcript, concatenated_notes):
    empty_list = ["%"]
    concatenated_transcript_length = 0
    concatenated_notes_length = 0
    number_of_marked_trios = 0
    percent_of_identical_notes_trios = 0
    were_there_any_identical_trios = False
    transcript_counter = 0
    'a counter for moving through the transcript word trio by word trio'
    notes_counter = 0
    'a counter for moving through the notes word trio by word trio'
    concatenated_transcript_length = len(concatenated_transcript)
    concatenated_notes_length = len(concatenated_notes)
    print("HITS - IDENTICAL BETWEN BOTH DOCUMENTS")
    while concatenated_transcript_length > transcript_counter:
        while concatenated_notes_length > notes_counter:
            if (concatenated_transcript[transcript_counter] == concatenated_notes[notes_counter]):
                print(concatenated_notes[notes_counter])
                concatenated_notes[notes_counter] = empty_list
                '''
                this marks this trio in the notes as having been a match by
                effectively erasing the word trio and replacing it with a
                marker number_of_marked_triosthat we can trace later to find out
                how many trios were matched. This is necessary, as in the case
                we used a counter variable, then duplicate trios in the
                transcript could match to the same trio in the notes twice or
                more, leading to the possibility of similarity percentages over
                100%.
                '''
                were_there_any_identical_trios = True
            notes_counter += 1
        transcript_counter += 1
        notes_counter = 0
    if (were_there_any_identical_trios == False):
        print("No Hits")
        
    while concatenated_notes_length > notes_counter:
        if (concatenated_notes[notes_counter] == empty_list):
            number_of_marked_trios += 1
        notes_counter += 1
    percent_of_identical_notes_trios = number_of_marked_trios / concatenated_notes_length
    percent_of_identical_notes_trios *= 100
    if (percent_of_identical_notes_trios.is_integer()):
        percent_of_identical_notes_trios = int(percent_of_identical_notes_trios)
    print("PERCENTAGE OF NOTES MATERIAL IDENTICAL TO TRANSCRIPT MATERIAL")
    print(percent_of_identical_notes_trios, empty_list[0])
    
    return percent_of_identical_notes_trios


'''
A function which will ask the user for their original transcript file name and
then provide it to the file reader function.
'''
def transcript_filename_getter ():
    transcript_filename = ""
    transcript_filename = input("Hello! Put in the file name of your original transcript. Remember to add the file extension, You'll have to change the encoding language in the program if it isn't utf-8. The file has to be in the same folder as this program.")

    return transcript_filename

'''
A function which will ask the user for their notes file name and then provide
it to the file reader function.
'''
def notes_filename_getter ():
    notes_filename = ""
    notes_filename = input("And now put in the file name of the notes you'll be comparing with the original. Remember to add the file extension. You'll have to change the encoding language in the program if it isn't utf-8. The file has to be in the same folder as this program.")

    return notes_filename


'''
The main function
'''
def main ():
    go_again = True
    while go_again == True:
        processed_transcript = transcript_processor ()
        processed_notes = notes_processor ()
        comparer (processed_transcript, processed_notes)
        go_again = ""
        while go_again != "yes" and go_again != "no":
            go_again = input("Would you like to do another operation? (yes/no)")
            while go_again != "yes" and go_again != "no":
                go_again =input("(yes/no)")
        if (go_again == "yes"):
            go_again = True
        elif (go_again == "no"):
            go_again = False
    print("Done")

main()
