import csv
import shutil
import os
import os.path

with open('MaestroV3Dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count == 0 :
             line_count += 1
        else:
            ## Initializing variables with values from csv file
            composer = row[0].strip()
            title = row[1].strip()
            formID = row[2].strip()
            midiFile = row[3].strip()
            formURL = row[4].strip()
            midiURL = row[5].strip()
            period = row[6].strip()

            ## Writing the music file
            first_char = title[0].lower()
            #print(first_char)
            composer = composer.replace('/', '_')
            title_no_space = title.replace(' ', '').replace('/', ',')
            title_motified = title.replace(':', '')
            music_file_name = title_no_space + '(' + formID  + ')-' + composer + '.md'

            ## Writing the music folder
            path = '../content/musics/' + first_char
            if os.path.isdir(path):
                print(first_char + ' folder already exists')
            else:
                os.mkdir(path)
                print('new folder ' + first_char + ' is made')

            ## Writing the music file
            music_file_object = open(path + "/" + music_file_name, "w")
            music_file_object.write('---\n')
            music_file_object.write('title: ' + composer + ' - ' + title_motified + ' (' + formID  + ')\n')
            music_file_object.write('description: This is the description for ' + title_motified + ' by ' + composer +'\n')
            music_file_object.write('composers: [' + composer + ']\n')
            music_file_object.write('periods: [' + period + ']\n')
            music_file_object.write('audioURL: ' + midiURL + '\n')
            music_file_object.write('formURL: ' + formURL + '\n')
            music_file_object.write('comments: true\n')
            music_file_object.write('share: true\n')
            music_file_object.write('date: 2021-08-08T07:43:13-06:00\n')
            music_file_object.write('---\n')
            music_file_object.close()
            print(music_file_name + ' done')

            ## Creating the Composer folder and description
            path = '../content/composers/' + composer
            composer_for_wiki = ''
            if os.path.isdir(path):
                print(composer + ' already exists')
            else:
                os.mkdir(path)
                for x in range (0, len(composer), 1):
                    if composer[x] == '/':
                        pass
                    else:
                        composer_for_wiki = composer_for_wiki + composer[x]
                composer_for_wiki = composer_for_wiki.replace(' ', '_')
                wiki_url = 'https://en.wikipedia.org/wiki/' + composer_for_wiki
                composer_file_object = open(path + '/_index.md', 'w')
                composer_file_object.write('---\n')
                composer_file_object.write('title: ' + composer + '\n')
                composer_file_object.write('description: This is the description for ' + composer + '\n')
                composer_file_object.write('wikipedia: ' + wiki_url + '\n')
                composer_file_object.write('taxonomy_indexes: true\n')
                composer_file_object.write('---\n')
                composer_file_object.close()
                print(composer + ' done')

            #source = '.'
            #destination = './' + first_char
            #new_path = shutil.move(source, destination)
            #line_count += 1

        print(f'Processed {line_count} lines.')
