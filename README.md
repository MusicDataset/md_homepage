
# Music dataset

### Purpose
Music Dataset is a platform that collects people's emotional responses after listening to classical music. By labeling music with certain tags, I hope the dataset can solve the complexity involved in the abstract components of music, thus allowing it to be analyzed and classified by computer. The ultimate aim is to improve the field of music machine learning by providing a dataset for training.

### How to use it?
The repertoires in this dataset have been sorted for easy find:
1. The first letter of their title in the alphabetical order
2. The music period from which their composer lived in:
   1. Baroque (1600 - 1750)
   2. Classical (1750 – 1820)
   3. Romantic (1820 – 1900)
   4. Impressionism (1890-1920)
   5. Contemporary (1820 – present)
3. The first letter of their composer in the alphabetical order

To contribute to the dataset, you can select a composing genre, artist, or period of your preference. On the page of each individual songs, a playable midi recording (no downloads required, but note that it may takes some time to load), piano tile visuals, and a form which requires inputs from you regarding description labels for the music and some optional questions about your background that would help greatly to data analysis. Please complete as many forms as you can, but don't feel obligated to rush through them. Take the time to relax and to truly appreciate the music and the emotions that it may bring to you. Lastly, I would really appreciate it if you can share this and bring your friends and family to this data collection process as well.

To access the dataset, feel free to email me at MusicDataset@gmail.com.

### Background
Music Dataset is created by a high school student passionate about both music and computer science, who is seeking ways to combine these two fields and wishing to make an impact.

The idea was created when the student was working on a music generation model that uses machine learning. She wished to allow the user to input specific characteristics they want in the music, and to achieve that, a curated training data must first be created for data pre-processing. She believes the current music generation models can be greatly improved to become more customizable if a dataset with specific labels are created. Then, when a user prompts for a certain characteristic as input, only songs with corresponding tags would be fed into the training model, and the output result would follow the desire of the user.

While researching about plausible labels to gave to the dataset, I came about the article ["What music makes us feel: At least 13 dimensions organize subjective experiences associated with music across different cultures"](https://www.pnas.org/content/117/4/1924) written by UC Berkeley researchers. This inspired the first three questions in my survey, asking for the emotion (categorized into 13 feelings: amusement, joy, eroticism, beauty, relaxation, sadness, dreaminess, triumph, anxiety, scariness, annoyance, defiance, and feeling pumped up), valence, and excitement level upon hearing a piece of music. Further questions ask for the difficulty levels about these songs, to better sort the dataset as input to the music generation machine learning model, as the input directly determines the style of the output.

[comment]: <like piano, evokes emotion, how this project's idea was started, why not name it music net?>


### Future improvements
The website and dataset is only in an infancy state, it can be improved in multiple aspects:
1. Modify the website to be able to look for repertoires more easily, such as by adding a "search" option or by adding shortcuts using the alphabet of the first character.
2. Advertise the website to increase the collection of form responses.
3. Devise more labels to be included in the forms that are needed to correctly categorize the music.
4. Add additional music data points to the dataset to possibly include instruments other than the piano.


### Source
Currently, I have included [MAESTRO](https://magenta.tensorflow.org/datasets/maestro) (MIDI and Audio Edited for Synchronous Tracks and Organization) Version 3.0.0 in the dataset. This source is common in music machine learning projects and includes about 200 hours of virtuosic piano performances from the [International Piano-e-Competition](https://piano-e-competition.com).


### Acknowledgement
Huge thank you for:
* [Magenta](https://magenta.tensorflow.org/datasets/maestro) for the MAESTRO Dataset;
* [Hugo](https://gohugo.io/) for the website framework and the easy generation of static sites;
* [Hugo-Initio](https://github.com/miguelsimoni/hugo-initio) for nice looking theme and templates;
* [Hugo taxomies](https://github.com/guayom/hugo-taxonomies) for teaching me how to add the taxonomy organization to the website;
* [Ondřej Cífka](https://github.com/cifkao/html-midi-player) for the awesome html midi player effect;
* And lastly, my dad, for guiding me along when I need help with coding.

For any questions or suggestions about how this dataset can be improved, as well looking to help it expand, please feel free to email MusicDataset@gmail.com or to check out my [Github repo](https://github.com/MusicDataset/MusicDataset.github.io) and [personal homepage](https://ireneyrzd.github.io/).
