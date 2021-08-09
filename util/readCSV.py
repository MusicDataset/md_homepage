import csv
from dsform import *

with open('dataURL_input.csv') as csv_file1:
    csv_reader = csv.reader(csv_file1, delimiter=',')
    line_count = 0
    filename = 'dataURL.csv'

    with open(filename, 'w') as csv_file2:
        # creating a csv writer object
        csv_writer = csv.writer(csv_file2)

        for row in csv_reader:
            if line_count == 0 :
                 fields = ['Composer', 'Title', 'FormID', 'MidiFile', 'FormURL', 'MidiURL']
                 csv_writer.writerow(fields)
                 line_count += 1
            else:
                composer = row[0]
                title = row[1]
                formID = row[2]
                midiFile = row[3]
                print ('Starting ' + composer + ' - ' + title + ' (' + formID + ')')
                if row[4] != '':
                    formURL = row[4]
                    print ('Form URL already exsists')
                else:
                    formURL = createForm(composer, title, formID)
                if row[5] != '':
                    midiURL = row[5]
                    print ('Midi URL already exsists')
                else:
                    midiURL = 'https://OpenMusicDataset.github.io/Maestro/maestro-v3.0.0/' + midiFile
                # writing the data rows
                csv_writer.writerow([composer, title, formID, midiFile, formURL, midiURL])
                print([formURL, midiURL])
                line_count += 1

        print(f'Processed {line_count} lines.')

##csv_file.closed
