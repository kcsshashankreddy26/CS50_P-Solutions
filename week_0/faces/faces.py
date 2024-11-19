#to print the result of the conversion
def main():
#to get the input from the user
    faces = input("How are you gonna convert emoticons into emojis? ")
#calling the convert function
    result = convert(faces)
#printing the result of the conversion
    print(result)
#convert emoticons into emojis and return the string to main() function
def convert(faces):
#converting the first emoticon into  an emoji
    face1 = faces.replace(":)","🙂")
#converting the second emoticon into an emoji
    face2 = face1.replace(":(","🙁")
    return face2

main()

