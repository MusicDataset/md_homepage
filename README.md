# Music dataset

### Why Music Dataset?
Music Dataset is an free, public online platform that hopes to solve the subjecivity in music by collecting response of abstract components in classical music from a variety of audience. It seeks to take advantage the online setting where people from all over the world can be easily connected through one projects. The viewers are asked to place descriptive tags onto music according to the unique response that the particular repotoires evokes in them. Qualities of music, such as the emotion, valence, or excitement level that it is able to bring to the listener, once ambigious and objective, can become specific measurements gvien to music using the help of the general community.

While image classification and recognition have grown increasingly robust in recent years, the field of processing of music using deep learning are still relatively new.

This is due to the amount complexity involved in music. In general, music includes concrete components (e.g. rhythm, tempo, time signature, pitch, key, and tonality) and abstract components (e.g. texture, dynamics, articulation, and timbre). The concret components are straight forward and objective in terms of measurement values and data collection. On the other hand, the abstract component is more subjective and lacks standard of measurement.  As a result, making datasets of subjective and abstract qualities of songs, a critical component of making music accessible to deep learning training, is difficult to achieve.

By labeling the music, I hope the dataset can solve the complexity involved in the abstract components of music, thus allowing it to be analyzed and classified by computer. The ultimate aim is to improve the field of music machine learning by providing a dataset for training.


### How to use it?
So far, the dataset includes 1,276 reportoires, each paired with form that collects responses about the music. They have been sorted for easy find by:
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
Music Dataset is created by a girl passionate about both music and computer science. I have been playing the piano for more than 11 years and am seeking ways to combine these two fields and wishing to make an impact.

The idea was created when the student was working on a music generation model that uses machine learning. I wished to allow the user to input specific characteristics they want in the music, and to achieve that, a curated training data must first be created for data pre-processing. I believe the current music generation models can be greatly improved to become more customizable if a dataset with specific labels are created. Then, when a user prompts for a certain characteristic as input, only songs with corresponding tags would be fed into the training model, and the output result would follow the desire of the user.

While researching about plausible labels to gave to the dataset, I came about the article ["What music makes us feel: At least 13 dimensions organize subjective experiences associated with music across different cultures"](https://www.pnas.org/content/117/4/1924) written by UC Berkeley researchers. This inspired the first three questions in my survey, asking for the emotion (categorized into 13 feelings: amusement, joy, eroticism, beauty, relaxation, sadness, dreaminess, triumph, anxiety, scariness, annoyance, defiance, and feeling pumped up), valence, and excitement level upon hearing a piece of music. Further questions ask for the difficulty levels about these songs, to better sort the dataset as input to the music generation machine learning model, as the input directly determines the style of the output.


[comment]: <In researching about dataset for music machine learning, I came across another music dataset called [MusicNet](https://homes.cs.washington.edu/~thickstn/musicnet.html). However, our aim In the future, I might also like to include other instruments into the dataset, like piano, evokes emotion, how this project's idea was started, why not name it music net?>


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
