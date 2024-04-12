def fileNameChange():


    file_input=input()



    with open(file_input, 'r') as f:
        contents = f.read()
        new_list = contents.replace('_photo.jpg', '_info.txt')
        print(new_list)

    return

if __name__ == '__main__':
    fileNameChange()

